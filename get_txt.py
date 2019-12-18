import requests
from datetime import datetime
import xml.etree.ElementTree as ET
import re
import os


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

save_time = datetime.strftime(datetime.now(),'%Y%m%d-%H%M%S')

path = '/Users/matt/Desktop/work/vcs_monitor/pull20191012-224811/'
