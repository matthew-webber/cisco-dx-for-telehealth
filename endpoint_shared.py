import requests
from dicts import *
import time


class Endpoint:

    def __init__(self, ip, call_string="", user='admin', password='admin456'):
        self.ip = ip
        self.call_string = call_string
        self.user = user
        self.password = password
        self.session = requests.session()
        self.login()

    def login(self):
        self.session.post(url_dict['login'].replace('{{}}',self.ip), data=dict(username=self.user, password=self.password))

    def play_ringtone(self, tone_key):
        xml = xml_dict['commands']['play_ringtone'].replace('{{}}', xml_dict['ringtones'][tone_key])
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def set_ringtone_volume(self, volume):
        xml = xml_dict['configuration']['ring_volume'].replace('{{}}', str(volume))
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def ignore_call(self):
        xml = xml_dict['commands']['disconnect']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers= headers)

    def reboot(self):
        xml = xml_dict['commands']['reboot']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def accept_call(self):
        xml = xml_dict['commands']['accept']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers= headers)

    def reject_call(self):
        xml = xml_dict['commands']['reject']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def call(self, call_string):
        xml = xml_dict['commands']['call'].replace('{{}}', call_string)
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers= headers)


# todo setup a 'timeout' capability otherwise this thing will hang if the object isn't on the network

# myDX = Endpoint('128.23.200.152', '40100@cucm.musc.edu', password='a;sldkfj')
ca300 = Endpoint('10.33.48.163', 'musc.ttt.ca30@musc.edu')
# michael_cart = Endpoint('128.23.200.77', 'TTTVX@musc.edu')

# ca300.call(michael_cart.call_string)
# time.sleep(1)


# r = requests.session()
# r2 = requests.session()
#
# _ = r.post(f'http://{device1_ip}/web/signin/open', device1_data)
# _ = r2.post(f'http://{device2_ip}/web/signin/open', device2_data)