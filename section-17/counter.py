def counter():
	count = int(input('What should I countdown from?\n'))
	
	def increment():
		nonlocal count
		while count > 0:
			print(count)
			count -= 1

	increment()

counter()