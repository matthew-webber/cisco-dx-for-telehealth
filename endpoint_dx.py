import requests
import time
from endpoint_shared import Endpoint
from dicts import *


class DX(Endpoint):

    def disconnect_call(self):
        xml = xml_dict['commands']['disconnect']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers= headers)

    def display_alert(self, text, title='', duration=3):
        xml = xml_dict['userinterface']['alert']
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
