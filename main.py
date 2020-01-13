from endpoint_dx import DX
from endpoint_sx import SX
from endpoint_shared import Endpoint
from dicts import xml_dict, url_dict

# todo setup a 'timeout' capability otherwise this thing will hang if the object isn't on the network

myDX = DX('128.23.200.152', '40100@cucm.musc.edu', password='a;sldkfj')
davidsDX = DX('128.23.200.189')
richardsDX = DX('128.23.200.158')
ca300 = SX('10.33.48.163', 'musc.ttt.ca30@musc.edu')
michael_cart = Endpoint('128.23.200.77', 'TTTVX@musc.edu')

# ca300.call(michael_cart.call_string)
# time.sleep(1)


# r = requests.session()
# r2 = requests.session()
#
# _ = r.post(f'http://{device1_ip}/web/signin/open', device1_data)
# _ = r2.post(f'http://{device2_ip}/web/signin/open', device2_data)

# for i in [richardsDX, davidsDX, ca300]:
#     i.play_ringtone('a')