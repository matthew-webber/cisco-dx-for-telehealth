from endpoints.endpoint_dx import DX
from endpoints.endpoint_sx import SX
from direct_commands import echo_bomb, sound_bomb, DummyDX

# ca300 = SX(ip='10.33.48.163', password='admin456')
# michael_cart = SX('128.23.200.77')
# cth750 = SX('128.23.27.109')
ttt750 = SX('10.33.108.74')

myDX = DX('10.27.200.140', password='lkjlkj')

# davidsDX = DX('128.23.200.189')
# richardsDX = DX('128.23.200.158')
# wendysDX = DX('128.23.200.16')


# DX stations

# DX_7E = DX('10.33.110.119')
# DX_ART_5E = DX('10.33.112.74')
# DX_ART_5W = DX('10.33.69.192')  # ex DX Patient 3
# DX_ART_6W_01 = DX('10.33.80.108')
# # DX_EXTRA = DX('10.33.27.113')  # not deployed yet
# DX_STATION_01 = DX('10.33.46.85')
# DX_MAIN_10W = DX('10.33.72.81')
# DX_MAIN_6E = DX('10.33.58.244')
# DX_MAIN_6W = DX('10.33.20.6')  # ex DX Patient 4
# DX_MICU_BED = DX('10.33.100.145')
# DX_MICU_STATION_01 = DX('10.33.49.50')
# DX_MSICU_01 = DX('10.33.15.156')
# DX_TELEPOD_01 = DX('10.33.114.35')

# DX_stations = [DX_7E, DX_ART_5E, DX_ART_5W, DX_ART_6W_01, DX_MAIN_10W, DX_MAIN_6E, DX_MAIN_6W, DX_MICU_STATION_01, DX_MSICU_01]

# update_group_03 = [DX_STATION_01, DX_STATION_02]

# all_update_groups = [update_group_01, update_group_02, update_group_03]

# # favorites 1
# # CART_02 = DummyDX('10.33.9.189', 'MONA-VPO-CART-02', '11002@cucm.musc.edu')  # offline 12:34 3/26
# CART_02 = DX('10.33.9.189')
# CART_03 = DX('10.33.10.144')
# CART_04 = DummyDX('10.33.111.118', 'MONA-VPO-CART-04', '11004@cucm.musc.edu')
# # CART_04 = DX('10.33.111.118')
# CART_07 = DX('10.33.107.22')
# CART_09 = DX('10.33.84.116')
# CART_11 = DX('10.33.102.191')
# CART_12 = DX('10.33.1.119')
# CART_13 = DX('10.33.126.42')
# CART_14 = DX('10.33.45.45')
# CART_19 = DX('10.33.117.19')
# CART_20 = DX('10.33.87.102')
#
# # # favorites 2
# patientDX1 = DX('10.33.59.0')
# patientDX2 = DX('10.33.39.69')
# patientDX5 = DX('10.33.81.103')
# patientDX7 = DX('10.33.120.174')
# patientDX8 = DX('10.33.18.168')  # ex DX Patient 10
# patientDX9 = DX('10.33.1.143')
# patientDX11 = DX('10.33.31.227')
# patientDX12 = DX('10.33.45.139')
# #
# carts_list = [CART_02, CART_03, CART_04, CART_07, CART_09, CART_11, CART_12, CART_13, CART_14, CART_19, CART_20]
# patientDX_list = [patientDX1, patientDX2, patientDX5, patientDX7, patientDX8, patientDX9, patientDX11, patientDX12]
# all_pt_endpoints = carts_list + patientDX_list
#
# DX_TELEPOD_01.delete_all_contacts()
# DX_TELEPOD_01.add_all_favorites(favorites=all_pt_endpoints)
# DX_TELEPOD_01.display_covid_alert(path='/Users/webber/PycharmProjects/cisco_API/DX_alert_msg.txt')
#
# DX_STATION_01.delete_all_contacts()
# DX_STATION_01.add_all_favorites(favorites=patientDX_list)
# DX_STATION_01.display_covid_alert(path='/Users/webber/PycharmProjects/cisco_API/DX_alert_msg.txt')
#
# for dx_ in DX_stations:
#     dx_.delete_all_contacts()
#     dx_.add_all_favorites(favorites=carts_list)
#     dx_.display_covid_alert(path='/Users/webber/PycharmProjects/cisco_API/DX_alert_msg.txt')
#
# myDX.delete_all_contacts()
# myDX.add_all_favorites(favorites=DX_stations + all_pt_endpoints)


