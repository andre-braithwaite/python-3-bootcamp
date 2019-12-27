conversion = 1.60934
print('How many miles did you run?')
miles = input() # changes prompt in command line
km = round( (float(miles) * conversion), 2)
print(f'Wow! {miles} miles is pretty decent!')
print('Your {} mile run is equal to {}km'.format(miles, km))