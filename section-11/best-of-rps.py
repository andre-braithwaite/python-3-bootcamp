from random import choice, randint

print('''...rock...
...paper...
...scissors...\n''')

best_of = int(input('What shall play best of? '))
ok_response = ['rock', 'paper', 'scissors']

player_choice = None
player_score = 0
computer_score = 0
forfeit = False
player_choice, computer_choice = None, None

while ( (player_score + computer_score) < best_of and forfeit == False):
	while not (player_choice in ok_response):
		player_choice = input('Player, please enter rock, paper or scissors: ').lower()
		
		if player_choice[0] == 'q':
			forfeit = True
			break		

		if player_choice in ok_response:
			computer_choice = choice(ok_response)
			print(f'The Computer chose... {computer_choice}!')

	if player_choice == computer_choice:
		print(f'Draw! You both chose {player_choice}')
	else:
		if player_choice == 'rock':
			if computer_choice == 'scissors':
				print('Player wins! Rock breaks scissors.')
				player_score += 1
			else:
				print('Computer wins! Paper wraps rock.')
				computer_score += 1
		
		elif player_choice == 'paper':
			if computer_choice == 'rock':
				print('Player wins! Paper wraps rock.')
				player_score += 1
			else:
				print('Computer wins! Scissors cut paper.')
				computer_score += 1
		
		elif player_choice == 'scissors':
			if computer_choice == 'paper':
				print('Player wins! Scissors cut paper.')
				player_score += 1
			else:
				print('Computer wins! Rock breaks scissors.')
				computer_score += 1
		else:
			print('something went wrong...')
			print('Player entered {} and Computer entered {}'.format(player_choice, computer_choice))

	player_choice, computer_choice = None, None
	print('#### SCORE ####\nPlayer: {} Computer {}'.format(player_score, computer_score))

if player_score == computer_score:
	print('The series ended in a draw. {} : {}'.format(player_score, computer_score))
elif player_score > computer_score:
	print(f'You won the series {player_score} : {computer_score}!')
else:
	print(f'The computer whooped your sorry butt {computer_score} : {player_score}... Ouch.')

if forfeit == True:
	print('You gave up!')
print('\nGAME OVER')
