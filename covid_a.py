from endpoints.endpoint_mock import TestEndpointMock

class Cluster:

    def __init__(self, role):
        self._role = role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role


if __name__ == '__main__':

    # generate a new endpoint
    mock1 = TestEndpointMock('1.1.1.1', 'Mock1', 'test@example.com', 'DX', 'portal_a', 'status')
    # specify type - DX, SX

    # specify role = portal_a, portal_b (if portal_b, cart or desk)
    # specify status = online, offline (if online, instantiate DX, if offline, mock object)
    # clusters
    # a cluster = portal_a
#     b cluster = portal_b
#
#
