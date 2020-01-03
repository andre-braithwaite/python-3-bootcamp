size = int(input('How many pyramid rows am I printing? '))

# While loop
row = 1
while row <= size:
	print((' ' * (size - row)) + ('*' * (row * 2 - 1)))
	row += 1

# Nested while loop, poor solution
row = 1
while row <= size:
	count = 1
	spaces = ' ' * (size - row)
	stars = ''
	while count <= (row * 2 - 1): 
		stars += '*'
		count += 1
	print(spaces + stars)
	row += 1

# # For loop
# for i in range(size):
# 	print('*' * (i + 1))

# # Nested for loops
# for i in range(size):
# 	for j in range(i + 1):
# 		print('*', end = '')
# 	print('')