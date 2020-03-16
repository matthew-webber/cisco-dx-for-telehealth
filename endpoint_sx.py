from endpoint_shared import Endpoint
from dicts import *


class SX(Endpoint):
    #
    # def __init__(self):
    #     super.__init__()

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