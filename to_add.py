from typing import Dict, Match
import re
import help
import xml.etree.ElementTree as et
from datetime import datetime

content_servers = dict(
    # vcs_c='https://muscgk1.mdc.musc.edu/status.xml',
    # vcs_e='https://bc1.musc.edu/status.xml',
    thisthat='/Users/matt/Desktop/work/vcs_monitor/pull20191012-224811/status-20191012-224811.xml'
)

def
def lower_and_strip(input):
    return input.strip().lower()


def parse_user_input(uinput):

    match_object = re.match(r"([\w\W\d]+?) (-?[e?])", uinput)
    if match_object is None:
        return uinput
    return match_object

# todo make this work for show all registrations???
# def show_all(thing):
#     if isinstance(thing, Deck):
#         for card in deck.stack:
#             i = deck.stack.index(card) + 1
#             print(f"""Card #{i} {card.front}/{card.back}""")


def show_help(*args):
    print(help.help_text)


def quit(*args):
    quit_confirm = lower_and_strip(input('Are you sure you want to quit? (Y/N)'))

    if quit_confirm == 'y':
        save_confirm = lower_and_strip(input('Do you want to save your deck? (Y/N)'))

        if save_confirm == 'y':
            return 'quit_and_save'

        else:
            return 'quit_no_save'

    return 'back to loop'


def reg_check(mode):

    x = ModeBuilder(mode)
    print(x.mode_greeting)
    response = QueryString(lower_and_strip(input()))


class QueryString:

    def __init__(self, query):
        self.query = query
        self.response = self.query_server()

    def query_server(self):
        thisthat = []
        for url in content_servers.values():
            thisthat.append(RegistrationData(url))

        return thisthat

class RegistrationData():

    def __init__(self, url):
        # self.save_time = datetime.strftime(datetime.now(),'%Y%m%d-%H%M%S')
        self.xml_file = et.parse(url)
        self.registrations = self.parse_xml('Registrations')

    def save_data(self, path, save_time):
        pass

    def parse_xml(self, target):

        root = self.xml_file.getroot()

        try:
            return list(root.find(target))

        except KeyError:
            print('could not find')


class CommandHandler:

    commands = \
        dict(
            # todo parse out showall to be show + all
            quit={
                'name': 'quit',
                'command': 'Q',
                'action': 'Exit current mode',
                'quit_and_save': True,
                'quit_no_save': True,
                'function': quit},
            regcheck={
                'name': 'regcheck',
                'command': 'rc',
                'action': 'Check registration status',
                'function': reg_check},
            # todo show all registrations, not cards
            showall={
                'name': 'showall',
                'command': 'showall',
                'action': 'Show all files/cards/decks/etc.',
                'function': ''},
            help={
                'name': 'help',
                'command': 'help',
                'action': 'Show help file text',
                'function': show_help},
        )

    def __init__(self, command='', *args):
        self.command = command
        self.process_command()

    def check_command(self, command, *args):
        response = CommandHandler.commands.get(command)

        if response:
            return response

    def process_command(self):

        CommandHandler.commands[self.command]['function'](self.command)



class ModeBuilder:

    start_strings = {
        'edit': f"""
Choose which card you want to edit by typing [card_index_number_here] -e""",
        'regcheck': f"""
Enter the full or partial name of a registration to search.""",
        'end': """""",
        'insertion': """""",
    }

    modes: Dict[str, dict] = \
        dict(
            # end={'input': 'x', 'name': 'end', 'value': 0, 'startString': start_strings['end']},
            regcheck={'input': 's', 'name': 'regcheck', 'value': 1, 'startString': start_strings['regcheck']},
            # edit={'input': 'e', 'name': 'edit', 'value': 2, 'startString': start_strings['edit']},
            # insertion={'input': 'i', 'name': 'insertion', 'value': 10, 'startString': start_strings['insertion']}
        )

    def __init__(self, mode):
        self.mode = self.set_mode(mode)

    @property
    def mode_greeting(self):
        return ModeBuilder.modes[self.mode['name']]['startString']

    def set_mode(self, mode):
        """
        Print the mode_greeting and set self.mode

        """
        return ModeBuilder.modes[mode]
        # self.mode_change()

    def mode_change(self):
        print(f"*~*~* Entering {self.mode['name'].upper()} mode *~*~*")
        print(self.mode_greeting)

    def get_mode(self):
        return self.mode

    def input_to_name(self, input):
        for contents in self.modes.values():
            if input in contents.values():
                return contents['name']




while True:

    # check for command before checking for mode
    clean_input = lower_and_strip(input())
    command = CommandHandler(clean_input)

    # mode_selection = x.input_to_name(clean_input)

    # print "Doing the thing now"
    # get the data
    # store data in object
    # search against data
    # present data
    '''

    if mode_selection is None:
        if clean_input in CommandHandler.commands:
            controller = CommandHandler(clean_input)
            continue
        else:
            print('Command not recognized.')
            continue

    elif mode_selection:
        x.set_mode(mode_selection)

    else:
        print('Command not recognized.')
        continue
    '''
