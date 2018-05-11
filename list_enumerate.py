'''
problem 1
'''
#函數 prList(arr), 輸入值 arr 是一個 list, 將其中每個元素印出, 用逗號分隔
#例如: prList([10, 20, 30, 40, 50]) 印出 10, 20, 30, 40, 50

a = [10,20,30,40,50]
def prList(arr):
    #index is last one , then println. otherwise,","
    for idx,el in enumerate(arr):
        if (idx != len(arr)-1):
            print(el,end=",")
        else:
            print(el)
b = [30,4,56]
print(prList(a))
print(prList(b))

'''
prob 2
'''
#函數 enumList(arr), 輸入值 arr 是一個 list, 請將其中每個元素分行印出, 並在那一行的最前面加上編號.
#例如: enumList(['apple', 'orange', 'banana']) 會印出:
#1. apple
#2. orange
#3. banana
def enumList(arr):
    for idx,el in enumerate(arr):
        print(idx+1,'. ',el)
enumList(['apple', 'orange', 'banana'])

# we can also use 'Format' !!
def enumList2(arr):
    for idx,el in enumerate(arr):
        print("{}. {}".format(idx+1,el))
enumList2(['apple','orange','banana'])