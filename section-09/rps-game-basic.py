print('''...rock...
...paper...
...scissors...\n''')

no_winner = True

while no_winner:
	p1_choice = input('Player 1, please enter rock, paper or scissors: ')
	p2_choice = input('Player 2, please enter rock, paper or scissors: ')

	if p1_choice == p2_choice:
		print(f'Draw! You both chose {p1_choice}')
	else:
		if p1_choice == 'rock' and p2_choice == 'paper':
				print('Player 2 wins! Paper wraps rock.')
		elif p1_choice == 'rock' and p2_choice == 'scissors':
				print('Player 1 wins! Rock breaks scissors.')
		elif p1_choice == 'paper' and p2_choice == 'rock':
				print('Player 1 wins! Paper wraps rock.')
		elif p1_choice == 'paper' and p2_choice == 'scissors':
				print('Player 2 wins! Scissors cut paper.')
		elif p1_choice == 'scissors' and p2_choice == 'rock':
				print('Player 2 wins! Rock breaks scissors.')
		elif p1_choice == 'scissors' and p2_choice == 'paper':
				print('Player 1 wins! Scissors cut paper.')
		else:
			print('something went wrong...')
			print('Player 1 entered {} and player 2 entered {}'.format(p1_choice, p2_choice))

		no_winner = False
		print('GAME OVER')

