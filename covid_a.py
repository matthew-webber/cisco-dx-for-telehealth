from endpoints.endpoint_mock import *
import requests
import xml.etree.ElementTree as ET
from creds import endpoint_data
from endpoints.endpoint_dx import DX
from endpoints.endpoint_sx import SX
from ixml import *
import re
from urllib3.exceptions import NewConnectionError


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


class EndpointFactory:

    def __init__(self, queue):
        self.queue = queue  # list of IPs

    def process_queue(self):
        """
        Takes a list of endpoint IPs and generates either a...

            * live endpoint (DX, SX, etc.), or
            * a mock object (ibid)

        ...and returns a dictionary of these objects.

        "Online" = live endpoints
        "Offline" = mock objects
        "Unknown" = IP not online and not in mock data .csv file

        :return: dict()
        """

        endpoints = list()
        mock_objects = list()

        for ip in self.queue:
            endpoint = EndpointFactory.create(endpoint_data.copy(), ip)
            if endpoint:
                endpoints.append(endpoint)
            else:
                mock_objects.append(ip)

        if mock_objects:
            factory = MockEndpointFactory()

            endpoint_dict = factory.process_data(mock_objects)
            endpoint_dict['online'] = endpoints

        else:
            endpoint_dict = {'online': endpoints}

        return endpoint_dict

    @staticmethod
    def create(data, ip, status='Online'):
        """
        Create a session, grab the status.xml, and then create an endpoint with attached session and XML data
        If session can't be created, get help from the mock object factory

        :param data: dict of endpoint data
        :param ip: endpoint IPv4 address
        :param status: Online/Offline string
        :return:
        """
        # grab a session using data added to method
        data['login_url'] = data['login_url'].replace('$ip', ip)
        data['test_url'] = data['test_url'].replace('$ip', ip)
        print(f'Logging into {ip}...')
        session = EndpointFactory.add_session(data)

        if not session:  # if cart not online, None should be returned as session
            return None

        # get product platform to determine what type of endpoint to make
        status_xml = ET.fromstring(session.get(f'http://{ip}/getxml?location=Status').text)
        endpoint_model = get_xml_value("ProductPlatform", status_xml)[0].text
        print(f'Endpoint model is {endpoint_model}')

        generator = EndpointFactory._get_generator(endpoint_model)
        return generator(session, status_xml)

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
    def _make_DX(session, status_xml):
        return DX(session, status_xml)

    @staticmethod
    def _make_SX(session, status_xml):
        return SX()


class Endpoint:

    def __init__(self):
        pass


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
                    print('Connection timed out.')
                    break
                except Exception as e:
                    print('Max retries with URL... or something else...?')
                    break

                # print(f'Log in success with "{user}":"{pw}"')
                print(f'Logged in succesfully!')

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
            return session.get(self.url, timeout=2, allow_redirects=False).status_code
        except requests.ReadTimeout:
            return 401
        except requests.exceptions.ConnectTimeout:
            return 'FAILED_CONNECTION'
        except ConnectionRefusedError:
            return 'REFUSED_CONNECTION'


class RoleDefiner:

    # import re
    # identifiers = {'patient': [identifiers]}
    # sorter = EndpointSorter(identifiers)
    # sorted_endpoints = [sorter.get_role(endpoint, add_flag=True) for endpoint in [unsorted_endpoints]]

    def __init__(self, patient_identifiers, provider_types, add_flag):
        self.patient_identifiers = patient_identifiers
        self.provider_types = provider_types
        self.flag = add_flag

    def get_role(self, endpoint):

        # if name not like any identifiers, it must be a provider
        role = 'provider'

        for identifier in self.patient_identifiers:
            match = re.search(identifier, endpoint.name)  # it's in the patient_identifiers list...
            if match:
                role = 'patient'

        # return {'role': role}
        return role

    def get_type(self, provider_endpoint):

        type_ = "Unknown"

        for provider_type in self.provider_types:
            match = re.search(provider_type.upper(), provider_endpoint.name.upper())
            if match:
                type_ = match[0]

        # if not in self.provider_types, it's an unknown type
        return {"type": type_}


class EndpointSorter:

    def __init__(self):
        pass


class Directives:

    def __init__(self, input_queue):
        self.queue = input_queue

    @staticmethod
    def add_directives():
        pass


if __name__ == '__main__':

    # todo TEST if running this when a DX is on gets the proper online vs mock object (run, reboot + run)

    # all_data = MockDataDaemon().pull_all_data()
    # endpoint_ips = [endpoint['ip'] for endpoint in all_data]
    role_definer = RoleDefiner(patient_identifiers=['CART', 'DX-PATIENT'],
                               provider_types=['DX-NS', 'TELEPOD', 'ID-NS', 'TRIAGE'])
    endpoint_ips = ['10.33.112.74', '10.33.100.145']
    factory = EndpointFactory(endpoint_ips)

    endpoints = factory.process_queue()


    # with open('testing/status.xml', 'r') as f:
    #     root = ET.fromstring(f.read())
    #
    # thisthat = get_nested_xml(root, 'UserInterface', 'ContactInfo', 'Name')

    # thisthat = EndpointFactory(data=endpoint_data, ip=ip)
    # resp = thisthat.post(f'http://{ip}/web/signin/open', headers=headers)
    # type_ = thisthat.get(f'http://{ip}/getxml?location=Status', headers={'Content-Type': 'application/xml'})
    # type_ = ET.fromstring(type_.text)
    # target = "ProductPlatform"

    # iurl = 'http://$ip/web/signin/open'
    #
    # endpoint_data = {'login_url': iurl, 'ip': ip}


# if online, check what type of object it is
#     logon, get ProductPlatform from status
#     create object based on result
#     store status xml with object
# if offline, get last known type from csv list and make mock object