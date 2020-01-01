age = int(input('Please enter your age: '))
# 2 - 8, 2 dollars
# 65, 5 dollars
# infants, 0 dollars
# adults, 10 dollars

# if age < 2:
# 	print(f'At {age} years old you get to watch for free! (infant rate)')
# elif 1 < age < 9:
# 	print(f'At {age} years old you pay 2 dollars (child rate).')
# elif age >= 9 and age < 65:
# 	print('At {} years old you pay 10 dollars (adult rate).'.format(age))
# elif age >= 65:
# 	print('At {} years old you pay 5 dollars (senior rate).'.format(age))

if not ((age >= 2 and age <= 8) or age >= 65 or age < 2):
	print('At {} years old you pay 10 dollars, full price.'.format(age))
elif age < 2:
	print(f'At {age} years old you get in for free!')
else:
	print('At {} years old you get a discount!'.format(age))

