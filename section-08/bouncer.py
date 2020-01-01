# Concert entry, Ask for age
# 18 - 20 wristband
# 21+ can drink
# < 18 too young

# age = input('How old are you?\n')
# # If there's any value in age...
# if age: 
# 	age = int(age)
# 	if age >= 18 and age < 21:
# 		print('You can enter but you need a wristband')
# 	elif age >= 21:
# 		print('You are good to enter and can drink!')
# 	else: 
# 		print('Sorry, you\'re too young to enter :(')
# else:
# 	print('Please enter your age.')

age = input('How old are you?\n')
# If there's any value in age...
if age: 
	age = int(age)
	if age >= 21:
		print('You are good to enter and can drink!')
	elif age >= 18:
		print('You can enter but you need a wristband')
	else: 
		print('Sorry, you\'re too young to enter :(')
else:
	print('Please enter your age.')
