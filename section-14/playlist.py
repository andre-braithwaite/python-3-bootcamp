# Some data modelling

song_a = dict(name = 'The A Song', artists = ['A Team', 'A+ Team'], album = 'That A Album', duration = '3:37')
song_b = dict(name = 'The B Song', artists = ['B Team'], album = 'That B Album', duration = '2:22')
song_c = dict(name = 'The C Song', artists = ['C Team'], album = 'That C Album', duration = '4:44')

playlist = dict(name = 'Awesome Mix 2', author = 'Doc Dre', songs = [song_a, song_b, song_c])



print(playlist)

for song in playlist['songs']:
	artists = ', '.join(song["artists"])
	print(f'{song["name"]} by {artists}')