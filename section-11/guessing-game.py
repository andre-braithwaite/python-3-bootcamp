from random import randint

while True:
	answer = randint(1, 10)
	guesses = 1
	guess = int(input('Guess a number between 1 and 10: '))

	if guess == answer:
		print(f'Good guess first time! I was thinking of {answer}!')
	else:
		while guess != answer:	
			if guess > answer:
				clue = 'high'
			else:
				clue = 'low'

			print(f'Too {clue}...')
			guess = int(input('Guess again: '))
			guesses += 1

		print(f'Good job, I was thinking of {answer}!')
		print('You needed {} guesses.'.format(guesses))

	play_again = input('Would you like to play again? ')

	if play_again[0].lower() == 'n':
		print('Thanks for playing!')
		break
