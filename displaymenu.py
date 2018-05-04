#encoding:utf-8
print('Welcome to the nature center. What would you like to do?')
print('')

while True: #或用 while choise != 'q'
	print('[1]Enter 1 to take a bicycle ride.')
	print('[2]Enter 2 to go for a run.')
	print('[3]Enter 3 to climb a mountain.')
	print('[q]Enter q to quit.')
	print('')
	choise = input('What would you like to do?')
	if choise == '1':
		print('Here is a bicycle. Have fun!')
		print('')
	elif choise == '2':
		print('Here are some runiing shoes. Run fast!')
		print('')
	elif choise == '3':
		print('Here is a map. Can you leave a trip plan for us?')
		print('')
	elif choise == 'q':
		print('Thanks for playing. See you later!')
		break
	else:
		print('Wrong input -- try again')