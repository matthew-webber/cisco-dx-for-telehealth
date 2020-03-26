from endpoints.endpoint_dx import DX
from endpoints.endpoint_sx import SX
from direct_commands import *

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

# ca300 = SX(ip='10.33.48.163', password='admin456')
# michael_cart = SX('128.23.200.77')
# cth750 = SX('128.23.27.109')
# ttt750 = SX('10.33.108.74')

myDX = DX('10.27.200.140', password='')

# davidsDX = DX('128.23.200.189')
# richardsDX = DX('128.23.200.158')
# wendysDX = DX('128.23.200.16')


# # # update group 1
# DX_TELEPOD_01 = DX('10.33.114.35')
# #
# # # update group 2
# DX_7E = DX('10.33.110.119')
# DX_ART_6WEST_01 = DX('10.33.80.108')
# DX_MSICU_01 = DX('10.33.15.156')
# DX_MICU_01 = DX('10.33.49.50')
# DX_MAIN_10W = DX('10.33.72.81')
# #
# # # update group 3
# DX_STATION_01 = DX('10.33.46.85')
# DX_STATION_02 = DX('10.33.112.74')
#
# # DX_MAIN_6W = DX('128.23.200.63')  # offline
#
# # # favorites 1
# CART_02 = DX('10.33.9.189')
# CART_04 = DX('10.33.111.118')
# CART_11 = DX('10.33.102.191')
# CART_12 = DX('10.33.1.119')
# CART_13 = DX('10.33.126.42')
# CART_14 = DX('10.33.45.45')
# CART_19 = DX('10.33.117.19')
# CART_20 = DX('10.33.87.102')
# # favorites 2
# patientDX1 = DX('10.33.59.0')
# patientDX2 = DX('10.33.39.69')
# patientDX3 = DX('10.33.69.192')
# patientDX4 = DX('10.33.20.6')
# patientDX5 = DX('10.33.81.103')
# patientDX6 = DX('10.33.100.145')
# patientDX7 = DX('10.33.120.174')
# patientDX8 = DX('10.33.18.168')
# patientDX9 = DX('10.33.1.143')
# patientDX10 = DX('10.33.27.113')
# patientDX11 = DX('10.33.31.227')
# patientDX12 = DX('10.33.45.139')

# update_group_01 = [DX_TELEPOD_01]
# update_group_02 = [DX_ART_6WEST_01, DX_MSICU_01, DX_MICU_01, DX_MAIN_10W]
# # update_group_02 = [DX_7E, DX_ART_6WEST_01, DX_MSICU_01, DX_MICU_01, DX_MAIN_10W]
# update_group_03 = [DX_STATION_01, DX_STATION_02]

# favorites = [CART_02, CART_11, CART_12, CART_13, CART_14, CART_19, CART_20]
# favorites_telepod = [CART_02, CART_11, CART_12, CART_13, CART_14, CART_19, CART_20, patientDX1, patientDX2, patientDX3, patientDX4, patientDX5, patientDX6, patientDX7, patientDX8, patientDX9, patientDX10, patientDX11, patientDX12]

# DX_TRIAGE_01 = DX('10.33.81.103')
# DX_TRIAGE_02 = DX('128.23.2.27')
# DX_TRIAGE_03 = DX('128.23.200.229')
# DX_TRIAGE_04 = DX('128.23.200.195')

musc_vidyo = '112453@vidyo.musc.edu'
pspn_vidyo = '102007@vidyo.pspnsc.org'

#todo
# *******
# MAKE OBJECT METHODS!!!!
# *******

def delete_all_contacts(dx_):
    contacts_list = dx_.phonebook_search("this")
    for contact in contacts_list:
        dx_.delete_contact(contact.find('ContactId').text)


def add_all_favorites(dx_, favorites):
    for favorite in favorites:
        dx_.add_contact(favorite.name, favorite.call_string)

# mylist = myDX.phonebook_search('PATIENT')
# when the list of contacts get's passed back....
    # for elem in mylist:
    #     myDX.delete_contact(elem.find('ContactId').text)