from dicts import *
import xml.etree.ElementTree as ET
import requests
from testing.login import SessionTester


class Endpoint:

    def __init__(self, ip='0.0.0.0', name="No name provided", call_string="", user='admin', password='admin456',
                 testing=False):
        self.ip = ip
        self.login_url =  url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.call_string = call_string
        self.user = user
        self.password = password
        self.soundbank = SoundBank()
        self.ringtone = self.soundbank.get_ringtone()
        self.name = name
        if not testing:
            self.session = requests.session()
            self.login()

    # def __repr__(self):
    #     if self.call_string: return self.call_string
    #     else: pass

    def add_contact(self, name, number, protocol='Auto', call_rate='0', call_type='Video', tag='Favorite',
                    device='Video'):
        xml = xml_dict['commands']['contact_add']
        xml = xml.replace('$name', str(name))
        xml = xml.replace('$number', str(number))
        xml = xml.replace('$protocol', str(protocol))
        xml = xml.replace('$call_rate', str(call_rate))
        xml = xml.replace('$call_type', str(call_type))
        xml = xml.replace('$device', str(device))
        xml = xml.replace('$tag', str(tag))
        headers = xml_dict['headers']
        self.session.post(url, xml, headers=headers)

    def delete_contact(self, contact_id):
        xml = xml_dict['commands']['contact_delete']
        xml = xml.replace('$contact_id', str(contact_id))
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def phonebook_search(self, search_str, contact_type='Any', limit='100'):
        xml = xml_dict['commands']['phonebook_search']
        xml = xml.replace('$search_str', str(search_str))
        xml = xml.replace('$contact_type', str(contact_type))
        xml = xml.replace('$limit', str(limit))
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        response = self.session.post(url, xml, headers=headers)
        # parse xml move this later
        root = ET.fromstring(response.text)
        contacts_list = root[0].findall('Contact')
        return contacts_list

    def set_call_string(self, value):
        self.call_string = value

    def set_device_name(self, value):
        self.name = value

    def set_name(self, value):
        self.name = value

    def login(self):
        print(f'Trying {self.ip}...')
        self.session.post(url_dict['login'].replace('{{}}', self.ip),
                          data=dict(username=self.user, password=self.password))
        # check if login was successful
        test = SessionTester(self.session, self.test_url)

        print(f'Logged in to {self.ip}!')

    def play_sound(self, sound):
        xml = xml_dict['commands']['play_sound'].replace('{{}}', sound)
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def set_volume(self, level):
        xml = xml_dict['commands']['set_volume'].replace('{{}}', str(level))
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def stop_sound(self):
        xml = xml_dict['commands']['stop_sound']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def play_ringtone(self):
        xml = xml_dict['commands']['play_ringtone'].replace('{{}}', self.ringtone)
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def set_ringtone_volume(self, volume):
        xml = xml_dict['configuration']['ring_volume'].replace('{{}}', str(volume))
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def set_external_manager_address(self, address):
        xml = xml_dict['configuration']['external_manager'].replace('{{}}', str(address))
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def set_provisioning_mode(self, mode):
        xml = xml_dict['configuration']['provisioning_mode'].replace('{{}}', str(mode))
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def end_call(self):
        xml = xml_dict['commands']['disconnect']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def accept_call(self):
        xml = xml_dict['commands']['accept']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def reject_call(self):
        xml = xml_dict['commands']['reject']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)

    def call(self, call_string):
        xml = xml_dict['commands']['call'].replace('{{}}', call_string)
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers=headers)


class SoundBank:

    def __init__(self):
        self._ringtones = self._get_ringtones()
        self._sounds = self._get_sounds()
        # self._tone = self.get_ringtone()
        # self._sound = self.get_sound(sound)

    @property
    def ringtones(self):
        print(f'Printing ringtones...')
        return self._ringtones

    @property
    def sounds(self):
        print(f'Printing sounds...')
        return self._sounds

    def get_random(self):
        pass

    def get_ringtone(self, tone='Sunrise'):
        if isinstance(tone, int):
            return self._ringtones[tone]
        else:
            return self._ringtones[self._ringtones.index(tone)]

    @staticmethod
    def _get_ringtones():
        ringtones = [
            'Sunrise',
            'Mischief',
            'Ripples',
            'Reflections',
            'Vibes',
            'Delight',
            'Evolve',
            'Playful',
            'Ascent',
            'Calculation',
            'Mellow',
            'Ringer',
        ]
        return ringtones

    @staticmethod
    def _get_sounds():
        sounds = [
            'Alert',
            'Bump',
            'Busy',
            'CallDisconnect',
            'CallInitiate',
            'CallWaiting',
            'Dial',
            'KeyInput',
            'KeyInputDelete',
            'KeyTone',
            'Nav',
            'NavBack',
            'Notification',
            'OK',
            'PresentationConnect',
            'Ringing',
            'SignIn',
            'SpecialInfo',
            'TelephoneCall',
            'VideoCall',
            'VolumeAdjust',
            'WakeUp',
        ]
        return sounds

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

    def __init__(self, ip, password="admin456"):
        super().__init__(ip=ip, password=password)
        self.call_string = ''
        self.name = ''
        self.set_call_string(self.get_call_string())
        # print(f'my call string is {self.call_string}')
        self.set_device_name(self.get_device_name())
        # print(f'my name is {self.name}')

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

    myDX = DX('10.27.200.140')

    call_string = myDX.get_device_name()
