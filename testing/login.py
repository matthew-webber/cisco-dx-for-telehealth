class SessionTester:

    fail_codes = [400, 401]

    @staticmethod
    def test_session(session, test_type=0, url, headers=""):
        # self.response = response
        # self.status = None
        # self.test_session()
        data = dict(
            session=session,
            url=url,
            headers=headers,
        )
        response = SessionTester.test_session(data)
        result = SessionTester.check_response(response)


        # tester = SessionTester.get_tester(test_type)
        # return SessionTester.test_session(tester)

    @staticmethod
    def check_response(response):
        if response.status_code in SessionTester.fail_codes

    @staticmethod
    def test_session(data):
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

    from collections import namedtuple

    Session = namedtuple('TestSession', 'pw')
    Response = namedtuple('TestResponse', 'status_code')

    test_session = Session(pw='password')
    test_response = Response(status_code=401)

    thisthat = SessionTester(test_session, test_response)

