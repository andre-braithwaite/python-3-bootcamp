def sum_nums(*args):
	total = 0
	for i in args:
		total += i
	return total

print(sum_nums(1, 2, 3))