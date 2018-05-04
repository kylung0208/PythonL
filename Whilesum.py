#encoding:utf-8
total = 0
num = 0

while num != -1:
	num = int(input('Please enter the number: '))
	if num != -1:
		total = total + num 

print('Total is %d' % total)