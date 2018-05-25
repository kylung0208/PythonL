def readInput():
    line1 = input()
    line2 = input()
    line3 = input()
    num1 = int(line1)
    num2 = int(line2)
    num3 = int(line3)
    print(num1 + 1)
    print(num2 + 1)
    print(num3 + 1)

def readInput2():
    line = input()
    cnt = int(line)
    for i in range(0,cnt):
        line = input()
        num = int(line)
        print(num + 1)

print()

readInput2()

#若要從另一個已經打好的txt檔案輸入input，則在終端機打上 python3 numbers.py < testnumber.txt
#注意：input指令讀取的是一行！！
#注意：從另一個檔案讀取資料不能一次執行兩個read function！ 會亂掉

#readInput2 Function所讀取的檔案在第一行的資料要是：下面總共有幾筆資料。