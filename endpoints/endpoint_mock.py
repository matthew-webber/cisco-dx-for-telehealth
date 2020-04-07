class MockEndpoint:

    def __init__(self, endpoint_data):
        self.ip = endpoint_data['ip']
        self.name = endpoint_data['name']
        self.call_string = endpoint_data['call_string']

        # these will be defined by the role definer / provisioner post instantiation
        self._role, self._type, self._directives = None, None, None

        # self.status = endpoint_data['status']
        # print(f'Logging in to {self.ip}...')
        # print(f'Success!')

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type_):
        self._type = type_

