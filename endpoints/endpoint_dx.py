from endpoints.endpoint_shared import Endpoint
from dicts import *
import xml.etree.ElementTree as ET
from direct_commands import *
from ixml import *


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

    def __init__(self, session, status_xml):
        super().__init__(session, status_xml)
        self.xml_lib = dict()
        self.xml_lib['status'] = status_xml
        self.name = self.get_name_2()[0].text
        self.call_string = self.get_call_string_2()[0].text
        # self.set_call_string(self.get_call_string())
        # print(f'my call string is {self.call_string}')
        # self.set_device_name(self.get_device_name())
        # print(f'my name is {self.name}')

    def get_name_2(self):
        return get_nested_xml(self.xml_lib.get('status'), "ContactInfo/Name")

    def get_call_string_2(self):
        return get_nested_xml(self.xml_lib.get('status'), 'Registration/URI')


    def get_device_name(self):
        URL_suffix = xml_dict['status']['device_name']
        headers = xml_dict['headers']
        url = url_dict['get_xml'].replace('{{}}', self.ip) + URL_suffix
        response = self.session.get(url, headers=headers)
        # now parse the response -- this needs to go elsewhere
        root = ET.fromstring(response.text)
        return root[0][0][0].text

    def get_call_string(self):
        URL_suffix = xml_dict['status']['call_string']
        headers = xml_dict['headers']
        url = url_dict['get_xml'].replace('{{}}', self.ip) + URL_suffix
        response = self.session.get(url, headers=headers)
        while response.status_code == 401:
            response = self.session.get(url, headers=headers)
        #     SessionTester(session, url, headers) -->
        #     return session
        #       while SessionTester not True: continue, else: input("New pw")
        #       if input == "q!", quit, else session = SessionUpdater(pw)
        # now parse the response -- this needs to go elsewhere
        root = ET.fromstring(response.text)
        return root[0][0][0].text

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

    myDX = DX('10.27.200.140', password='')

    call_string = myDX.get_device_name()