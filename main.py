from endpoints.endpoint_dx import DX
from endpoints.endpoint_sx import SX
from direct_commands import echo_bomb, sound_bomb

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

def provider_refresh(dx_, favorites):
    print(f'Updating {dx_.name}...')
    dx_.delete_all_contacts()
    dx_.delete_callhistory()
    dx_.add_all_favorites(favorites=favorites)
    dx_.display_covid_alert(path=alert_path)


class DummyDX:

    def __init__(self, ip, name, call_string):
        self.ip = ip
        self.name = name
        self.call_string = call_string


def clear_all_alerts(DXs):
    for DX_ in DXs:
        DX_.display_alert('')


def point_all_to_cucm(dx_list):
    for DX_ in dx_list:
        DX_.set_external_manager_address('128.23.1.36')
        DX_.set_provisioning_mode('CUCM')
        DX_.reboot()

# ca300 = SX(ip='10.33.48.163', password='admin456')
# michael_cart = SX('128.23.200.77')
# cth750 = SX('128.23.27.109')
# ttt750 = SX('10.33.108.74')

# davidsDX = DX('128.23.200.189')
# richardsDX = DX('128.23.200.158')
# wendysDX = DX('128.23.200.16')


# myDX = DX('10.27.200.140', password='')

print('\nLogging into telepod...\n')
DX_TELEPOD_01 = DX('10.33.114.35')

# # update group 2
print('\nLogging into nurse stations...\n')
DX_NS_01 = DX('10.33.110.119')
DX_NS_02 = DummyDX('10.33.112.74', 'DX-NS-02', '40178@cucm.musc.edu')
DX_NS_03 = DX('10.33.69.192')
DX_NS_04 = DX('10.33.80.108')
DX_NS_05 = DX('10.33.72.81')
DX_NS_06 = DX('10.33.58.244')
DX_NS_07 = DX('10.33.49.50')
DX_NS_08 = DX('10.33.72.103')
DX_NS_09 = DX('10.33.20.6')  # ex DX Patient 4
DX_NS_10 = DX('10.33.0.106')
DX_NS_11 = DX('10.33.111.4')
DX_NS_12 = DX('10.33.15.156')
DX_NS_13 = DX('10.33.126.200')
DX_NS_14 = DX('10.33.121.109')
DX_NS_15 = DX('128.23.200.158')
DX_NS_16 = DX('128.23.200.189')
DX_5C_NS_01 = DX('10.33.46.85')
DX_5C_NS_02 = DX('10.33.121.109')

DX_TRIAGE_TENT = DX('10.33.48.18')

# DX_NS_02 = DX('10.33.112.74')
# DX_NS_03 = DummyDX('10.33.69.192', 'DX-NS-03', '40166@cucm.musc.edu')
# DX_NS_06 = DummyDX('10.33.58.244', 'DX-NS-06', '40193@cucm.musc.edu')
# DX_5C_NS_02 = DummyDX('10.33.121.109', 'DX-5C-NS-02', '40203@cucm.musc.edu')

NS_refresh_group = [DX_NS_01,
                    # DX_NS_02,
                    DX_NS_03,
                    DX_NS_04,
                    DX_NS_05,
                    DX_NS_06,
                    DX_NS_07,
                    DX_NS_08,
                    DX_NS_09,
                    DX_NS_10,
                    DX_NS_11,
                    DX_NS_12,
                    DX_NS_13,
                    DX_NS_14,
                    DX_NS_15,
                    DX_NS_16,
                    DX_5C_NS_01,
                    # DX_5C_NS_02,
                    ]

NS_contact_group = [DX_NS_01,
                    DX_NS_02,
                    DX_NS_03,
                    DX_NS_04,
                    DX_NS_05,
                    DX_NS_06,
                    DX_NS_07,
                    DX_NS_08,
                    DX_NS_09,
                    DX_NS_10,
                    DX_NS_11,
                    DX_NS_12,
                    DX_NS_13,
                    DX_NS_14,
                    DX_NS_15,
                    DX_NS_16,
                    DX_5C_NS_01,
                    DX_5C_NS_02,
                    ]

# # favorites 1
print('\nLogging into carts...\n')
CART_01 = DX('10.33.26.21')
CART_02 = DX('10.33.9.189')
CART_03 = DX('10.33.10.144')
CART_04 = DX('10.33.111.118')
CART_05 = DX('10.33.58.239')
CART_06 = DX('10.33.102.141')
CART_07 = DX('10.33.107.22')
CART_08 = DX('10.33.72.38')
CART_09 = DX('10.33.84.116')
CART_10 = DX('10.33.107.207')
CART_11 = DX('10.33.102.191')
CART_12 = DX('10.33.1.119')
CART_13 = DX('10.33.126.42')
CART_14 = DX('10.33.45.45')
CART_15 = DX('10.33.76.80')
CART_16 = DX('10.33.2.188')
# CART_17 = DX('10.33.62.71')
CART_18 = DX('10.33.31.218', password='')  # todo change pw to admin456
CART_19 = DX('10.33.117.19')
CART_20 = DX('10.33.87.102')

# CART_01 = DummyDX('10.33.26.21', 'MONA-VPO-CART-01', '11001@cucm.musc.edu')
# CART_02 = DummyDX('10.33.9.189', 'MONA-VPO-CART-02', '11002@cucm.musc.edu')  # offline 12:34 3/26
# CART_03 = DummyDX('10.33.10.144', 'MONA-VPO-CART-03', '11003@cucm.musc.edu')
# CART_04 = DummyDX('10.33.111.118', 'MONA-VPO-CART-04', '11004@cucm.musc.edu')
# CART_07 = DummyDX('10.33.107.22', 'MONA-VPO-CART-07', '11007@cucm.musc.edu')
# CART_14 = DummyDX('10.33.45.45', 'MONA-VPO-CART-14', '11014@cucm.musc.edu')
CART_17 = DummyDX('10.33.62.71', 'MONA-VPO-CART-17', '11017@cucm.musc.edu')

carts_only = [
    CART_01,
    CART_02,
    CART_03,
    CART_04,
    CART_05,
    CART_06,
    CART_07,
    CART_08,
    CART_09,
    CART_10,
    CART_11,
    CART_12,
    CART_13,
    CART_14,
    CART_15,
    CART_16,
    CART_17,
    CART_18,
    CART_19,
    CART_20
]

# favorites 2
print('\nLogging into patient DXs...\n')
patientDX1 = DX('10.33.59.0')
patientDX2 = DX('10.33.39.69')
patientDX3 = DX('10.33.18.168')
patientDX4 = DX('10.33.1.143')
patientDX5 = DX('10.33.81.103')
patientDX6 = DX('10.33.31.227')
patientDX7 = DX('10.33.120.174')
patientDX8 = DX('10.33.27.113')
patientDX10 = DummyDX('10.33.100.145', 'DX-PATIENT-10', '40162@cucm.musc.edu')  # registered but can't hit webUI
patientDX12 = DX('10.33.45.139')

patient_DXs = [
    patientDX1,
    patientDX2,
    patientDX3,
    patientDX4,
    patientDX5,
    patientDX6,
    patientDX7,
    patientDX8,
    patientDX10,
    patientDX12
]

all_pt_endpoints = carts_only + patient_DXs

alert_path = '/Users/matt/PycharmProjects/dx_sx_api/DX_alert_msg.txt'  # home iMac

# print('\nUpdating telepod...\n')
# provider_refresh(DX_TELEPOD_01, favorites=all_pt_endpoints + NS_contact_group)
#
# print('\nUpdating nurse stations...\n')
# for dx_ in NS_refresh_group:
#     provider_refresh(dx_, favorites=all_pt_endpoints + NS_contact_group)
