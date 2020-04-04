import re
from operator import methodcaller
from pathlib import Path


class TeleportProvisioner:

    def __init__(self):
        self.role_module = RoleDefiner(
                                patient_types=dict(
                                    cart='CART',
                                    patient='DX-PATIENT'
                                ),
                                 provider_types=dict(
                                    nurse_station='-NS-',
                                    pod='-POD-',
                                    triage='TRIAGE',
                                    testing='PROVIDER-TESTING',
                                )
                            )

        # the alert method for Covid Teleports expects a text file to render information about the
        # endpoint.  To keep the program from failing, there must be a file named "DX_alert_msg.txt" in
        # the parent directory of this project.

        alert_txt_file = f'{Path().absolute()}/DX_alert_msg.txt'

        self.provider_directives = dict(
            delete_contacts=methodcaller('delete_all_contacts'),
            clear_recents=methodcaller('delete_callhistory'),
            display_alert=methodcaller('display_covid_alert', path=alert_txt_file),
            add_favorites=methodcaller('add_all_favorites')
        )

    def typify(self, endpoints):
        """Updates roles and types for endpoints"""
        for endpoint in endpoints:
            types_to_add = self.role_module.get_type(endpoint)

            endpoint.type = types_to_add['type_']
            endpoint.role = types_to_add['role']

    def add_directives(self, endpoint):

        if endpoint.role == "Provider":
            endpoint.directives = self.provider_directives
        else:
            pass  # currently, providers are the only endpoints that get directives

    def define_favorites(self, endpoint):

        favorites_types = None

        provider_types = list(self.role_module.types.get('provider').keys())
        endpoint_type = endpoint.type

        if endpoint_type in provider_types:  # currently providers get ALL endpoints as favorites
            favorites_types = \
                list(self.role_module.types.get('provider').keys()) + \
                list(self.role_module.types.get('patient').keys())

        return favorites_types


class RoleDefiner:

    def __init__(self, patient_types, provider_types, add_flag=True):
        self._types = dict(patient=patient_types, provider=provider_types)
        self.patient_types = patient_types
        self.provider_types = provider_types
        self.flag = add_flag

    @property
    def types(self):
        return self._types

    def get_type(self, endpoint):

        type_ = "Unknown"
        role_ = "Unknown"

        # todo DRY this thing out... one return statement plz

        # for prov_types, pt_types in self._types.items():

        for prov_type, prov_identifier in self._types['provider'].items():
            match = re.search(prov_identifier.upper(), endpoint.name.upper())
            if match:
                return dict(type_=prov_type, role="Provider")
                # type_ = match[0]
                # role_ = "Provider"
                # retu

        for pt_type, pt_identifier in self._types['patient'].items():
            match = re.search(pt_identifier.upper(), endpoint.name.upper())
            if match:
                return dict(type_=pt_type, role="Patient")

        return dict(type_=type_, role=role_)

    # def get_role(self, endpoint):
    #
    #     # if name not like any identifiers, it must be a provider
    #     role = 'provider'
    #
    #     for identifier in self.patient_identifiers:
    #         match = re.search(identifier, endpoint.name)  # it's in the patient_identifiers list...
    #         if match:
    #             role = 'patient'
    #
    #     # return {'role': role}
    #     return role

if __name__ == '__main__':

    class iEndpoint:

        def __init__(self, name, type, role, favorites):
            self.name = name
            self.type = type
            self.role = role
            self.favorites = favorites

    iendpoint = iEndpoint(type=None, role=None, name="DX-NS-01", favorites=None)
    provisioner = TeleportProvisioner()

    provisioner.typify([iendpoint])
    print(provisioner.define_favorites(iendpoint), f'for {iendpoint.type}')