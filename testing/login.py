from dicts import xml_dict


class SessionTester:

    fail_codes = [400, 401]

    def __init__(self, session, url, headers=""):
        self.session = session
        self.url = url
        self.headers = headers
        self._test_pass = None

    @property
    def test_pass(self):
        return self._test_pass

    @test_pass.setter
    def test_pass(self, result):
        self._test_pass = result

    def test_session(self):

        data = dict(
            session=self.session,
            url=self.url,
            headers=self.headers,
        )

        response = self.get_url(data)
        result = self.check_response(response)

        self.test_pass = result

        # tester = SessionTester.get_tester(test_type)
        # return SessionTester.test_session(tester)

    @staticmethod
    def check_response(response):
        return response.status_code not in SessionTester.fail_codes

    @staticmethod
    def get_url(data):
        return data['session'].get(data['url'], headers=data['headers'])

        #
        # """Return True if only one test fails"""
        #
        # if self.ps_test_401() * self.ps_test_400():
        #     self.status = 'Success'
        # else:
        #     self.status = 'Failure'

    def ps_test_401(self):

        return self.response == 401

    def ps_test_400(self):

        return self.response == 400

    def update_pw(self):

        pass

# SessionUpdater class

# instantiate with session obj, response obj
# methods: update password, test session


class SessionUpdater:

    def udpate_password(self, session):
        session.password



if __name__ == "__main__":
    pass
    # from collections import namedtuple
    #
    # Session = namedtuple('TestSession', 'pw')
    # Response = namedtuple('TestResponse', 'status_code')
    #
    # test_session = Session(pw='password')
    # test_response = Response(status_code=401)


    # myDX = Endpoint('10.27.200.140')  # myDX

    # test = dict(
    #     url=xml_dict['status']['device_name'].replace('{{}}', myDX.ip),
    #     headers=xml_dict['headers'],
    # )

