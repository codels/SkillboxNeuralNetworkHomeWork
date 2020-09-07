import time
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World 1! <a href='/status'>status</a>"


@app.route("/status")
def status():
    return {'status': 'OK', 'name': 'pychatgram', 'time': time.asctime()}


app.run()
