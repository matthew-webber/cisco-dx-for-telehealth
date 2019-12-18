import requests
from datetime import datetime
import xml.etree.ElementTree as ET
import re
import os

def strip_and_lower(string):

    return string.strip().lower()


def strip_and_lower_list(list_):

    for _ in list_:
        _ = list_.pop(list_.index(_)).strip().lower()
        list_.insert(0, _)

    return list_


'''
Testing the below

    STEP 1 Open historical registrations file and read file
    STEP 2 Read active_registrations and compare with read file
    STEP 3 If active_registration not in read file, append to historical registration file



'''

all_registrations = [{'261 Cannon Park Place': {'name': '261 Cannon Park Place', 'protocol': 'H323',
                                                'reg_time': '2019-09-24 16:56:51', 'hardware': None,
                                                'dial_string': '8437924807@musc.edu',
                                                'ip_address': '128.23.45.115:1720', 'id': None}}, {
                         'MUSC Beaufort Peds Specialty 02': {'name': 'MUSC Beaufort Peds Specialty 02',
                                                             'protocol': 'H323', 'reg_time': '2019-10-15 16:18:54',
                                                             'hardware': None, 'dial_string': '8438767126@musc.edu',
                                                             'ip_address': '10.33.3.144:1720', 'id': None}}, {
                         'MUSCTTTVX ': {'name': 'MUSCTTTVX ', 'protocol': 'H323', 'reg_time': '2019-09-24 16:56:55',
                                        'hardware': None, 'dial_string': '8437920001@musc.edu',
                                        'ip_address': '128.23.200.77:1720', 'id': None}}, {
                         'MUSC Tidelands Murrells Inlet': {'name': 'MUSC Tidelands Murrells Inlet', 'protocol': 'H323',
                                                           'reg_time': '2019-10-15 16:19:02', 'hardware': None,
                                                           'dial_string': '8438767125@musc.edu',
                                                           'ip_address': '10.33.94.105:1720', 'id': None}}, {
                         'MUSC Center for Telehealth LC-Patient': {'name': 'MUSC Center for Telehealth LC-Patient',
                                                                   'protocol': 'H323',
                                                                   'reg_time': '2019-09-24 16:56:58', 'hardware': None,
                                                                   'dial_string': '8437920020@musc.edu',
                                                                   'ip_address': '128.23.26.152:1720', 'id': None}}, {
                         'MUSC Center for Telehealth Small Conference Room': {
                             'name': 'MUSC Center for Telehealth Small Conference Room', 'protocol': 'H323',
                             'reg_time': '2019-09-24 16:56:58', 'hardware': None, 'dial_string': '8437920012@musc.edu',
                             'ip_address': '128.23.57.61:1720', 'id': None}}, {
                         'MUSC Adult ED EX60-2': {'name': 'MUSC Adult ED EX60-2', 'protocol': 'H323',
                                                  'reg_time': '2019-08-02 11:22:10', 'hardware': None,
                                                  'dial_string': '8437923826@musc.edu',
                                                  'ip_address': '128.23.26.64:1720', 'id': None}}, {
                         'MUSC Center for Telehealth CA310': {'name': 'MUSC Center for Telehealth CA310',
                                                              'protocol': 'H323', 'reg_time': '2019-10-10 12:53:54',
                                                              'hardware': None, 'dial_string': '8437920013@musc.edu',
                                                              'ip_address': '128.23.57.129:1720', 'id': None}}, {
                         'MUSC ART Chest Pain Center EX60': {'name': 'MUSC ART Chest Pain Center EX60',
                                                             'protocol': 'H323', 'reg_time': '2019-09-24 16:57:03',
                                                             'hardware': None, 'dial_string': '8438767175@musc.edu',
                                                             'ip_address': '128.23.74.161:1720', 'id': None}}, {
                         'CMIO Office Cannon Park': {'name': 'CMIO Office Cannon Park', 'protocol': 'H323',
                                                     'reg_time': '2019-09-24 16:57:03', 'hardware': None,
                                                     'dial_string': '8437920030@musc.edu',
                                                     'ip_address': '128.23.4.215:1720', 'id': None}}, {
                         'MUSC HRID Room 1': {'name': 'MUSC HRID Room 1', 'protocol': 'H323',
                                              'reg_time': '2019-09-24 16:57:03', 'hardware': None,
                                              'dial_string': '8437921126@musc.edu', 'ip_address': '128.23.7.125:1720',
                                              'id': None}}, {
                         'Art1119@musc.edu': {'name': 'Art1119@musc.edu', 'protocol': 'H323',
                                              'reg_time': '2019-09-24 16:57:08', 'hardware': None,
                                              'dial_string': '8438765721@musc.edu', 'ip_address': '128.23.70.205:1720',
                                              'id': None}}, {
                         'TCSH323': {'name': 'TCSH323', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:09',
                                     'hardware': None, 'dial_string': None, 'ip_address': '128.23.1.245:1720',
                                     'id': None}}, {'tridentfammed': {'name': 'tridentfammed', 'protocol': 'H323',
                                                                      'reg_time': '2019-09-24 17:11:47',
                                                                      'hardware': None,
                                                                      'dial_string': '8438767080@musc.edu',
                                                                      'ip_address': '128.23.51.196:1720', 'id': None}},
                     {'TelehealthTechnologyTeam': {'name': 'TelehealthTechnologyTeam', 'protocol': 'H323',
                                                   'reg_time': '2019-10-10 02:06:32', 'hardware': None,
                                                   'dial_string': '8437929999@musc.edu',
                                                   'ip_address': '128.23.200.254:1720', 'id': None}}, {
                         'OCIO 4th Floor Conference Room 405': {'name': 'OCIO 4th Floor Conference Room 405',
                                                                'protocol': 'H323', 'reg_time': '2019-09-25 12:19:31',
                                                                'hardware': None, 'dial_string': '8437925351@musc.edu',
                                                                'ip_address': '128.23.59.122:1720', 'id': None}}, {
                         'MUSC BEB 302': {'name': 'MUSC BEB 302', 'protocol': 'H323', 'reg_time': '2019-10-11 09:02:42',
                                          'hardware': None, 'dial_string': '8437929000@musc.edu',
                                          'ip_address': '128.23.20.196:1720', 'id': None}}, {
                         'chascenterfammed': {'name': 'chascenterfammed', 'protocol': 'H323',
                                              'reg_time': '2019-10-15 05:14:08', 'hardware': None,
                                              'dial_string': '8438762912@musc.edu', 'ip_address': '128.23.158.32:1720',
                                              'id': None}}, {
                         'MUSC Telehealth Technology Team': {'name': 'MUSC Telehealth Technology Team',
                                                             'protocol': 'H323', 'reg_time': '2019-10-11 09:41:34',
                                                             'hardware': None, 'dial_string': '8437920010@musc.edu',
                                                             'ip_address': '10.33.48.163:1720', 'id': None}}, {
                         'Specialty Care North': {'name': 'Specialty Care North', 'protocol': 'H323',
                                                  'reg_time': '2019-10-14 11:21:07', 'hardware': None,
                                                  'dial_string': '8438761677@musc.edu',
                                                  'ip_address': '128.23.225.140:1720', 'id': None}}, {
                         'MUSC QF105': {'name': 'MUSC QF105', 'protocol': 'H323', 'reg_time': '2019-10-15 16:33:59',
                                        'hardware': None, 'dial_string': '8437920105@musc.edu',
                                        'ip_address': '128.23.104.103:1720', 'id': None}}]
# all_registrations = [{'record3@musc.edu': {'name': 'record3@musc.edu', 'protocol': 'SIP', 'reg_time': '2019-10-15 21:02:05', 'hardware': 'TANDBERG/80 (S7.10)', 'dial_string': 'record3@musc.edu', 'ip_address': 'sip:record3@128.23.1.245:5060;transport=tcp', 'id': None}}, {'261 Cannon Park Place': {'name': '261 Cannon Park Place', 'protocol': 'H323', 'reg_time': '2019-09-24 16:56:51', 'hardware': None, 'dial_string': '8437924807@musc.edu', 'ip_address': '128.23.45.115:1720', 'id': None}}, {'MUSC Beaufort Peds Specialty 02': {'name': 'MUSC Beaufort Peds Specialty 02', 'protocol': 'H323', 'reg_time': '2019-10-15 16:18:54', 'hardware': None, 'dial_string': '8438767126@musc.edu', 'ip_address': '10.33.3.144:1720', 'id': None}}, {'MUSCTTTVX ': {'name': 'MUSCTTTVX ', 'protocol': 'H323', 'reg_time': '2019-09-24 16:56:55', 'hardware': None, 'dial_string': '8437920001@musc.edu', 'ip_address': '128.23.200.77:1720', 'id': None}}, {'MUSC Tidelands Murrells Inlet': {'name': 'MUSC Tidelands Murrells Inlet', 'protocol': 'H323', 'reg_time': '2019-10-15 16:19:02', 'hardware': None, 'dial_string': '8438767125@musc.edu', 'ip_address': '10.33.94.105:1720', 'id': None}}, {'MUSC Center for Telehealth LC-Patient': {'name': 'MUSC Center for Telehealth LC-Patient', 'protocol': 'H323', 'reg_time': '2019-09-24 16:56:58', 'hardware': None, 'dial_string': '8437920020@musc.edu', 'ip_address': '128.23.26.152:1720', 'id': None}}, {'MUSC Center for Telehealth Small Conference Room': {'name': 'MUSC Center for Telehealth Small Conference Room', 'protocol': 'H323', 'reg_time': '2019-09-24 16:56:58', 'hardware': None, 'dial_string': '8437920012@musc.edu', 'ip_address': '128.23.57.61:1720', 'id': None}}, {'MUSC Adult ED EX60-2': {'name': 'MUSC Adult ED EX60-2', 'protocol': 'H323', 'reg_time': '2019-08-02 11:22:10', 'hardware': None, 'dial_string': '8437923826@musc.edu', 'ip_address': '128.23.26.64:1720', 'id': None}}, {'MUSC Center for Telehealth CA310': {'name': 'MUSC Center for Telehealth CA310', 'protocol': 'H323', 'reg_time': '2019-10-10 12:53:54', 'hardware': None, 'dial_string': '8437920013@musc.edu', 'ip_address': '128.23.57.129:1720', 'id': None}}, {'MUSC ART Chest Pain Center EX60': {'name': 'MUSC ART Chest Pain Center EX60', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:03', 'hardware': None, 'dial_string': '8438767175@musc.edu', 'ip_address': '128.23.74.161:1720', 'id': None}}, {'CMIO Office Cannon Park': {'name': 'CMIO Office Cannon Park', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:03', 'hardware': None, 'dial_string': '8437920030@musc.edu', 'ip_address': '128.23.4.215:1720', 'id': None}}, {'MUSC HRID Room 1': {'name': 'MUSC HRID Room 1', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:03', 'hardware': None, 'dial_string': '8437921126@musc.edu', 'ip_address': '128.23.7.125:1720', 'id': None}}, {'Art1119@musc.edu': {'name': 'Art1119@musc.edu', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:08', 'hardware': None, 'dial_string': '8438765721@musc.edu', 'ip_address': '128.23.70.205:1720', 'id': None}}, {'TCSH323': {'name': 'TCSH323', 'protocol': 'H323', 'reg_time': '2019-09-24 16:57:09', 'hardware': None, 'dial_string': None, 'ip_address': '128.23.1.245:1720', 'id': None}}, {'tridentfammed': {'name': 'tridentfammed', 'protocol': 'H323', 'reg_time': '2019-09-24 17:11:47', 'hardware': None, 'dial_string': '8438767080@musc.edu', 'ip_address': '128.23.51.196:1720', 'id': None}}, {'TelehealthTechnologyTeam': {'name': 'TelehealthTechnologyTeam', 'protocol': 'H323', 'reg_time': '2019-10-10 02:06:32', 'hardware': None, 'dial_string': '8437929999@musc.edu', 'ip_address': '128.23.200.254:1720', 'id': None}}, {'OCIO 4th Floor Conference Room 405': {'name': 'OCIO 4th Floor Conference Room 405', 'protocol': 'H323', 'reg_time': '2019-09-25 12:19:31', 'hardware': None, 'dial_string': '8437925351@musc.edu', 'ip_address': '128.23.59.122:1720', 'id': None}}, {'MUSC BEB 302': {'name': 'MUSC BEB 302', 'protocol': 'H323', 'reg_time': '2019-10-11 09:02:42', 'hardware': None, 'dial_string': '8437929000@musc.edu', 'ip_address': '128.23.20.196:1720', 'id': None}}, {'chascenterfammed': {'name': 'chascenterfammed', 'protocol': 'H323', 'reg_time': '2019-10-15 05:14:08', 'hardware': None, 'dial_string': '8438762912@musc.edu', 'ip_address': '128.23.158.32:1720', 'id': None}}, {'MUSC Telehealth Technology Team': {'name': 'MUSC Telehealth Technology Team', 'protocol': 'H323', 'reg_time': '2019-10-11 09:41:34', 'hardware': None, 'dial_string': '8437920010@musc.edu', 'ip_address': '10.33.48.163:1720', 'id': None}}, {'Specialty Care North': {'name': 'Specialty Care North', 'protocol': 'H323', 'reg_time': '2019-10-14 11:21:07', 'hardware': None, 'dial_string': '8438761677@musc.edu', 'ip_address': '128.23.225.140:1720', 'id': None}}, {'MUSC QF105': {'name': 'MUSC QF105', 'protocol': 'H323', 'reg_time': '2019-10-15 16:33:59', 'hardware': None, 'dial_string': '8437920105@musc.edu', 'ip_address': '128.23.104.103:1720', 'id': None}}]

historical_registrations_path = '/Users/Webber/Desktop/work/vcs_monitor/master_file.txt'



def read_master_file(file):
    """
    Reads the first line (registration names) of the master file & returns as a list
    :param file: file obj
    :return: list
    """
    with open(file, 'r') as f:
        registrations = f.readline().split(',')
        return registrations


def read_append_master_file(file, active_registrations):
    registrations_to_add = []
    remaining_lines = ''

    # STEP 1

    with open(file, 'r') as f:
        historical_registrations = f.readline()
        while f.readline():
            remaining_lines += f.readline()

    # STEP 2

    historical_registrations = historical_registrations.split(',')
    for active_registration in active_registrations:
        for name in active_registration.keys():
            if strip_and_lower(name) not in strip_and_lower_list(historical_registrations):
                registrations_to_add.append(name)

    file_overwrite = f'{",".join(historical_registrations)}\n{remaining_lines}'

    # historical_registrations += registrations_to_add
    # historical_registrations.append('\n')
    # historical_registrations += remaining_lines

    with open(file, 'w') as f:
        # f.write(','.join(historical_registrations))
        f.write(file_overwrite)

    return historical_registrations


a = read_append_master_file(historical_registrations_path, all_registrations)
# a = read_master_file(historical_registrations_path)
# b = set(a)
#
# print(len(a))
# print(len(b))
#
#
# for i in a:
#     print(i)
#
# print('set***********')
# for i in b:
#     print(i)