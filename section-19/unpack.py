def sum_all_values(*args):
	total = 0
	for num in args:
		total += num
	print(total)

nums = [*{1, 2}, 3, 4, 5,*[6]]
print(nums)
print(type(nums))
sum_all_values(*nums)

# *before a collection to unpack into a sequence of individual arguments to pass into a function