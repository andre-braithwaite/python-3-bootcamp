print('WELCOME TO YOUR SHOPPING CART')
groceries = []

while True:
	item = input('Add something to the cart? Type q to quit: ')

	if item.lower() == 'q':
		break
	else:
		groceries.append(item)

print('YOUR FINAL GROCERY LIST')
for item in sorted(groceries):
	print('- {}'.format(item))

# 