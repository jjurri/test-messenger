from random import randint

import oldmax


users = [
	{
		'name': 'Jack',
		'password': '1234567890',
		'age': 10
	},
	{
		'name': 'Helen',
		'password': '0987654321',
		'age': 50
	}
]


for i in range(10):
	users.append({
		'name': oldmax.generate_name(),
		'password': oldmax.generate_name(),
		'age': randint(1, 100)
	})

print(users)

print(oldmax.oldmax(users))
