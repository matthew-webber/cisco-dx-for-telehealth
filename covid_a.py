class PatientCluster:

    def __init__(self, role):
        self._role = role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

class ProviderCluster:

    def __init__(self):
        pass


