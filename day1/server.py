from flask import Flask
from time import ctime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World! Karmapa Chenno"


@app.route("/status")
def status():
    return {
        'status' : True,
        'time' : ctime()
    }

app.run()