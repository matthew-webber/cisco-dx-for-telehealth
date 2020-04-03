import re


class RoleDefiner:

    # import re
    # identifiers = {'patient': [identifiers]}
    # sorter = EndpointSorter(identifiers)
    # sorted_endpoints = [sorter.get_role(endpoint, add_flag=True) for endpoint in [unsorted_endpoints]]

    def __init__(self, patient_types, provider_types, add_flag=True):
        self.patient_types = patient_types
        self.provider_types = provider_types
        self.flag = add_flag

    # def define_roles(self, endpoint_name):
    #
    #     role, type_ = self.get_role(endpoint_name)
    #     # type_ = self.get_type(endpoint_name)
    #
    #     return {'role': role, 'type': type_}

    def define_roles(self, endpoint_name):

        # if name not like any identifiers, it must be a provider
        role = 'unknown'
        type_ = 'unknown'

        for patient_type in self.patient_types:
            match = re.search(patient_type, endpoint_name)  # it's in the patient_identifiers list...
            if match:
                role = 'patient'
                type_ = patient_type

        for provider_type in self.provider_types:
            match = re.search(provider_type, endpoint_name)
            if match:
                role = 'provider'
                type_ = provider_type

        # return {'role': role}
        return role, type_
    #
    # def get_type(self, endpoint_name):
    #
    #     type_ = "Unknown"
    #
    #     for provider_type in self.provider_types:
    #         match = re.search(provider_type.upper(), endpoint_name.upper())
    #         if match:
    #             type_ = match[0]
    #
    #     # if not in self.provider_types, it's an unknown type
    #     return {"type": type_}


class EndpointSorter:

    def __init__(self):
        pass


class Directives:

    def __init__(self, input_queue):
        self.queue = input_queue

    @staticmethod
    def add_directives():
        pass