from endpoint_shared import Endpoint
from dicts import *


class SX(Endpoint):

    def disconnect_all_call(self):
        xml = xml_dict['commands']['disconnect_all']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers= headers)