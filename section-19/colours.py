def fav_colours(**kwargs):
	for k, v in kwargs.items():
		print('{}\'s favourite colour is {}!'.format(k, v))

fav_colours(andre='red', marc='green', colin='blue')