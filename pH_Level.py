#encoding:utf-8
#Allow users to input the pH level
pH_level = input('Enter a pH value: ')
pH = float(pH_level)

if len(pH_level) > 0:
	if pH < 0.0 or pH > 14.0 :
		print('Invalid pH value')
	if 0.0 <= pH < 5.0 :
		print('Strong acid')
	if 5.0 <= pH < 7.0 :
		print('Weak acid')
	if 7.0 <= pH < 8.0 :
		print('Neutral')
	if 8.0 <= pH < 10.0 :
		print('Weak base')
	if 10.0 <= pH <= 14.0 :
		print('Strong base')
else:
	print('No pH value given')
