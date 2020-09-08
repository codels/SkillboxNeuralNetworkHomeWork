import time
from datetime import datetime
import random

from flask import Flask, request

app = Flask(__name__)
db = []


@app.route("/")
def hello():
    return "Добро пожаловать на сервер нашего Мессенджера! <a href='/status'>status</a>"


@app.route("/status")
def status():
    users = set()
    for message in db:
        users.add(message['name'])
    return {
        'status': True,
        'name': 'pychatgram',
        # 'time0': time.time(),
        # 'time1': time.asctime(),
        # 'time2': datetime.now(),
        # 'time3': datetime.now().isoformat(),
        'time': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
        'users': len(users),  # кол-во пользователей
        'messages': len(db),  # кол-во сообщений
    }


@app.route("/send", methods=['POST'])
def send():
    data = request.json

    # timestamp = time.time()
    db.append({
        'id': len(db),
        'name': data['name'],
        'text': data['text'],
        'timestamp': time.time()
    })

    # чат бот
    # if text ...
    if data['text'][0] == '/':
        command = data['text'][1:]

        result = 'command "' + command + '" not found'

        if command == 'random':
            result = random.randrange(100)

        db.append({
            'id': len(db),
            'name': 'BOT',
            'text': result,
            'timestamp': time.time()
        })

    return {'ok': True}


@app.route("/messages")
def messages():
    after_id = 0
    limit = 100

    if 'after_id' in request.args:
        after_id = int(request.args['after_id']) + 1

    if 'limit' in request.args:
        limit = int(request.args['limit'])

    end = after_id + limit

    return {'messages': db[after_id:end]}


app.run()
