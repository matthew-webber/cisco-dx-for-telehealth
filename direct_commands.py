import time
from string import Template

#todo
# setup a 'timeout' capability otherwise this thing will hang if the object isn't on the network
# add a DX factory
# add a way to dynamically get the name of the DX using APIs
# close the session To close a session after use, issue a POST to
# http://<ip-address>/xmlapi/session/end with the provided
# cookie.

# todo -- need to find a way to get value from XML returned by using GET
#todo -- SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# this happens when calling "add contact" with 007 as the argument for "number"



# todo ******make the below object methods******


def get_COVID_alert(DX_obj, alert_txt_file="/Users/webber/PycharmProjects/cisco_API/DX_alert_msg.txt"):
    with open(alert_txt_file, "r") as f:
        dx_alert = f.read()

    alert = Template(dx_alert).substitute(name=DX_obj.name,
                                      ip=DX_obj.ip,
                                      call_string=DX_obj.call_string
                                      )

    return alert

def echo_bomb(target, attacker):
    attacker.call(target.call_string)
    time.sleep(6)
    attacker.call(target.call_string)
    time.sleep(3)
    target.accept_call()
    time.sleep(3)
    target.delete_callhistory()


musc_vidyo = '112453@vidyo.musc.edu'
pspn_vidyo = '102007@vidyo.pspnsc.org'

# r = requests.session()
# r2 = requests.session()
#
# _ = r.post(f'http://{device1_ip}/web/signin/open', device1_data)cth
# _ = r2.post(f'http://{device2_ip}/web/signin/open', device2_data)

# for i in [richardsDX, davidsDX, ca300]:
#     i.play_ringtone('a')

def sound_bomb(targets, sound, sleep=0, loops=10):

    if not isinstance(targets, list):
        targets = [targets]

    for target in targets:
        target.set_volume(100)
        for i in range(loops):
            target.play_sound(sound)
            time.sleep(sleep)

        target.stop_sound()
        target.set_volume(50)

class DummyDX:

    def __init__(self, ip, name, call_string):
        self.ip = ip
        self.name = name
        self.call_string = call_string


def clear_all_alerts(DXs):
    for DX_ in DXs:
        DX_.display_alert('')


def point_all_to_CUCM(DXs):
    for DX_ in DXs:
        DX_.set_external_manager_address('128.23.1.36')
        DX_.set_provisioning_mode('CUCM')
        DX_.reboot()

# def repeat_bomb():
#     # vol_dir = 'up'
#     # volume = 0
#     #
#     # while True:
#     #
#     #     if vol_dir == 'up':
#     #         volume += 50
#     #     else:
#     #         volume -= 50
#     richardsDX.play_sound('Ringing')
#     davidsDX.play_sound('Ringing')
#
#         #
#         # if volume == 100:
#         #     vol_dir = 'down'
#         # elif volume == 0:
#         #     vol_dir = 'up'


