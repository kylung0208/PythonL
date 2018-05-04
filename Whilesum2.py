#encoding:utf-8
#give initial values to variables
total = 0
num = 0
yes_no = False

#While loop for entering values and (y/n)
while not yes_no:
    num = int(input('Please enter a number: '))
    boo = input('Do you want another?(y/n): ')
    if boo == 'y' or boo == 'yes': #這邊不能打 if boo == 'y' or 'yes' ，會變成所有的輸入值都直接迴圈。'Kind of weird...'
    	total += num 
    	yes_no = False
    else:
    	total += num
    	yes_no = True

print('The resent total value is %d ' %total )