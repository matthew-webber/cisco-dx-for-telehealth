def strip_and_lower(string):

    return string.strip().lower()


def master_file_first_line(registrations):

    file_str = ''

    for reg_dict in all_registrations:

        _ = f'{next(iter(reg_dict))}'
        _ = _.strip()

        if file_str == '':
            file_str = _
        else:
            file_str = f'{file_str},{_}'

    return file_str


def read_master_file(file):
    """
    Reads the first line (registration names) of the master file & returns as a list
    :param file: file obj
    :return: list
    """
    with open(file, 'r') as f:
        registrations = f.readline().split(',')
        return registrations


def populate_master_file(file, first_line):

    with open(file, 'w') as f:
        f.write(first_line)


all_registrations = [{'tridentfammed@musc.edu': {'name': 'tridentfammed@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-12 03:54:42', 'hardware': 'PolycomHDX8000HD/3.1.12', 'dial_string': 'tridentfammed@musc.edu', 'ip_address': 'sip:tridentfammed@128.23.51.196:5060;transport=tcp', 'id': '"<urn:uuid:18c9886c-1e5e-57a3-a0d5-c1428e410755>"'}}, {'261 Cannon Park Place': {'name': '261 Cannon Park Place', 'protocol': 'H323', 'reg_time': '2019-09-24 16:56:51', 'hardware': None, 'dial_string': '8437924807@musc.edu', 'ip_address': '128.23.45.115:1720', 'id': None}}, {'record3@musc.edu': {'name': 'record3@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:56:54', 'hardware': 'TANDBERG/80 (S7.10)', 'dial_string': 'record3@musc.edu', 'ip_address': 'sip:record3@128.23.1.245:5060;transport=tcp', 'id': None}}, {'MUSCTTTVX': {'name': 'MUSCTTTVX ', 'protocol': 'H323', 'reg_time': '2019-09-24 16:56:55', 'hardware': None, 'dial_string': '8437920001@musc.edu', 'ip_address': '128.23.200.77:1720', 'id': None}}, {'ocio4thfloorconf@musc.edu': {'name': 'ocio4thfloorconf@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-02 18:33:04', 'hardware': 'TANDBERG/528 (TC7.3.5.a93bdb1)', 'dial_string': 'ocio4thfloorconf@musc.edu', 'ip_address': 'sip:ocio4thfloorconf@128.23.59.122:5061;transport=tls', 'id': '"<urn:uuid:eb75e896-5570-54c3-aedc-deffb5ad4e5a>"'}}, {'muscpedsed@musc.edu': {'name': 'muscpedsed@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-12 20:26:14', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-SX10', 'dial_string': 'muscpedsed@musc.edu', 'ip_address': 'sip:muscpedsed@128.23.63.181:5061;transport=tls', 'id': '"<urn:uuid:d079b0fa-2c8c-589b-809f-0d49f1ea7474>"'}}, {'MUSC Center for Telehealth LC-Patient': {'name': 'MUSC Center for Telehealth LC-Patient', 'protocol': 'H323', 'reg_time': '2019-09-24 16:56:58', 'hardware': None, 'dial_string': '8437920020@musc.edu', 'ip_address': '128.23.26.152:1720', 'id': None}}, {'MUSC Center for Telehealth CA750': {'name': 'MUSC Center for Telehealth CA750', 'protocol': 'H323', 'reg_time': '2019-09-24 16:56:58', 'hardware': None, 'dial_string': '8437920012@musc.edu', 'ip_address': '128.23.27.109:1720', 'id': None}}, {'MUSC Adult ED EX60-2': {'name': 'MUSC Adult ED EX60-2', 'protocol': 'H323', 'reg_time': '2019-08-02 11:22:10', 'hardware': None, 'dial_string': '8437923826@musc.edu', 'ip_address': '128.23.26.64:1720', 'id': None}}, {'MUSC Center for Telehealth CA310': {'name': 'MUSC Center for Telehealth CA310', 'protocol': 'H323', 'reg_time': '2019-10-10 12:53:54', 'hardware': None, 'dial_string': '8437920013@musc.edu', 'ip_address': '128.23.57.129:1720', 'id': None}}, {'MUSC ART Chest Pain Center EX60': {'name': 'MUSC ART Chest Pain Center EX60', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:03', 'hardware': None, 'dial_string': '8438767175@musc.edu', 'ip_address': '128.23.74.161:1720', 'id': None}}, {'MUSC Tidelands Murrells Inlet': {'name': 'MUSC Tidelands Murrells Inlet', 'protocol': 'H323', 'reg_time': '2019-10-10 17:48:11', 'hardware': None, 'dial_string': '8438767125@musc.edu', 'ip_address': '10.33.94.105:1720', 'id': None}}, {'CMIO Office Cannon Park': {'name': 'CMIO Office Cannon Park', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:03', 'hardware': None, 'dial_string': '8437920030@musc.edu', 'ip_address': '128.23.4.215:1720', 'id': None}}, {'MUSC HRID Room 1': {'name': 'MUSC HRID Room 1', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:03', 'hardware': None, 'dial_string': '8437921126@musc.edu', 'ip_address': '128.23.7.125:1720', 'id': None}}, {'record1@musc.edu': {'name': 'record1@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:57:04', 'hardware': 'TANDBERG/80 (S7.10)', 'dial_string': 'record1@musc.edu', 'ip_address': 'sip:record1@128.23.1.245:5060;transport=tcp', 'id': None}}, {'MUSC Summerville AHC': {'name': 'MUSC Summerville AHC', 'protocol': 'H323', 'reg_time': '2019-10-01 16:47:08', 'hardware': None, 'dial_string': '8438768950@musc.edu', 'ip_address': '10.33.79.46:1720', 'id': None}}, {'Art1119@musc.edu': {'name': 'Art1119@musc.edu', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:08', 'hardware': None, 'dial_string': '8438765721@musc.edu', 'ip_address': '128.23.70.205:1720', 'id': None}}, {'MUSC Beaufort Peds Specialty 02': {'name': 'MUSC Beaufort Peds Specialty 02', 'protocol': 'H323', 'reg_time': '2019-10-01 16:47:47', 'hardware': None, 'dial_string': '8438767126@musc.edu', 'ip_address': '10.33.3.144:1720', 'id': None}}, {'TCSH323': {'name': 'TCSH323', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:09', 'hardware': None, 'dial_string': None, 'ip_address': '128.23.1.245:1720', 'id': None}}, {'CenterForTelehealthLCPatient@musc.edu': {'name': 'CenterForTelehealthLCPatient@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 17:00:52', 'hardware': 'TANDBERG/529 (ce8.3.4.99243f7) Cisco-SX20', 'dial_string': 'CenterForTelehealthLCPatient@musc.edu', 'ip_address': 'sip:CenterForTelehealthLCPatient@128.23.26.152:5061;transport=tls', 'id': '"<urn:uuid:aa269666-7051-5ef7-95b5-5fdb218c2df6>"'}}, {'mcu5320@musc.edu': {'name': 'mcu5320@musc.edu', 'protocol': 'H323', 'reg_time': '2019-10-09 02:36:38', 'hardware': None, 'dial_string': '89999@musc.edu', 'ip_address': '128.23.1.1:1720', 'id': None}}, {'tridentfammed': {'name': 'tridentfammed', 'protocol': 'H323', 'reg_time': '2019-09-24 17:11:47', 'hardware': None, 'dial_string': '8438767080@musc.edu', 'ip_address': '128.23.51.196:1720', 'id': None}}, {'WestAshleyCardiology@musc.edu': {'name': 'WestAshleyCardiology@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:30', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-SX10', 'dial_string': 'WestAshleyCardiology@musc.edu', 'ip_address': 'sip:WestAshleyCardiology@128.23.246.42:5061;transport=tls', 'id': '"<urn:uuid:aaada106-700b-5c32-ad35-5ab508f17965>"'}}, {'CenterForTelehealthSmall@musc.edu': {'name': 'CenterForTelehealthSmall@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:31', 'hardware': 'TANDBERG/529 (ce8.2.1.e9daf06) Cisco-SX10', 'dial_string': 'CenterForTelehealthSmall@musc.edu', 'ip_address': 'sip:CenterForTelehealthSmall@128.23.57.61:5061;transport=tls', 'id': '"<urn:uuid:5225e5da-c73d-5487-b3cc-d006cf54c5ed>"'}}, {'MUSCWMC@musc.edu': {'name': 'MUSCWMC@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:36', 'hardware': 'TANDBERG/528 (TC7.3.3.c84180a)', 'dial_string': 'MUSCWMC@musc.edu', 'ip_address': 'sip:MUSCWMC@128.23.2.73:5061;transport=tls', 'id': '"<urn:uuid:6184b457-1e3a-5359-b0d9-134214cccf0d>"'}}, {'OrthoConfRmCSB708@musc.edu': {'name': 'OrthoConfRmCSB708@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:36', 'hardware': 'TANDBERG/528 (TC7.3.2.14ad7cc)', 'dial_string': 'OrthoConfRmCSB708@musc.edu', 'ip_address': 'sip:OrthoConfRmCSB708@128.23.157.77:5061;transport=tls', 'id': '"<urn:uuid:1e10e528-f364-5490-8f30-b09f1aab6f3c>"'}}, {'TelehealthTechnologyTeam': {'name': 'TelehealthTechnologyTeam', 'protocol': 'H323', 'reg_time': '2019-10-10 02:06:32', 'hardware': None, 'dial_string': '8437929999@musc.edu', 'ip_address': '128.23.200.254:1720', 'id': None}}, {'chpSX-10@musc.edu': {'name': 'chpSX-10@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:39', 'hardware': 'TANDBERG/529 (ce8.1.0.b8c0ca3)', 'dial_string': 'chpSX-10@musc.edu', 'ip_address': 'sip:chpSX-10@128.23.229.87:5061;transport=tls', 'id': '"<urn:uuid:ae0e8166-f126-5717-8303-3855677db5d0>"'}}, {'OCIO 4th Floor Conference Room 405': {'name': 'OCIO 4th Floor Conference Room 405', 'protocol': 'H323', 'reg_time': '2019-09-25 12:19:31', 'hardware': None, 'dial_string': '8437925351@musc.edu', 'ip_address': '128.23.59.122:1720', 'id': None}}, {'MUSC BEB 302': {'name': 'MUSC BEB 302', 'protocol': 'H323', 'reg_time': '2019-10-11 09:02:42', 'hardware': None, 'dial_string': '8437929000@musc.edu', 'ip_address': '128.23.20.196:1720', 'id': None}}, {'MUSC.OrthoTrauma.SX10@musc.edu': {'name': 'MUSC.OrthoTrauma.SX10@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:45', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-SX10', 'dial_string': 'MUSC.OrthoTrauma.SX10@musc.edu', 'ip_address': 'sip:MUSC.OrthoTrauma.SX10@128.23.156.227:5061;transport=tls', 'id': '"<urn:uuid:09dd96d0-1490-5b62-a954-e5ff1166a4fb>"'}}, {'telehealthtechnologyteam@musc.edu': {'name': 'telehealthtechnologyteam@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-10 02:06:44', 'hardware': 'PolycomRealPresenceGroup310/6.2.2', 'dial_string': 'telehealthtechnologyteam@musc.edu', 'ip_address': 'sip:telehealthtechnologyteam@128.23.200.254:5061;transport=tls', 'id': '"<urn:uuid:dd271a23-1721-5bfe-b32a-a0cfe3a57872>"'}}, {'NNICUSX10@musc.edu': {'name': 'NNICUSX10@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:48', 'hardware': 'TANDBERG/528 (TC7.3.5.a93bdb1)', 'dial_string': 'NNICUSX10@musc.edu', 'ip_address': 'sip:NNICUSX10@128.23.146.250:5061;transport=tls', 'id': '"<urn:uuid:7107603a-8d3d-50e4-90ae-f82bdf56382b>"'}}, {'261CannonParkPlace@musc.edu': {'name': '261CannonParkPlace@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:49', 'hardware': 'TANDBERG/529 (ce9.1.3.75ff735) Cisco-SX10', 'dial_string': '261CannonParkPlace@musc.edu', 'ip_address': 'sip:261CannonParkPlace@128.23.45.115:44609;transport=tls', 'id': '"<urn:uuid:1b7bd141-a409-56c3-84ed-615bffb62bac>"'}}, {'TurnerEX60@musc.edu': {'name': 'TurnerEX60@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:50', 'hardware': 'TANDBERG/528 (TC7.3.11.c1479a9) Cisco-EX60', 'dial_string': 'TurnerEX60@musc.edu', 'ip_address': 'sip:TurnerEX60@128.23.156.139:5061;transport=tls', 'id': '"<urn:uuid:5fc6ed35-139a-5ec5-b83c-35e1690d7097>"'}}, {'HRIDRoom1@musc.edu': {'name': 'HRIDRoom1@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:54', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-SX20', 'dial_string': 'HRIDRoom1@musc.edu', 'ip_address': 'sip:HRIDRoom1@128.23.7.125:5061;transport=tls', 'id': '"<urn:uuid:5a007ba1-1aa7-5fdc-a14c-6b23ed752971>"'}}, {'GallientSX10@musc.edu': {'name': 'GallientSX10@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:55', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-SX10', 'dial_string': 'GallientSX10@musc.edu', 'ip_address': 'sip:GallientSX10@128.23.206.98:5061;transport=tls', 'id': '"<urn:uuid:0d2cc5c7-c75e-5c41-a5ed-1dae1a5ccbc2>"'}}, {'CenterForTelehealth@musc.edu': {'name': 'CenterForTelehealth@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:56', 'hardware': 'TANDBERG/529 (ce8.2.2.3263c59) Cisco-SX80', 'dial_string': 'CenterForTelehealth@musc.edu', 'ip_address': 'sip:CenterForTelehealth@128.23.57.169:5061;transport=tls', 'id': '"<urn:uuid:ac6cf7f3-c00b-5360-b155-42c1ee8268a6>"'}}, {'cmiooffice@musc.edu': {'name': 'cmiooffice@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:58:57', 'hardware': 'TANDBERG/528 (TC7.3.7.01c84fd) Cisco-SX20', 'dial_string': 'cmiooffice@musc.edu', 'ip_address': 'sip:cmiooffice@128.23.4.215:5061;transport=tls', 'id': '"<urn:uuid:7d91edb7-36f7-5259-8e01-ac498e0cac4e>"'}}, {'muscambulatorycare@musc.edu': {'name': 'muscambulatorycare@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-02 18:33:17', 'hardware': 'PolycomRealPresenceGroup500/5.0.1', 'dial_string': 'muscambulatorycare@musc.edu', 'ip_address': 'sip:muscambulatorycare@128.23.4.59:5061;transport=tls', 'id': '"<urn:uuid:30de8517-4fbd-5e18-a7d8-6573b1f6590e>"'}}, {'HRIDAnteRoom@musc.edu': {'name': 'HRIDAnteRoom@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:07', 'hardware': 'TANDBERG/529 (ce9.1.4.3ae3106) Cisco-SX10', 'dial_string': 'HRIDAnteRoom@musc.edu', 'ip_address': 'sip:HRIDAnteRoom@128.23.157.67:5061;transport=tls', 'id': '"<urn:uuid:d4fa8d42-0162-57c7-af90-1bfeb2ff5240>"'}}, {'AfterHoursSummervilleCA300@musc.edu': {'name': 'AfterHoursSummervilleCA300@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-02 18:33:19', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-SX20', 'dial_string': 'AfterHoursSummervilleCA300@musc.edu', 'ip_address': 'sip:AfterHoursSummervilleCA300@10.33.79.46:5061;transport=tls', 'id': '"<urn:uuid:4d576e21-eeda-5080-8235-a3fff20bff62>"'}}, {'MUSC Telehealth Technology Team': {'name': 'MUSC Telehealth Technology Team', 'protocol': 'H323', 'reg_time': '2019-10-11 09:41:34', 'hardware': None, 'dial_string': '8437920010@musc.edu', 'ip_address': '10.33.48.163:1720', 'id': None}}, {'MUSC BEB201': {'name': 'MUSC BEB201', 'protocol': 'H323', 'reg_time': '2019-09-19 20:44:46', 'hardware': None, 'dial_string': '8438762324@musc.edu', 'ip_address': '128.23.20.182:1720', 'id': None}}, {'ART1119@musc.edu': {'name': 'ART1119@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-26 01:16:30', 'hardware': 'TANDBERG/529 (ce8.3.1.3276302) Cisco-SX80', 'dial_string': 'ART1119@musc.edu', 'ip_address': 'sip:ART1119@128.23.70.205:5061;transport=tls', 'id': '"<urn:uuid:e1db0bc0-ed6a-58d2-a89e-5f4e761d18be>"'}}, {'ARTChestPainCenter@musc.edu': {'name': 'ARTChestPainCenter@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:15', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-EX60', 'dial_string': 'ARTChestPainCenter@musc.edu', 'ip_address': 'sip:ARTChestPainCenter@128.23.74.161:5061;transport=tls', 'id': '"<urn:uuid:03803cbb-5902-51d7-992a-21a182c5b4e8>"'}}, {'muscvstsx20@musc.edu': {'name': 'muscvstsx20@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:18', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-SX20', 'dial_string': 'muscvstsx20@musc.edu', 'ip_address': 'sip:muscvstsx20@128.23.144.140:5061;transport=tls', 'id': '"<urn:uuid:04267227-7d82-5bbe-84d6-e5c09bcb80d1>"'}}, {'ART2008@musc.edu': {'name': 'ART2008@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:21', 'hardware': 'TANDBERG/529 (ce9.4.0.62bc0aa4505) Cisco-SX80', 'dial_string': 'ART2008@musc.edu', 'ip_address': 'sip:ART2008@128.23.76.230:5061;transport=tls', 'id': '"<urn:uuid:cfce3f82-7a9f-5728-9376-fc696f72917e>"'}}, {'chascenterfammed@musc.edu': {'name': 'chascenterfammed@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-12 07:37:03', 'hardware': 'PolycomHDX8000HD/3.1.12', 'dial_string': 'chascenterfammed@musc.edu', 'ip_address': 'sip:chascenterfammed@128.23.158.32:5060;transport=tcp', 'id': '"<urn:uuid:9f2027b4-614c-5024-9e07-c1ca850f27f1>"'}}, {'BeaufortPedsSpecialty02@musc.edu': {'name': 'BeaufortPedsSpecialty02@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-02 18:33:28', 'hardware': 'TANDBERG/529 (ce8.3.4.99243f7) Cisco-SX20', 'dial_string': 'BeaufortPedsSpecialty02@musc.edu', 'ip_address': 'sip:BeaufortPedsSpecialty02@10.33.3.144:5061;transport=tls', 'id': '"<urn:uuid:40f9865c-e699-5cb0-925a-1ab20bda3a1e>"'}}, {'colcockboardroom@musc.edu': {'name': 'colcockboardroom@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:36', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-SX80', 'dial_string': 'colcockboardroom@musc.edu', 'ip_address': 'sip:colcockboardroom@128.23.166.205:5061;transport=tls', 'id': '"<urn:uuid:3c811929-57a4-5f4e-ac69-95157d541fc8>"'}}, {'CenterForTelehealthCA750@musc.edu': {'name': 'CenterForTelehealthCA750@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:39', 'hardware': 'TANDBERG/529 (ce8.3.5.c877c7f) Cisco-SX20', 'dial_string': 'CenterForTelehealthCA750@musc.edu', 'ip_address': 'sip:CenterForTelehealthCA750@128.23.27.109:60016;transport=tls', 'id': '"<urn:uuid:9b34d9c2-60fd-5254-96f2-881e8327fe56>"'}}, {'AdultEX60-ED@musc.edu': {'name': 'AdultEX60-ED@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:46', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-EX60', 'dial_string': 'AdultEX60-ED@musc.edu', 'ip_address': 'sip:AdultEX60-ED@128.23.6.37:5061;transport=tls', 'id': '"<urn:uuid:4ef62583-f204-5d74-b538-fbbd357d51d5>"'}}, {'AdultEX60-ED2@musc.edu': {'name': 'AdultEX60-ED2@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:47', 'hardware': 'TANDBERG/528 (TC7.3.6.ea51021) Cisco-EX60', 'dial_string': 'AdultEX60-ED2@musc.edu', 'ip_address': 'sip:AdultEX60-ED2@128.23.26.64:5061;transport=tls', 'id': '"<urn:uuid:c814c83d-c6e1-5182-834e-a2d286d52619>"'}}, {'TCSSIP@musc.edu': {'name': 'TCSSIP@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-03 06:43:57', 'hardware': 'TANDBERG/80 (S7.10)', 'dial_string': 'TCSSIP@musc.edu', 'ip_address': 'sip:TCSSIP@128.23.1.245:5060;transport=tcp', 'id': None}}, {'record2@musc.edu': {'name': 'record2@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:54', 'hardware': 'TANDBERG/80 (S7.10)', 'dial_string': 'record2@musc.edu', 'ip_address': 'sip:record2@128.23.1.245:5060;transport=tcp', 'id': None}}, {'TCSSIPRecord@musc.edu': {'name': 'TCSSIPRecord@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-09-24 16:59:54', 'hardware': 'TANDBERG/80 (S7.10)', 'dial_string': 'TCSSIPRecord@musc.edu', 'ip_address': 'sip:TCSSIPRecord@128.23.1.245:5060;transport=tcp', 'id': None}}]

master_file_path = '/Users/matt/Desktop/work/vcs_monitor/master_file.txt'
def get_active_regs_names_times(all_registrations):
    """
    Copy registration's name + reg_time to a new dictionary
    :param all_registrations: dict
    :return: dict
    """

    new_dict = dict()

    for i in all_registrations:
        for k,v in i.items():
            new_dict[k] = v['reg_time']
            break

    return new_dict

#todo
# 1. get the NAME / CREATION TIME from each entry in ALL_REGISTRATIONS add to new dictionary
# 2. get the NAME from MASTER_FILE and compare against each NAME in ALL_REGISTRATIONS
# 3. if MF NAME in new dictionary, next ..... if MF NAME not in new dictionary, add to new dictionary
# 4. use status_reporter func on user input .... print(status_reporter(user input, new dictionary)
# ************ making search INCLUSIVE ************
# 5. check USER INPUT against all parts of NAME .... add ea. matched NAME to list
# 6. run NAME LIST through function to grab online status (status_reporter())


def add_historical_regs_names(reg_dict, file):
    """
    Add historical registrations from file and combine
    with active registrations
    :param reg_dict:
    :param file:
    :return:
    """

    master_registrations = read_master_file(file)
    for registration in master_registrations:
        if registration in reg_dict:
            continue
        else:
            reg_dict[registration] = ''

    return reg_dict


# def find_registration_matches(user_input, registration_dict):
#     """
#     Take registration search from input() and check if
#     any part of registration names match.  Return
#     matches as list
#     :param uinput: str - registration name
#     :param registration_dict: dict - consolidated registration names/times (master list + current registrations)
#     :return: list - registration data that matches search term
#     """
#
#     matches = []
#
#     uinput = strip_and_lower(user_input)
#
#     for registration in registration_dict.keys():
#         if uinput in strip_and_lower(registration):
#             matches.append(strip_and_lower(registration))
#
#     return matches

def xxyyxx(user_input, registration_dict):
    """
    Take registration search from input() and check if
    any part of registration names match.  Return
    matches as list
    :param uinput: str - registration name
    :param registration_dict: dict - consolidated registration names/times (master list + current registrations)
    :return: list - registration data that matches search term
    """

    results = []

    uinput = strip_and_lower(user_input)

    for reg_name, reg_time in registration_dict.items():
        if uinput in strip_and_lower(reg_name) and reg_time != '':

            results.append(strip_and_lower(reg_name))

    # for name, time in registration_dict.items():
    #     name = strip_and_lower(name)
    #
    #     if name == registration and time != '':
    #         return f'{registration} is ONLINE as of {time}'
    #
    #     elif name == registration:
    #         return f'{registration} is OFFLINE.'
    #
    # return f'ERROR: {registration} not found!'

    return results
#
# def status_reporter(registration, registration_dict):
#     """
#     Check if...
#     a) registration in dict &
#     b) registration has creation time
#     If registration + creation time, return ONLINE, else OFFLINE / NOT FOUND
#     :param registration: user input str
#     :param registration_dict: registration name / creation time dict
#     :return: str
#     """
#
#     for name, time in registration_dict.items():
#         name = strip_and_lower(name)
#
#         if name == registration and time != '':
#             return f'{registration} is ONLINE as of {time}'
#
#         elif name == registration:
#             return f'{registration} is OFFLINE.'
#
#     return f'ERROR: {registration} not found!'


active_reg_data = get_active_regs_names_times(all_registrations)
all_reg_data = add_historical_regs_names(active_reg_data, master_file_path)

while True:
    # search_str = input('Type a registration name')
    # reg_matches = find_registration_matches(search_str, all_reg_data)
    # for match in reg_matches:
    #     print(status_reporter(match, all_reg_data))
    search_str = input('Type a registration name')
    for reg_status in xxyyxx(search_str, all_reg_data):
        print(reg_status)

# noinspection PyUnreachableCode
'''


# todo pull out the below and refactor to APPEND registrations that don't exist
# populate_master_file(master_file_path, master_file_first_line(all_registrations))

master_file_content = read_master_file(master_file_path)

master_file_dict = dict()

for registration in master_file_content:
    master_file_dict[registration] = list()

for k, v in master_file_dict.items():
    for reg_info in all_registrations:
        _ = next(iter(reg_info))
        if k == _:
            v.insert(0, reg_info[_]['reg_time'])
            break

'''
