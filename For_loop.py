#encoding:utf-8
def pr10():
    for i in range(0,11):
        print(i, end=' ')  #加上end=' '之後，原本預設print函數完就換行，就變成空白。
    print()

def prNums(n):
    for i in range(0,n+1):
        print(i, end=' ')
    print()

def print10(n):
    i = 0
    while i <= n:
        print(i, end = ' ')
        i += 1
    print()

def test():
    pr10()
    prNums(15)
    print10(10)

test()
