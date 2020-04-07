import csv

class EndpointStorage:

    def __init__(self, endpoints):
        self.online = endpoints['online']
        self.offline = endpoints['offline']

    def add_endpoints(self, endpoints, status):
        """# todo """
        if status == "ONLINE":
            self.online.append(endpoints)
        elif status == "OFFLINE":
            self.offline.append(endpoints)


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


class XmlProcessor:

    pass
