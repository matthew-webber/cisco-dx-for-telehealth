from endpoints.endpoint_shared import Endpoint
from dicts import *
import xml.etree.ElementTree as ET
from direct_commands import *

# DX cluster class

class DXCluster:

    _clusters = []

    def __init__(self, dx: object, name: str):
        self.name = name
        self.dxs = [dx]
        self._clusters.append(self)

    def add_dx(self, dx):
        self.dxs.append(dx)


class DX(Endpoint):

    def __init__(self, session, status_xml, ip):
        super().__init__(session=session, status_xml=status_xml, ip=ip)

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

    def execute_directives(self):
        for directive in self.directives.values():
            directive(self)

    # todo add UPDATE FAVORITES method + move to shared object???
    def collect_favorites(self, endpoints, favorite_types):
        for endpoint in endpoints:
            if endpoint.type in favorite_types:
                self._favorites.append(endpoint)

    def reboot(self):
        xml = xml_dict['DX']['commands']['reboot']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def disconnect_call(self):
        xml = xml_dict['commands']['disconnect']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers= headers)

    def display_alert(self, text, title='', duration=3):
        xml = xml_dict['DX']['commands']['alert']
        xml = xml.replace('$1', str(duration))
        xml = xml.replace('$2', text)
        xml = xml.replace('$3', title)
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def display_covid_alert(self, path):
        self.display_alert(get_COVID_alert(self, alert_txt_file=path), "Information", 0)
        print(f'{self.name} - alert displayed!')

    def display_prompt(self, text, options: list, feedbackid='', title=''):
        xml = xml_dict['userinterface']['prompt']
        xml = xml.replace('$text', text)
        xml = xml.replace('$feedbackid', feedbackid)
        xml = xml.replace('$title', title)

        # maximum 5 options -- fill list if fewer than 5
        while not len(options) >= 5:
            options.append('')

        for i, option in enumerate(options):
            xml = xml.replace(f'$option{i+1}', option)

        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)


if __name__ == "__main__":
    pass