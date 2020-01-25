a = [1, 3, 2, 34, 5, 656, 4212, 37,6, 67]

# print(a)
# print(type(a))
# print(max(a))

def mymax(elements):
	if len(elements) == 0:
		return None
	else:
		m = elements[0]

		# for element in elements[1:]:
		# 	if element > m:
		# 		m = element
		i = 1
		while i < len(elements):
			if elements[i] > m:
				m = elements[i]
			i += 1

		return m

print(mymax(a))