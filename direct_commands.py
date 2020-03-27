import time
from string import Template


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


