#encoding:utf-8
def getnums():
	#create a list from user input
	nums = []
	while 1:
		xstr = input('Enter a number: ')
		if xstr == 'q':
			break
		nums.append(eval(xstr))
	return nums

def average(lst):
	#compute the average of a given list
	sum = 0.0
	for num in lst:
		sum += num
	return sum / len(lst)

#main
data = getnums()
print('Average = ', average(data))
