print('''...rock...
...paper...
...scissors...\n''')

no_winner = True
ok_response = ['rock', 'paper', 'scissors']
p1_choice, p2_choice = None, None

while no_winner:
	while not (p1_choice in ok_response and p2_choice in ok_response):
		p1_choice = input('Player 1, please enter rock, paper or scissors: ')
		print('NO CHEATING!\n' * 20)
		p2_choice = input('Player 2, please enter rock, paper or scissors: ')

	if p1_choice == p2_choice:
		print(f'Draw! You both chose {p1_choice}')
		p1_choice, p2_choice = None, None
	else:
		if p1_choice == 'rock':
			if p2_choice == 'paper':
				print('Player 2 wins! Paper wraps rock.')
			elif p2_choice == 'scissors':
				print('Player 1 wins! Rock breaks scissors.')
		
		elif p1_choice == 'paper':
			if p2_choice == 'rock':
				print('Player 1 wins! Paper wraps rock.')
			elif p2_choice == 'scissors':
				print('Player 2 wins! Scissors cut paper.')
		
		elif p1_choice == 'scissors':
			if p2_choice == 'rock':
				print('Player 2 wins! Rock breaks scissors.')
			elif p2_choice == 'paper':
				print('Player 1 wins! Scissors cut paper.')
		else:
			print('something went wrong...')
			print('Player 1 entered {} and player 2 entered {}'.format(p1_choice, p2_choice))

		no_winner = False
		print('GAME OVER')

