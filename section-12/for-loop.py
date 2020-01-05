colours = ['purple', 'teal', 'magenta', 'yellow', True, 42]

# Print list with for
for colour in colours:
	print(colour)

# Print list with while
i = 0
while i < len(colours):
	print('{}: {}'.format(i, colours[i]))
	i += 1