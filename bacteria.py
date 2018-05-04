#encoding:utf-8
#給定初始時間
t = 0
#給定初始病毒數
pop = 1000
#給定成長率
r = 0.21

#進入迴圈
while pop < 2000:
	pop += pop * r
	print(pop)
	t += 1
print('Took',t,'minutes for the bacteria to double')
print('And the final population is',pop)