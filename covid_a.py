from endpoints.endpoint_mock import TestEndpointMock
import requests
import xml.etree.ElementTree as ET
from creds import endpoint_credentials

class Cluster:

    def __init__(self, role):
        self._role = role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    class EndpointFactory:

        def __init__(self, data):
            # determine object model
            self.session = SessionModule(data={'url': endpoint_data.get('login_url'), 'ip': ip})

        def factory(self):
            pass

        def get_status(target, xml):
            return [tag.text for tag in xml.iter(target)][0]

    class DX2:


        def refresh_status(self):
            pass

    class AuthSession:

        def __init__(self, session, credentials):
            self._secure = False
            self.credentials = credentials
            self.user, self.password = credentials.get('username')[:], credentials.get('password')[:]

            if session:
                self._session = session
            else:
                self._session = RegSession.session

        def secure(self, data_fetcher):
            for user in self.user:
                for pw in self.password:
                    response = data_fetcher.login(user, pw)
                    while response.code == 401:
                        response = data_fetcher.login(user, pw)
                        print(f'Logged in failed with {user}:{pw}')

                    print(f'Logged in success with {user}:{pw}')
                    self.user = user
                    self.password = pw

    class RegSession:

        def __init__(self):
            self._session = requests.session()

        @property
        def session(self):
            return self._session

    class SessionModule:

        def __init__(self, credentials=None, session=None, start_session: bool = True, start_auth_session: bool = True):
            self.data_fetcher = DataFetcher()

            session_generator = SessionModule.get_session
            self._session = self.session_generator(session, credentials)
            self.response = None
            self._credentials = endpoint_credentials

            if start_auth_session:
                self._session = self.init_auth_session()
                print('Authenticated session ready.')
            elif start_session:
                self._session = self.init_session()
                print('Regular session ready.')

        def get_session(self, session, credentials):

            if session and credentials:
                # authorize current session
                return AuthSession(session, credentials)
            elif credentials:
                # create AuthSession
                pass
            else:
            #     create regular Session
                pass

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


class DataFetcher:

    def __init__(self):
        # self.target = target
        # self.login_required = login_required
        pass

    def login(self, url, parameters=None):
        if not self._session:
            return 'Cannot post to non-existent session'

        print(f'Logging in to {url}')
        self._session.post(url, headers=parameters)

    def fetch_data(self, target, login_url=None, login_required=True):

        if not self._session:
            return 'Cannot fetch data without session'

        if login_required:
            self.login(login_url)

        print(f'Fetching data from {target}')
        return self._session.get(target)


if __name__ == '__main__':

    # generate a new endpoint
    # mock1 = TestEndpointMock('1.1.1.1', 'Mock1', 'test@example.com', 'DX', 'portal_a', 'status')
    # specify type - DX, SX

    # specify role = portal_a, portal_b (if portal_b, cart or desk)
    # specify status = online, offline (if online, instantiate DX, if offline, mock object)
    # clusters
    # a cluster = portal_a
    #     b cluster = portal_b
    ip = '10.27.200.140'
    thisthat = requests.session()
    thisthat.auth = ('admin', '')
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    resp = thisthat.post(f'http://{ip}/web/signin/open', headers=headers)
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