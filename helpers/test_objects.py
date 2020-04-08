from random import choices, randint
from creds import endpoint_data
from time import sleep

def get_status_code(status_codes=(401, 'FAILED_CONNECTION', 200)):
    """
    Testing with DataFetcher.fetch_data
    :param status_codes: DataFetcher.fetch_data returns these "status codes"
    :return: status codes according to weight
    """
    # highest: Good connection, next: Timeout, last: incorrect username/pw
    code = choices(status_codes, [5, 10, 40])[0]

    # simulate time it takes to get status code using requests
    if code == 200:
        isleep = 1
    else:
        isleep = 2

    sleep(isleep)
    return code

# def test_data():
#     x = endpoint_data.copy()
#
#     x['login_url'] = x['login_url'].replace('$ip', )
#     x['test_url'] = x['test_url'].replace('$ip', ip)