import requests
from dicts import *
import time


class Endpoint:

    def __init__(self, ip='0.0.0.0', call_string="", user='admin', password='admin456', testing=False):
        self.ip = ip
        self.call_string = call_string
        self.user = user
        self.password = password
        self.soundbank = SoundBank()
        self.ringtone = self.soundbank.get_ringtone()
        if not testing:
            self.session = requests.session()
            self.login()

    def login(self):
        self.session.post(url_dict['login'].replace('{{}}',self.ip), data=dict(username=self.user, password=self.password))

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

    def ignore_call(self):
        xml = xml_dict['commands']['disconnect']
        headers = xml_dict['headers']
        url = url_dict['post_xml'].replace('{{}}', self.ip)
        self.session.post(url, xml, headers= headers)

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

if __name__ == '__main__':
    thisthat = SoundBank()
    foo = Endpoint(testing=True)