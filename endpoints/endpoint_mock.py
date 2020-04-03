import csv
from data.teleport_data import RoleDefiner


class MockDataDaemon:

    def __init__(self):
        pass

    @staticmethod
    def pull_all_data(path='/Users/matt/PycharmProjects/dx_sx_api/testing/dummy_dx_data.csv'):
        """
        Take the contents of a csv file and create a dict based on each row
        and then add to a list of dicts (rows)

        :param path: path of the csv file
        :return: list(dict)
        """
        pulled_data = list()
        with open(path, 'r', newline='') as f:
            reader = csv.reader(f)
            headers = [header for header in next(reader)]
            for row in reader:
                pulled_data.append({headers[i]: row[i] for i, val in enumerate(row)})

        return pulled_data

    @staticmethod
    def search_data(data, target):
        """
        Given a list of dicts in a form which matches the csv data form above,
        returns a data "row" that matches that IP

        :param data: list of dicts containing mock object data
        :param target: str of IP
        :return: dict containing mock data with IP that matches target IP
        """
        for _ in data:
            if _['ip'] == target:
                return _

        print(f'An IP matching {target} not found!')
        return None  # matching IP not found in given data


class MockEndpointFactory:

    def __init__(self):
        self.mock_data = MockDataDaemon.pull_all_data()  # prep the factory by gathering all data from the .csv file

    def process_data(self, ip_list: list):
        """
        Uses the mock data daemon to perform an iterative search over the mock data
        and put these into containers for the parent factory to use

        :param ip_list: list of IPs to create objects for
        :return: dict of lists for mock objs and objects not in the .csv file
        """
        # create another list of dicts with {ip : row_data}
        # that way, if the row data isn't there, it can bring a "None" object back to the parent factory
        # and more processing can take place
        matching_data = {ip: MockDataDaemon.search_data(self.mock_data, ip) for ip in ip_list}

        # make mock objects if they have data
        mock_objects = [MockEndpointFactory.create(data_match) for ip, data_match
                        in matching_data.items() if data_match]

        # todo make the above and below look better -- shouldn't be making 2 lists here...

        # if data_match is None, these IPs didn't exist in the table
        # pass them up to the parent factory
        unknown_ips = [ip for ip, data_match
                        in matching_data.items() if not data_match]

        return {'offline': mock_objects, 'unknowns': unknown_ips}

    @staticmethod
    def create(mock_object_data):
        return TestEndpointMock(mock_object_data)


class TestEndpointMock:

    def __init__(self, endpoint_data):
        self.ip = endpoint_data['ip']
        self.name = endpoint_data['name']
        self.call_string = endpoint_data['call_string']
        self._role, self._type = None, None

        # self.status = endpoint_data['status']
        # print(f'Logging in to {self.ip}...')
        # print(f'Success!')
        
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, role):
        self._role = role       
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type_):
        self._type = type_


if __name__ == '__main__':

    mock_ips = ['10.33.155.0', '10.33.110.0', '10.33.110.200']

    factory = MockEndpointFactory()

    a = factory.process_data(mock_ips)

