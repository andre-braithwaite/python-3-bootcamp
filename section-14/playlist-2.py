playlist = {
	'title': 'patagonia bus', 
	'author': 'dj steele', 
	'songs': [
		{'title': 'first song', 'artist': ['blue', 'green'], 'duration':2.5},
		{'title': 'second song', 'artist': ['red'], 'duration':1.5},
		{'title': 'third song', 'artist': ['yellow', 'magenta'], 'duration':3.5}
	]
}

total_duration = 0

for song in playlist['songs']:
	print(song['duration'])
	total_duration += song['duration']

print(f'The total duration is: {total_duration} seconds')