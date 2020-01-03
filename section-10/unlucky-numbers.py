# for num in range (1, 21):
# 	if num == 4 or num == 13:
# 		print(str(num) + " is unlucky!")
# 	else:
# 		if num % 2 == 0:
# 			print(f'{num} is even.')
# 		else:
# 			print('{} is odd.'.format(num))

for num in range (1, 21):
	if num == 4 or num == 13:
		state = 'unlucky!'
	else:
		if num % 2 == 0:
			state = 'even.'
		else:
			state = 'odd.'
	print('{} is {}'.format(num, state))