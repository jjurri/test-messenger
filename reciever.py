import time

import requests

last_time = 0

while True:
	response = requests.get("http://127.0.0.1:5000/messages",
	                        params={'after': last_time})
	messages = response.json()["messages"]

	for message in messages:
		print(message["username"], message["time"])
		print(message["text"])
		print()

		last_time = message["time"]

	time.sleep(2)