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

def display_all_alerts(DXs):
    for DX_ in DXs:
        DX_.display_alert(get_COVID_alert(DX_), 'Information', 0)


def clear_all_alerts(DXs):
    for DX_ in DXs:
        DX_.display_alert('')

def point_all_to_CUCM(DXs):
    for DX_ in DXs:
        DX_.set_external_manager_address('128.23.1.36')
        DX_.set_provisioning_mode('CUCM')
        DX_.reboot()

# ca300 = SX('10.33.48.163')
# michael_cart = SX('128.23.200.77')
# cth750 = SX('128.23.27.109')

# myDX = DX('10.27.200.140', password='')
# davidsDX = DX('128.23.200.189')
# richardsDX = DX('128.23.200.158')
# wendysDX = DX('128.23.200.16')

# DX_TELEPOD_01 = DX('10.27.57.109')
# DX_7E_01 = DX('10.31.110.119')
# DX_ART_6WEST_01 = DX('10.33.80.108')
# DX_MSICU_01 = DX('10.33.15.156')
# DX_MICU_01 = DX('10.33.49.50')
# DX_TRIAGE_01 = DX('10.33.81.103')
# DX_TRIAGE_02 = DX('128.23.2.27')
# DX_TRIAGE_03 = DX('128.23.200.229')
# DX_TRIAGE_04 = DX('128.23.200.195')

# DXs = [DX_TRIAGE_01, DX_TRIAGE_02, DX_TRIAGE_03, DX_TRIAGE_04]
# DXs = [Pod1DX, MICU, DX_7E_01, DX_ART_01, DX_MSICU_01]
# DXs = [DX_TRIAGE_01, DX_TRIAGE_02, DX_TRIAGE_03, DX_TRIAGE_04]

