from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World! Karmapa Chenno"


@app.route("/status")
def status():
    return "I'm alive"
app.run()