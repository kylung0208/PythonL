#encoding:utf-8
'''
	測試使用者輸入的數字(>1)是不是質數。
	測試方法：輸入數字除以1到自己，如果只有兩個可以整除 -->  質數
	                          若不止兩個整除 --> 不為質數
'''
while True:
	num = int(input('please enter an integer (>1): '))
	if num <= 1:
		print('Wrong input integer! -- try again')
	else:
		break
div = 2
total_div = 1

while num > 1:
	if num % div == 0 :
		total_div += 1
	div += 1
	if div > num:
		break

if total_div > 2:
	print(num,'is a NOT prime number.')
if total_div == 2:
	print(num,'is a prime number.')