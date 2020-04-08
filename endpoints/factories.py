from helpers.endpoint_helpers import *
from creds import endpoint_data
from endpoints.endpoint_dx import DX
from endpoints.endpoint_sx import SX
from ixml import *
from endpoints.endpoint_mock import MockEndpoint
from builders.session import *
from multiprocessing.pool import ThreadPool
from time import sleep


class EndpointFactory:

    def __init__(self, queue, **kwargs):
        """
        FIRE IT UP, LER!! **VRRROOOM!!**
        :param queue: list of IPs
        :param kwargs: empty dict of expected output structure (e.g. {'online': None, 'offline': None}
        """
        self.queue = queue  # list of IPs
        self.endpoints_types = {k: [] for k in kwargs.keys()}
        self.endpoint_data = endpoint_data.copy()

        self.online_queue = list(dict())  # queue for online EPs contains IP and AuthSession object
        self.offline_queue = list()  # queue for offline EPs only need an IP

    def process_queue(self, multiprocessor=True):
        """Puts each IP address in the factory queue through the factory sorter"""

        print("Determining network status of endpoints...")
        if multiprocessor is True:
            ip_pool = ThreadPool()
            pool_results = list()

            for ip in self.queue:
                pool_results.append(ip_pool.apply_async(self.test_endpoints, (ip,)))
                sleep(0.1)

            ip_pool.close()
            ip_pool.join()

            test_results = [pool_result.get() for pool_result in pool_results]

        else:
            test_results = list()

            for ip in self.queue:
                test_results.append(self.test_endpoints(ip))

        self.sort_test_results(test_results)


    def test_endpoints(self, ip):
        """
        # todo change the below
        Determine if an endpoint is online by attempting to get the "ProductPlatform" xml node associated
        with that endpoint's IP in the "Status" API group.  If it doesn't time out, then the ep is considered
        online and the IP + session are passed back up to be added to the online queue.  If it does timeout
        or the connection is refused, the IP is passed to the offline queue.

        :param ip: endpoint IPv4 address
        # todo change return here
        :return: nothing -- add data to respective self.queue
        """

        data_copy = self.endpoint_data.copy()  # create fresh data object for each endpoint

        # grab a session using data added to method
        data_copy['login_url'] = data_copy['login_url'].replace('$ip', ip)
        data_copy['test_url'] = data_copy['test_url'].replace('$ip', ip)
        session = EndpointFactory.add_session(data_copy)

        # print result of endpoint testing

        print_spacer = 17 - len(ip)  # for pretty printing
        print(f'\t[{ip}]{" " * print_spacer} {session.result_msg}')

        return dict(ip=ip, session=session)

    def sort_test_results(self, test_results):

        for result in test_results:
            ip = result.get('ip')
            session = result.get('session')

            if session.online:  # if cart not online, None should be returned as session
                self.online_queue.append(dict(ip=ip, session=session.session))
            else:
                self.offline_queue.append(ip)

    def package_endpoints(self, mode="DEFAULT"):
        """
        Create endpoints from the online/offline lists of endpoints populated by the queue
        processor / endpoint sorter and sends to the storage class

        :return: a storage instance with all online/offline endpoint objects
        """

        # call the generator to populate endpoint storage
        payload = self.endpoint_generator(mode)

        return EndpointStorage(payload)

    def endpoint_generator(self, mode):
        """
        Takes a list of endpoint IPs and generates either a...

            * live endpoint (DX, SX, etc.), or
            * a mock object (ibid)

        ...and returns a dictionary of these objects.
        :param mode:
        :return: dict()
        """

        online = list()
        offline = list()

        if mode == 'DEFAULT' or mode == 'ONLINE':
            for endpoint in self.online_queue:
                online_endpoint = EndpointFactory.online_ep_generator(endpoint['session'], endpoint['ip'])
                # self.endpoints_types['online'].append(online_endpoint)  # add new endpoint to storage
                # print(f"\tCreated endpoint for {online_endpoint.name}!")
                online.append(online_endpoint)  # add new endpoint to storage

        # don't need to iterate because mock factory takes a list, not endpoint
        if self.offline_queue and (mode == 'DEFAULT' or mode == 'OFFLINE'):
            endpoint_generator = EndpointFactory.offline_ep_generator(MockEndpointFactory())
            offline_endpoints = endpoint_generator(self.offline_queue)
            # self.endpoints_types['offline'].append(offline_endpoints['offline'])
            # print(f"\tCreated {len(offline_endpoints['offline'])} offline endpoint(s)!")
            # for offline_endpoint in offline_endpoints['offline']:
                # print(offline_endpoint.name)
            offline = offline + offline_endpoints['offline']

        return dict(online=online, offline=offline)

    @staticmethod
    def offline_ep_generator(mock_factory):
        return mock_factory.process_data

    @staticmethod
    def online_ep_generator(session, ip):

        # get product platform to determine what type of endpoint to make
        status_xml = ET.fromstring(session.get(f'http://{ip}/getxml?location=Status').text)
        endpoint_model = get_xml_value("ProductPlatform", status_xml)[0].text
        # print(f'Endpoint model is {endpoint_model}')

        online_generator = EndpointFactory._get_generator(endpoint_model)
        return online_generator(session, status_xml, ip=ip)

    @staticmethod
    def add_session(data):
        return SessionModule.create_session(login_data=data)

    @staticmethod
    def _get_generator(endpoint_model):
        if endpoint_model in ['DX70', 'DX80']:
            return EndpointFactory._make_DX
        elif endpoint_model in ['SX20']:
            return EndpointFactory._make_SX
        else:
            return ValueError(endpoint_model)

    @staticmethod
    def _make_DX(session, status_xml, ip):
        return DX(session, status_xml, ip)

    @staticmethod
    def _make_SX(session, status_xml):
        return SX()


class MockEndpointFactory:

    def __init__(self):
        self.mock_data = MockDataDaemon.pull_all_data()  # prep the factory by gathering all data from the .csv file

    def process_data(self, ip_list: list):
        """
        Uses the mock data daemon to perform an iterative search over the mock data
        and put these into containers for the parent factory to use

        :param ip_list: list of IPs to create objects for
        :return: dict of lists for mock objs and objects not in the .csv file
        """
        # create another list of dicts with {ip : row_data}
        # that way, if the row data isn't there, it can bring a "None" object back to the parent factory
        # and more processing can take place
        matching_data = {ip: MockDataDaemon.search_data(self.mock_data, ip) for ip in ip_list}

        # make mock objects if they have data
        mock_objects = [MockEndpointFactory.create(data_match) for ip, data_match
                        in matching_data.items() if data_match]

        # todo make the above and below look better -- shouldn't be making 2 lists here...

        # if data_match is None, these IPs didn't exist in the table
        # pass them up to the parent factory
        unknown_ips = [ip for ip, data_match
                       in matching_data.items() if not data_match]

        if unknown_ips: print('Unknown IPs ignored!', unknown_ips)

        return dict(offline=mock_objects)

    @staticmethod
    def create(mock_object_data):
        return MockEndpoint(mock_object_data)


if __name__ == '__main__':

    all_data = MockDataDaemon().pull_all_data()
    endpoint_ips = [endpoint['ip'] for endpoint in all_data]
    # endpoint_ips = ['10.33.155.0', '10.33.110.0', '10.33.110.200']

    factory = EndpointFactory(endpoint_ips)

    factory.process_queue(multiprocessor=True)

