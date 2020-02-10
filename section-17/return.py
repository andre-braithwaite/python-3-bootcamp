def print_square_of_2():
	print(2 ** 2)

# print_square_of_2()

def square_2():
	print('I am before return')
	return 2 ** 2
	print('I am after return')

result = square_2()
print(result)