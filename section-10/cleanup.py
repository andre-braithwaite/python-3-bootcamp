num = int(input('How many times do I have to tell you? '))

for i in range(num):
	print(f'time {i + 1}: CLEAN UP YOUR ROOM!')

print('')

# Without a for loop
print('CLEAN UP YOUR ROOM!\n' * num) 