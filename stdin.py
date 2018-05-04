#若不知道所要讀取的檔案有幾筆資料 --> 使用stdin
import sys
def readInput():
  for line in sys.stdin:
    print(line)

readInput()