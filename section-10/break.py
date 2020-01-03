while True:
	command = input('Please enter \'quit\' to exit: ')
	if command == 'quit':
		break

for x in range(1, 101):
	print(x)
	if x >= 13:
		print('Is thirteen still unlucky...')
		break