if 3>2:
	print('It works!')
	if 5<2:
		print('5 is indeed greater than 2')
	else:
		print('5 is not greater than 2')
		name = 'bev'
		if name =='vimbai':
			print('Hey vimbai!')
		elif name =='viviene':
			print('Hey viviene!')
		else:
			print('Hey anonymous!')
			volume = 157
			if volume< 20:
				print("Its kinda quiet.")
			elif 20<= volume < 40:
				print("Its nice for background music")
			elif 40<= volume < 60:
				print("Perfect, I can hear all the details")
			elif 60<= volume < 80:
				print("Nice for parties")
			elif 80<= volume <100:
				print("A bit loud")
			else:
				print("My ears are hurting! :(")
				if volume < 20 or volume > 80:
					volume = 50
					print("That's better!")
