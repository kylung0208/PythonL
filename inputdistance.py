### Let's go coding ###
#get strings from input
input_x1 = input("please enter x1: ")
input_y1 = input('please enter y1: ')
input_x2 = input('please enter X2: ')
input_y2 = input('please enter y2: ')

#convert the input string to float
x1 = float(input_x1)
y1 = float(input_y1)
x2 = float(input_x2)
y2 = float(input_y2)

#give the formula of diatance
dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

#print out the ans of diatance
print('the distance between', '(', x1,',',y1,')','and', '(', x2,',',y2,')','is:',dist)

'''
下次應該要在給定距離公式之前先多設定兩個變數代表 dist_x = (x2-x1)及 dist_y = (y2-y1)
然後再帶入公式中變成
dist = (dist_x ** 2 +dist_y ** 2) ** 0.5
這樣是比較好的寫程式表示法！！！
'''
