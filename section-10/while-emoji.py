size = int(input('What size triangle am I printing? '))

# While loop
row = 1
while row <= size:
	print('*' * row)
	row += 1

# Nested while loop, poor solution
row = 1
while row <= size:
	count = 1
	stars = ''
	while count <= row: 
		stars += '*'
		count += 1
	print(stars)
	row += 1

# For loop
for i in range(size):
	print('*' * (i + 1))

# Nested for loops
for i in range(size):
	for j in range(i + 1):
		print('*', end = '')
	print('')