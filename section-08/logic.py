choice = input('What\'s your favourite colour?\n')
if choice.lower() == 'blue':
	print(f'{choice} is my favourite colour too!')
elif choice.lower() == 'red':
	print('{} is soo predictable but ok...'.format(choice))
elif choice.lower() == 'green':
	print(choice[0].upper() + choice.lower()[1:] + ' is your favourite colour? I guess it could\'ve been worse')
else:
	print(f'Seriously?! {choice}? What are you thinking!')