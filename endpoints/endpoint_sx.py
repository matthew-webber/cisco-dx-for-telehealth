from endpoints.endpoint_shared import Endpoint
from dicts import *
import requests


class SX(Endpoint):
    #
    def __init__(self, ip, password='admin456'):
        super().__init__(ip=ip, password=password)
        self.session = requests.session()
        self.login()

    def disconnect_all_call(self):
        xml = xml_dict['commands']['disconnect_all']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers= headers)

    def reboot(self):
        xml = xml_dict['SX']['commands']['reboot']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)