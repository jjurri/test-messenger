from flask import Flask, request
from time import ctime
import time

app = Flask(__name__)
messages = [
    {"username": "Jack", "text": "Hello!", "time": time.ctime()},
    {"username": "Mary", "text": "Hi!", "time": time.ctime()},
]
users = {
    'Jack': '12345',
    'Mary': '54321'
}



@app.route("/")
def hello_view():
    return "Welcome to Python messenger"


@app.route("/status")
def status_view():
    return {
        'status': True,
        'time': ctime(),
        'messages_count': len(messages),
        'user_count': len(users)
    }

@app.route("/messages")
def messages_view():
    """
    Get messages after timestamp after
    input: after - timestamp
    output: {
        "messages": [
            {"username": str, "text": str, "time": float},
            ...
        ]
    }
    """
    after = request.args['after']
    new_messages = [message for message in messages if message['time'] > after]
    return {'messages': new_messages}


@app.route("/send", methods=['POST'])
def send_view():
    """
        Send messages
        input: {
            "username": str,
            "password": str,
            "text": str
        }
        output: {"ok": true}
        """
    data = request.json
    username = data["username"]
    password = data["password"]

    if username not in users or users[username] != password:
        return {"ok": False}


    text = data["text"]

    messages.append({"username": username, "text": text, "time": time.ctime()})

    return {'ok': True}

@app.route("/auth", methods=['POST'])
def auth_view():
    """
        Authorize user or tell that password is incorrect
        input: {
            "username": str,
            "password": str,
        }
        output: {"ok": bool}
        """
    data = request.json
    username = data["username"]
    password = data["password"]

    if username not in users:
        users[username] = password
        return {"ok": True}
    elif users[username] == password:
        return {"ok": True}
    else:
        return {"ok": False}
if __name__ == '__main__':
    app.run()