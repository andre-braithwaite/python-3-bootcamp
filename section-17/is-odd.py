def is_odd_number(num):
	if num % 2 != 0:
		return True
	return False
	# note that an else clause is not required, more concise

print(f'Is 1 odd? {is_odd_number(1)}')
print(f'Is 2 odd? {is_odd_number(2)}')
print(f'Is 3 odd? {is_odd_number(3)}')
print(f'Is 4 odd? {is_odd_number(4)}')
