#encoding:utf-8
#給使用者輸入成績
x1 = input('John\'s grade: ')
x2 = input('Mary\'s grade: ')
x3 = input('Alice\'s grade: ')
x4 = input('Oliver\'s grade: ')
x5 = input('Eric\'s grade: ')

#把input的string轉成float
flo_x1 = float(x1)
flo_x2 = float(x2)
flo_x3 = float(x3)
flo_x4 = float(x4)
flo_x5 = float(x5)

#設定我想要的格式
my_format_title = '|%-10s|%10s|%10s|'
my_format = '|%-10s|%10s|%10.2f|'

#輸出標題及成績
print(my_format_title % ('Name','Gender','Score'))
print(my_format % ('John','M',flo_x1))
print(my_format % ('Mary','F',flo_x2))
print(my_format % ('Alice','F',float(x3)))
print(my_format % ('Oliver','M',float(x4)))
print(my_format % ('Eric','M',float(x5)))
