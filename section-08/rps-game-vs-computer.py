from random import choice, randint

print('''...rock...
...paper...
...scissors...\n''')
# print(randint(1, 3))
# print(randint(1, 3))
# print(randint(1, 3))
# randint is inclusive
no_winner = True
ok_response = ['rock', 'paper', 'scissors']
player_choice, computer_choice = None, None

while no_winner:
	while not (player_choice in ok_response):
		player_choice = input('Player, please enter rock, paper or scissors: ').lower()
				
		if player_choice in ok_response:
			computer_choice = choice(ok_response)
			print(f'The Computer chose... {computer_choice}!')

	if player_choice == computer_choice:
		print(f'Draw! You both chose {player_choice}')
		player_choice, computer_choice = None, None
	else:
		if player_choice == 'rock':
			if computer_choice == 'paper':
				print('Computer wins! Paper wraps rock.')
			else:
				print('Player wins! Rock breaks scissors.')
		
		elif player_choice == 'paper':
			if computer_choice == 'rock':
				print('Player wins! Paper wraps rock.')
			elif computer_choice == 'scissors':
				print('Computer wins! Scissors cut paper.')
		
		elif player_choice == 'scissors':
			if computer_choice == 'rock':
				print('Computer wins! Rock breaks scissors.')
			elif computer_choice == 'paper':
				print('Player wins! Scissors cut paper.')
		else:
			print('something went wrong...')
			print('Player entered {} and Computer entered {}'.format(player_choice, computer_choice))

		no_winner = False
		print('GAME OVER')

