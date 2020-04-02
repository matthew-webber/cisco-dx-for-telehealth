from endpoints.endpoint_mock import TestEndpointMock
import requests
import xml.etree.ElementTree as ET
from creds import endpoint_data
from endpoints.endpoint_dx import DX
from endpoints.endpoint_sx import SX
from ixml import *


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

        # endpoints = []
        #
        # for ip in self.queue:
        #     data = endpoint_data.copy()
        #     endpoints.append(EndpointFactory.create(data, ip))

        endpoints = [EndpointFactory.create(endpoint_data.copy(), ip) for ip in self.queue]

        return endpoints  # list of endpoints


    @staticmethod
    def create(data, ip, status='Online'):
        """
        Create a session, grab the status.xml, and then create an endpoint with attached session and XML data
        :param data: dict of endpoint data
        :param ip: endpoint IPv4 address
        :param status: Online/Offline string
        :return:
        """
        # grab a session using data added to method
        data['login_url'] = data['login_url'].replace('$ip', ip)
        data['test_url'] = data['test_url'].replace('$ip', ip)
        session = EndpointFactory.add_session(data)

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

        if session and login_data:
            # authorize current session
            return AuthSession(credentials=login_data['credentials'],
                               login_url=login_data['login_url'],
                               test_url=login_data['test_url']).session
        elif login_data:
            # create new auth session
            return AuthSession(credentials=login_data['credentials'],
                               login_url=login_data['login_url'],
                               test_url=login_data['test_url']).session
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
        self._secure = False
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
                    print(f'Log in failed with "{user}":"{pw}"')
                    continue  # try next pw
                except TimeoutError:
                    print('returning None')
                    break
                    return None

                print(f'Log in success with "{user}":"{pw}"')
                self.user = user
                self.password = pw
                self._secure = True
                break

            if self._secure:
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

        print(f'Fetching data from {self.url}')
        try:
            return session.get(self.url, timeout=2, allow_redirects=False).status_code
        except requests.ReadTimeout:
            return 401
        except requests.exceptions.ConnectTimeout:
            return 'FAILED_CONNECTION'


if __name__ == '__main__':

    endpoint_ips = ['10.27.200.140', '10.33.110.119']
    factory = EndpointFactory(endpoint_ips)
    endpoints = [endpoint for endpoint in factory.process_queue()]

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