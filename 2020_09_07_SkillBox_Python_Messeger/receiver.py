import requests
import time
from datetime import datetime


def pretty_print(message):
    """
    2020/09/08 10:00:23 Nick
    Text

    """
    dt = datetime.fromtimestamp(message['timestamp'])
    dt = dt.strftime('%Y/%m/%d %H:%M:%S')
    first_line = dt + '   ' + message['name']
    print(first_line)
    print(message['text'])
    print()


url = 'http://127.0.0.1:5000/messages'

# response = requests.get(url)
# messages = response.json()['messages']
# print(messages)

after_timestamp = -1

# response = requests.get(url, params={'after_id': after_id})
# print(response.json())

# пагинация, по кусочка не более 100 сообщений
limit = 100

while True:
    response = requests.get(url, params={'after_timestamp': after_timestamp, 'limit': limit})
    messages = response.json()['messages']
    for message in messages:
        pretty_print(message)
        after_timestamp = message['timestamp']

    if not messages:
        time.sleep(1)
