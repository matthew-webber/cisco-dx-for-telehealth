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

# ca300 = SX(ip='10.33.48.163', password='admin456')
# michael_cart = SX('128.23.200.77')
# cth750 = SX('128.23.27.109')
# ttt750 = SX('10.33.108.74')

myDX = DX('10.27.200.140', password='')

# davidsDX = DX('128.23.200.189')
# richardsDX = DX('128.23.200.158')
# wendysDX = DX('128.23.200.16')


# # update group 1
DX_TELEPOD_01 = DX('10.33.114.35')

# # update group 2

DX_7E = DX('10.33.110.119')
DX_ART_5E = DX('10.33.112.74')
DX_ART_5W = DX('10.33.69.192')  # ex DX Patient 3
DX_ART_6W_01 = DX('10.33.80.108')
DX_MAIN_10W = DX('10.33.72.81')
DX_MAIN_6E = DX('10.33.58.244')
DX_MAIN_6W = DX('10.33.20.6')  # ex DX Patient 4
DX_MICU_01 = DX('10.33.49.50')
DX_MSICU_01 = DX('10.33.15.156')

# DX_XX_03 = DX('10.33.18.168')  # ex DX Patient 8

# # update group 3
DX_STATION_01 = DX('10.33.46.85')

update_group_01 = [DX_TELEPOD_01]
update_group_02 = [DX_7E, DX_ART_5E, DX_ART_5W, DX_ART_6W_01, DX_MAIN_10W, DX_MAIN_6E, DX_MAIN_6W, DX_MICU_01, DX_MSICU_01]

# update_group_03 = [DX_STATION_01, DX_STATION_02]

# all_update_groups = [update_group_01, update_group_02, update_group_03]

# # favorites 1
# CART_02 = DummyDX('10.33.9.189', 'MONA-VPO-CART-02', '11002@cucm.musc.edu')  # offline 12:34 3/26
CART_02 = DX('10.33.9.189')
CART_03 = DX('10.33.10.144')
CART_04 = DummyDX('10.33.111.118', 'MONA-VPO-CART-04', '11002@cucm.musc.edu')
CART_07 = DX('10.33.107.22')
CART_11 = DX('10.33.102.191')
CART_12 = DX('10.33.1.119')
CART_13 = DX('10.33.126.42')
CART_14 = DX('10.33.45.45')
CART_19 = DX('10.33.117.19')
CART_20 = DX('10.33.87.102')
#
# # favorites 2
patientDX1 = DX('10.33.59.0')
patientDX2 = DX('10.33.39.69')
patientDX5 = DX('10.33.81.103')
patientDX6 = DX('10.33.100.145')
patientDX7 = DX('10.33.120.174')
patientDX9 = DX('10.33.1.143')
# patientDX10 = DX('10.33.27.113')
# patientDX11 = DX('10.33.31.227')
patientDX12 = DX('10.33.45.139')
#
carts_only = [CART_02, CART_03, CART_04, CART_07, CART_11, CART_12, CART_13, CART_14, CART_19, CART_20]
all_pt_endpoints = carts_only + [patientDX1, patientDX2, patientDX5, patientDX6, patientDX7, patientDX9, patientDX12]
patient_DXs = [patientDX1, patientDX2, patientDX5, patientDX6, patientDX7, patientDX9, patientDX12]

# DX_TRIAGE_01 = DX('10.33.81.103')
# DX_TRIAGE_02 = DX('128.23.2.27')
# DX_TRIAGE_03 = DX('128.23.200.229')
# DX_TRIAGE_04 = DX('128.23.200.195')

musc_vidyo = '112453@vidyo.musc.edu'
pspn_vidyo = '102007@vidyo.pspnsc.org'

# mylist = myDX.phonebook_search('PATIENT')
# when the list of contacts get's passed back....
    # for elem in mylist:
    #     myDX.delete_contact(elem.find('ContactId').text)

DX_TELEPOD_01.delete_all_contacts()
DX_TELEPOD_01.add_all_favorites(favorites=all_pt_endpoints)
DX_TELEPOD_01.display_covid_alert(path='/Users/webber/PycharmProjects/cisco_API/DX_alert_msg.txt')

for dx_ in update_group_02:
    dx_.delete_all_contacts()
    dx_.add_all_favorites(favorites=carts_only)
    dx_.display_covid_alert(path='/Users/webber/PycharmProjects/cisco_API/DX_alert_msg.txt')


