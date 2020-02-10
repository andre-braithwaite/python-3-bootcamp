from random import choice, randint

sides = ('heads', 'tails')


def flip_coin():
	return choice(sides)


print('Flipping 10 times!')
for i in range(10):
	print(flip_coin())