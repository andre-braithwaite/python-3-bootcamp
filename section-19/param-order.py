# params, *args, default params, **kwargs

def display_info(a, b, *args, instructor = 'Colt', **kwargs):
	print(type(args))
	return [a, b, args, instructor, kwargs]

output = display_info(1, 2, 3, last_name = 'Steele', job = 'instructor')
print(output)