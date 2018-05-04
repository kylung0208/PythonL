#encoding:utf-8
#get input value from users

x = int(input('please enter a number: '))
y = int(input('please enter another number: '))

#set the upper boundary & lower boundary
if x < y:
	down = x
	up = y
else:
	up = x
	down = y

#start to the while loop for counting the down to the up, and see that if the number is dividable by 7 or 13
while down <= up:
	if (down % 7 == 0) and (down % 13 == 0):
		print(down)
	down += 1 #這個要放在 while loop 的下面，不是放在 if 的下面，不然不能形成迴圈！！！！