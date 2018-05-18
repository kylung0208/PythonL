#請讀取輸入, 建立一個 dictionary 記錄班上的同學名字以及他們對應的歲數.

#然後寫一個函數 prAge(name), 如果 name 存在 dictionary, 印出名字和歲數, 否則印出 N/A, 
#例如: prAge('Bob') 印出 Bob 10, prAge('John') 印出 N/A

ages = {}
def prAge(name):
    if name in ages:     # Or we can type >>> if ages.get(name):
        print(name, ages.get(name))
    else:
        print('N/A')

def test():
    num = int(input())
    for i in range(0,num):
        line = input()
        tokens = line.strip().split()
        name = tokens[0]
        age = int(tokens[1])
        ages[name] = age
    print(ages)
    #print name and age
    num = int(input())
    for i in range(0,num):
        line = input()
        prAge(line)
test()