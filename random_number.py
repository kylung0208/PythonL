#encoding:utf-8
import random
print(random.random()) #在[0,1)之間選取數字（小數）
print(random.uniform(-1, 1)) #在[-1,1)之間選取隨機數字（小數）
#不能在Random的框框裡面輸入兩個數字，要使用uniform : print(random.random(-1, 1)) --- Wrong!!!

print(random.randint(1, 10)) #在[1, 10)之間選取‘整數’
print(random.randint(0, 100))

suits = ['Club', 'Diamond', 'Heart', 'Spade']
print(random.choice(suits))
index = random.randint(0, len(suits)-1)
print(suits[index])
print('\n')
#another way to get random element from suits
random.shuffle(suits) #洗牌
print(suits[0])