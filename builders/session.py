import requests
from urllib3.exceptions import NewConnectionError  # todo is this still needed?


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
                               test_url=login_data['test_url'])
        elif login_data:
            # create new auth session
            return AuthSession(credentials=login_data['credentials'],
                                  login_url=login_data['login_url'],
                                  test_url=login_data['test_url'])
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
        """
        Attempts to create a session and get data to confirm that credentials are good.
        Runs self.secure() at end of init which returns an instance of AuthSession and a string
        representing the result of the attempt.
        :param credentials:
        :param login_url:
        :param test_url:
        :param session:
        """
        self.online = False
        self.session = session
        self._data_fetcher = DataFetcher(login_url=login_url, url=test_url)
        self.credentials = credentials
        self.user, self.password = None, None
        self.result_msg = None

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
                    self.result_msg = 'ERROR: Connection timed out.'
                    break
                except Exception as e:
                    self.result_msg = 'ERROR: Connection refused (or something else).'
                    break

                self.user = user
                self.password = pw
                self.online = True
                self.result_msg = "SUCCESS: Connection established."
                return


            #
            # if self.online:
            #     return self, self.result_msg
            # else:
            #     break

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