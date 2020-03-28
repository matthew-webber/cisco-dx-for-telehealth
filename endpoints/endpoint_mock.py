

class TestEndpointMock:

    def __init__(self, ip, name, call_string, type_, role, status):
        self.ip = ip
        self.name = name
        self.call_string = call_string
        self.type = type_
        self.role = role
        self.status = status
        print(f'Logging in to {self.ip}...')
        print(f'Success!')



import csv

x = list()

# the below can take the contents of a csv file and put each row as a dict into a list of dicts
# the dict can then be used to create an object

with open('../thisthat.csv', newline='') as f:
    reader = csv.reader(f)
    # dynamic mapping of values + headers
    headers = [header for header in next(reader)]
    for row in reader:
        x.append({headers[i]: row[i] for i, val in enumerate(row)})

for i in x:
    thisthat = TestEndpointMock(ip=i['ip'], name=i['name'], call_string=i['call_string'], type_=i['type_'], role=i['role'], status=i['status'])
