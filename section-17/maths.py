def add(a, b):
	return f'{a} + {b} = {a + b}'

def subtract(a, b):
	return f'{a} - {b} = {a - b}'

def maths(a, b, op):
	return op(a, b)

print(maths(2, 3, add))
print(maths(7, 5, subtract))
print(maths(b = 2, op = add, a = 5))