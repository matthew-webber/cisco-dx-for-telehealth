from endpoints.endpoint_mock import *
import requests
import xml.etree.ElementTree as ET
from creds import endpoint_data
from endpoints.endpoint_dx import DX
from endpoints.endpoint_sx import SX
from ixml import *
from urllib3.exceptions import NewConnectionError  # todo is this still needed?
from data.teleport_data import TeleportProvisioner


class Cluster:

    def __init__(self, role):
        self._role = role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role


class XmlProcessor:

    pass


class EndpointStorage:

    def __init__(self, endpoints):
        self.online = endpoints['online']
        self.offline = endpoints['offline']

    def add_endpoints(self, endpoints, status):
        """# todo """
        if status == "ONLINE":
            self.online.append(endpoints)
        elif status == "OFFLINE":
            self.offline.append(endpoints)


class EndpointFactory:

    def __init__(self, queue, **kwargs):
        """
        FIRE IT UP, LER!! **VRRROOOM!!**
        :param queue: list of IPs
        :param kwargs: empty dict of expected output structure (e.g. {'online': None, 'offline': None}
        """
        self.queue = queue  # list of IPs
        self.endpoints_types = {k: [] for k in kwargs.keys()}
        self.online_queue = list(dict())  # online endpoints need to store pairing session
        self.offline_queue = list()  # offline endpoints can just be IPs
        self.endpoint_data = endpoint_data.copy()

    def process_queue(self):
        """Puts each IP address in the factory queue through the factory sorter"""

        for ip in self.queue:
            self.endpoint_sorter(ip)

    def package_endpoints(self, mode="DEFAULT"):
        """
        Create endpoints from the online/offline lists of endpoints populated by the queue
        processor / endpoint sorter and sends to the storage class

        :return: a storage instance with all online/offline endpoint objects
        """

        # call the generator to populate endpoint storage
        payload = self.endpoint_generator(mode)

        return EndpointStorage(payload)

    def endpoint_sorter(self, ip):
        """
        # todo change the below
        Determine if an endpoint is online by attempting to get the "ProductPlatform" xml node associated
        with that endpoint's IP in the "Status" API group.  If it doesn't time out, then the ep is considered
        online and the IP + session are passed back up to be added to the online queue.  If it does timeout
        or the connection is refused, the IP is passed to the offline queue.

        :param ip: endpoint IPv4 address
        :return: nothing -- add data to respective self.queue
        """
        data_copy = self.endpoint_data.copy()  # create fresh data object for each endpoint

        # grab a session using data added to method
        data_copy['login_url'] = data_copy['login_url'].replace('$ip', ip)
        data_copy['test_url'] = data_copy['test_url'].replace('$ip', ip)
        print(f'\tLogging into {ip}...')
        session = EndpointFactory.add_session(data_copy)

        if session:  # if cart not online, None should be returned as session
            self.online_queue.append(dict(ip=ip, session=session))
        else:
            self.offline_queue.append(ip)

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
                print(f"\tCreated endpoint for {online_endpoint.name}!")
                online.append(online_endpoint)  # add new endpoint to storage

        # don't need to iterate because mock factory takes a list, not endpoint
        if self.offline_queue and (mode == 'DEFAULT' or mode == 'OFFLINE'):
            endpoint_generator = EndpointFactory.offline_ep_generator(MockEndpointFactory())
            offline_endpoints = endpoint_generator(self.offline_queue)
            # self.endpoints_types['offline'].append(offline_endpoints['offline'])
            print(f"\tCreated {len(offline_endpoints['offline'])} offline endpoint(s)!")
            for offline_endpoint in offline_endpoints['offline']:
                print(offline_endpoint.name)
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


class SessionModule:

    @staticmethod
    def create_session(login_data=None, session=None, start_session: bool = True, start_auth_session: bool = True):

        session_generator = SessionModule.get_session
        session = session_generator(session=session, login_data=login_data)
        return session

    @staticmethod
    def get_session(session, login_data):

        online = False

        if session and login_data:
            # authorize current session
            return AuthSession(credentials=login_data['credentials'],
                               login_url=login_data['login_url'],
                               test_url=login_data['test_url']).session
        elif login_data:
            # create new auth session
            session_ = AuthSession(credentials=login_data['credentials'],
                                  login_url=login_data['login_url'],
                                  test_url=login_data['test_url'])

            # a connection timeout should return None so a mock obj can be created
            if session_.online:
                online = True

            if online:
                return session_.session
            else:
                return None

        else:
            # create new non-auth session
            return RegSession

    def session_generator(self):
        pass

    def make_authsession(self):
        pass

    def make_regsession(self):
        pass

    def apply_credentials(self):
        pass

    def init_session(self):

        # if there's not already a session, start one
        if not self._session:
            print('Creating session object...')
            return requests.Session()
        else:
            print('Session object already exists.')
            return self._session

    def init_auth_session(self):

        auth_session = self.init_session()
        print('Session ready for credentials')

        return auth_session

    def update_data(self, target, login_url=None):
        self.response = self.data_fetcher.fetch_data(target=target, login_url=login_url)  # todo refactor to 'renew_data_fetcher' and 'update_data'


class AuthSession:

    def __init__(self, credentials, login_url, test_url, session=None):
        self.online = False
        self.session = session
        self._data_fetcher = DataFetcher(login_url=login_url, url=test_url)
        self.credentials = credentials
        self.user, self.password = None, None

        if not self.session:
            self.session = RegSession.session()

        self.secure()

    def secure(self):
        # self._data_fetcher.login(self.session)  # start session
        for user in self.credentials.get('username'):
            for pw in self.credentials.get('password'):
                # user = next(self.user)
                # pw = next(self.password)
                self.session.auth = (user, pw)  # first test all passwords with username 1, then with username 2...
                try:
                    self.test_connection()
                except ConnectionError:
                    # print(f'Log in failed with "{user}":"{pw}"')
                    continue  # try next pw
                except (NewConnectionError, TimeoutError):
                    print('\tERROR: Connection timed out.')
                    break
                except Exception as e:
                    print('\tERROR: Max retries with URL... or something else...?')
                    break

                # print(f'Log in success with "{user}":"{pw}"')
                # print(f'Logged in succesfully!')

                self.user = user
                self.password = pw
                self.online = True
                break

            if self.online:
                break  # connection established, don't try another username
            else:
                return None

    def test_connection(self):

        status_code = self._data_fetcher.fetch_data(self.session)  # returns 401 if timeout/actual 401 gotten

        while status_code == 401:
            raise ConnectionError("Connection failed")  # try next

        if status_code == 'FAILED_CONNECTION':
            raise TimeoutError("Connection timed out") # create mock object



class RegSession:

    @staticmethod
    def session():
        return requests.session()


class DataFetcher:

    def __init__(self, login_url=None, url=None):
        self._login_url = login_url
        self._url = url
        pass

    @property
    def login_url(self):
        return self._login_url

    @login_url.setter
    def login_url(self, url):
        self._login_url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    # def login(self, session, headers=None):
    #     # ensure login_url has been passed to method
    #     while not self.login_url:
    #         self.login_url = input('Cannot login without login_url\n')
    #
    #     print(f'Logging in to {self.login_url}')
    #     return session.post(self.login_url, headers=headers)

    def fetch_data(self, session):

        # print(f'Fetching data from {self.url}')
        try:
            return session.get(self.url, timeout=2).status_code
        except requests.ReadTimeout:
            return 401
        except requests.exceptions.ConnectTimeout:
            return 'FAILED_CONNECTION'
        except ConnectionRefusedError:
            return 'REFUSED_CONNECTION'


# class Directives:
#
#     def __init__(self, **kwargs):
#         self.directives =
#
#     @staticmethod
#     def add_directives():
#         pass
#

if __name__ == '__main__':

    # todo TEST if running this when a DX is on gets the proper online vs mock object (run, reboot + run)

    all_data = MockDataDaemon().pull_all_data()
    endpoint_ips = [endpoint['ip'] for endpoint in all_data]

    # endpoint_ips = [
    #     '10.33.100.145',  # DX-PATIENT 10 live but "offline"
    #     '10.33.112.74',  # NS-02 LIVE!!!!!!
    #     '10.27.200.140',  # my DX
    #     '10.33.114.35',  # telepod
    #     '10.33.48.18',  # triage
    #     '10.33.121.109',  # DX-5C-02
    # ]

    print("Creating factory...")
    factory = EndpointFactory(endpoint_ips)  # create factory + pass IPs to queue
    print("Determining network status of endpoints...")
    factory.process_queue()  # sort endpoints into online / offline queues
    print("\nSorting + packaging endpoints...")
    package = factory.package_endpoints()  # process queues and put into endpoint container
    print("\nCreating TeleportProvisioner...")
    provisioner = TeleportProvisioner()  # create provisioner to outfit endpoints for Teleport work
    print("Provisioning endpoints with types/roles...")
    provisioner.typify(package.online + package.offline)  # add Teleport types / roles to endpoints
    print("Provisioning endpoints with directives/favorites...\n")

    """for pretty printing"""
    lengths = [len(ep.name) for ep in package.online]
    long_name = max(lengths)

    for endpoint in package.online:  # currently, online providers are the only endpoints that get directives
        provisioner.add_directives(endpoint)  # add directives depending on role + type
        favorites = provisioner.define_favorites(endpoint)  # create favorites "to-be-added" to endpoint
        # print(favorites, f' for {endpoint.name}, {endpoint.type}')
        if favorites:
            endpoint.collect_favorites(package.online + package.offline, favorites)
            print(f"\t{endpoint.name}{'.' * (long_name - len(endpoint.name))}.. ({len(endpoint._favorites)}) favorites, ({len(endpoint.directives)}) directives")

    print(f"\n{len(package.online)} Teleports are locked and loaded!")

    myDX = package.online[-1]

# todo refresh offline endpoints to see if they're online again instead of having to run the whole thing over again

'''
Wishlist:

1. Refresh "offline" endpoints
        
        Pull up a list of offline endpoints ("status check") and then choose to refresh either all ("refresh all") or 
        refresh a specific endpoint ("refresh <index of endpoint from status check list>").  The objects would be
        checked again and moved from offline > online if necessary.
        
2. Check for conflicts b/t .csv file and live endpoint data

        Compare / contrast the data associated with an IP address across the .csv file and the data in a live endpoint.
        If a discrepancy is found, print the discrepancy and ask user if they want to update the .csv file or the
        endpoint itself using API calls (feel like this would be rare because the .csv is likely to be the inaccurate
        one).
        
'''

