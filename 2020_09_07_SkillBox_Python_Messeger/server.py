import time
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)
db = []


@app.route("/")
def hello():
    return "Добпро пожаловать на сервер нашего Мессенджера! <a href='/status'>status</a>"


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'pychatgram',
        # 'time0': time.time(),
        # 'time1': time.asctime(),
        # 'time2': datetime.now(),
        # 'time3': datetime.now().isoformat(),
        'time': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
        # кол-во пользователей
        # кол-во сообщений
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

    return {'ok': True}


@app.route("/messages")
def messages():
    if 'after_id' in request.args:
        after_id = int(request.args['after_id']) + 1
    else:
        after_id = 0
    return {'messages': db[after_id:]}


app.run()
