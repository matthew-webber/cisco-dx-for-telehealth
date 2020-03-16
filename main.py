from endpoint_dx import DX
from endpoint_sx import SX
from direct_commands import *

#todo
# setup a 'timeout' capability otherwise this thing will hang if the object isn't on the network
# add a DX factory
# add a way to dynamically get the name of the DX using APIs
# close the session To close a session after use, issue a POST to
# http://<ip-address>/xmlapi/session/end with the provided
# cookie.

# todo -- need to find a way to get value from XML returned by using GET

myDX = DX('10.27.200.140', '40100@cucm.musc.edu', password='')
davidsDX = DX('128.23.200.189')
# richardsDX = DX('128.23.200.158')
# ca300 = SX('10.33.48.163', 'musc.ttt.ca30@musc.edu')
# michael_cart = SX('128.23.200.77', 'TTTVX@musc.edu')
# wendysDX = DX('128.23.200.16')
# cth750 = SX('128.23.27.109', 'CenterForTelehealthCA750@musc.edu')
# Pod1DX = DX('10.27.57.109', call_string='40163@cucm.musc.edu', name='MUSC POD 01')
# MICU = DX('10.33.49.50', call_string='40161@cucm.musc.edu', name='MICU')
# DX_7E_01 = DX('10.31.110.119', call_string='40159@cucm.musc.edu', name='DX 7-EAST-01')
# DX_ART_01 = DX('10.33.80.108', call_string='40169@cucm.musc.edu', name='DX ART 01')
# DX_MSICU_01 = DX('10.33.15.156', call_string='40160@cucm.musc.edu', name='DX-MSICU-01')

#
# DXs = [Pod1DX, MICU, DX_7E_01, DX_ART_01, DX_MSICU_01]
#
# for DX_ in DXs:
#     DX_.display_alert(get_COVID_alert(DX_), 'Information', 0)

