import requests
from datetime import datetime
import xml.etree.ElementTree as ET
import re
import os

master_file = '/Users/Webber/Desktop/work/vcs_monitor/master_file.txt'


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

    with open(file, 'r') as f:
        registrations = f.readline().split(',')
        return registrations
        # registrations =


def populate_master_file(file, first_line):

    with open(file, 'w') as f:
        f.write(first_line)


def get_data_xml(node, registration):

    protocol = registration.find('Protocol').text

    if node == 'name':
        return get_name_xml(registration, protocol)

    elif node == 'protocol':
        return get_protocol_xml(registration, protocol)

    elif node == 'reg_time':
        return get_regtime_xml(registration, protocol)

    elif node == 'hardware':
        return get_hardware_xml(registration, protocol)

    elif node == 'dial_string':
        return get_dialstring_xml(registration, protocol)

    elif node == 'ip_address':
        return get_ipaddress_xml(registration, protocol)

    elif node == 'id':
        return get_id_xml(registration, protocol)


def get_name_xml(registration, protocol):

    if protocol == 'H323':
        return registration.find('./H323/Aliases/Alias[Type="H323Id"]/Value').text

    elif protocol == 'SIP':
        return registration.find('./SIP/AOR').text


def get_protocol_xml(registration, protocol):

    return registration.find('Protocol').text


def get_regtime_xml(registration, protocol):

    return registration.find('CreationTime').text


def get_hardware_xml(registration, protocol):

    if protocol == 'H323':
        return None
    elif protocol == 'SIP':
        return registration.find('VendorInfo').text


def get_dialstring_xml(registration, protocol):

    if protocol == 'H323':

        try:
            dial_string = f"""{registration.find('./H323/Aliases/Alias[Type="E164"]/Value').text}@musc.edu"""
        except AttributeError:
            dial_string = None

        return dial_string

    elif protocol == 'SIP':
        return registration.find('./SIP/AOR').text


def get_ipaddress_xml(registration, protocol):

    if protocol == 'H323':
        return registration.find('./H323/CallSignalAddresses/Address').text
    elif protocol == 'SIP':
        return registration.find('./SIP/Contact').text


def get_id_xml(registration, protocol):

    if protocol == 'H323':
        return None
    elif protocol == 'SIP':
        return registration.find('./SIP/Instance').text


def get_save_xml(username, password, path):

    url = f'https://{username}:{password}@muscgk1.mdc.musc.edu/status.xml'

    xml_doc = requests.get(url)
    xml_clean = re.sub(' xmlns="[^"]+?"', "", xml_doc.text)
    file_name = f'{path}status-{save_time}.xml'

    with open(file_name,'w') as f:
        f.write(xml_clean)

    return file_name


def create_reg_files(reg_list, path):

    file_str = ''

    for reg in reg_list:
        for k, v in reg.items():
            with open(path + k + '.txt', 'w') as f:
                for key, value in v.items():
                    if file_str == '':
                        file_str = f'{key}|{value}'
                    else:
                        file_str = f'{file_str}\n{key}|{value}'

                f.write(file_str)
                file_str = ''


# def list_names(type, root):
#
#     if type == 'H323':
#         return [reg.text for reg in root.findall('./Registrations/Registration/H323/Aliases/Alias[Type="H323Id"]/Value')]
#     if type == 'SIP':
#         return [reg.text for reg in root.findall('./Registrations/Registration/SIP/AOR')]

# def get_registration_time(registration, )


save_time = datetime.strftime(datetime.now(),'%Y%m%d-%H%M%S')
# path = f'/Users/Webber/desktop/work/vcs_monitor/pull{save_time}/'
# os.mkdir(path)
path = '/Users/Webber/Desktop/work/vcs_monitor/pull20191012-224811/status-20191012-224811.xml'

username = 'admin'
password = 'IPv4ever!'




# xml_path = get_save_xml(username, password, path)
xml_path = '/Users/Webber/Desktop/work/vcs_monitor/pull20191012-224811/status-20191012-224811.xml'

tree = ET.parse(xml_path)
root = tree.getroot()

registrations = list(root.find('Registrations'))

all_registrations = []

for registration in registrations:

    registration_data = dict(
        name=get_data_xml('name', registration),
        protocol=get_data_xml('protocol', registration),
        reg_time=get_data_xml('reg_time', registration),
        hardware=get_data_xml('hardware', registration),
        dial_string=get_data_xml('dial_string', registration),
        ip_address=get_data_xml('ip_address', registration),
        id=get_data_xml('id', registration)
    )

    all_registrations.append({registration_data['name']:registration_data})

populate_master_file(master_file, master_file_first_line(all_registrations))
first_line_master_list = read_master_file(master_file)
master_file_dict = dict()

for registration in first_line_master_list:
    master_file_dict[registration] = list()


#
# create_reg_files(all_registrations, path)





