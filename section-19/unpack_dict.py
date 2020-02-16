def display_names(first, second):
	return f'{first} says hello to {second}'

names = {'first': 'Andre', 'second': 'Marc'}
print(names)
print(names['first'])
print(names.get('second'))
print(display_names(**names)) # Unpacks into 2 separate keyword arguments (first='Andre', second='Marc')


print('Add and Multiply numbers')

def add_mult(a, b, c, **kwargs): #kwargs picks up keyword arguments after a, b and c
	print('Other Stuff...')
	print(kwargs)
	return a + b * c

data = dict(a = 1, b = 2, c = 3, d = 55, e = 56)

print(add_mult(**data, cat = 'Awesome'))