import requests
import time
from endpoint_shared import Endpoint
from dicts import *
from string import Template


class DX(Endpoint):

    # def __init__(self):
    #     self.call_string = ''
    #     self.name = ''
    #     self.ip = ''

    def get_call_string(self):
        URL_suffix = xml_dict['status']['call_string']
        headers = xml_dict['headers']
        url = url_dict['get_xml'].replace('{{}}', self.ip) + URL_suffix
        response = self.session.get(url, headers=headers)
        return response

    def get_device_name(self):
        xml = xml_dict['Status']['UserInterface']['ContactInfo']['Name']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        response = self.session.post(url, xml, headers=headers)
        return response

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
        print(xml)
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

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
    from endpoint_dx import DX
    davidsDX = DX('128.23.200.189')

    call_string = davidsDX.get_call_string()


