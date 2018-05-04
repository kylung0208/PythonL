#首先印出九宮格，讓使用者參考
print(" 1 | 2 | 3 ")
print("---|---|---")
print(" 4 | 5 | 6 ")
print("---|---|---")
print(" 7 | 8 | 9 ")
print()
print("   |   |   ")
print("---|---|---")
print("   |   |   ")
print("---|---|---")
print("   |   |   ")
print()

is_O=True #is_O代表是否輪到O玩家
gameover=False #gameover代表遊戲是否結束
choice=[" "," "," "," "," "," "," "," "," "] #choice表示目前被O和X玩家選中的格子

def print_result(): #由於需要重複進行如下的列印，因此寫成一個沒有返回值的函數，可以供待會呼叫
	print(" "+ choice[0] + " | " + choice[1] + " | " + choice[2])
	print("---|---|---")
	print(" "+ choice[3] + " | " + choice[4] + " | " + choice[5])
	print("---|---|---")
	print(" "+ choice[6] + " | " + choice[7] + " | " + choice[8])
	print("   |   |   ")

#當遊戲沒有結束時，執行迴圈
while not gameover:
	if is_O==True: #若輪到O玩家，則存取O玩家的選擇，並判斷合法性
		n=int(input("(O) Select [1-9]: "))
		if n<1 or n>9: #若不是輸入1~9的數字，則不合法，要求重新輸入
			print("Invalid input. Try again.")
			continue
		else:
			if choice[n-1] !="O" and choice[n-1] !="X": #必須判斷當下的選擇是否已經被選過
				choice[n-1]="O"
				if choice[0] == "O" and choice[1] == "O" and choice[2] == "O": #37~76行是判斷O是否獲勝了
					print()
					print("Player O win!")
					print()
					print_result()
					break
				if choice[3] == "O" and choice[4] == "O" and choice[5] == "O":
					print()
					print("Player O win!")
					print()
					print_result()
					break
				if choice[6] == "O" and choice[7] == "O" and choice[8] == "O":
					print()
					print("Player O win!")
					print()
					print_result()
					break
				if choice[0] == "O" and choice[3] == "O" and choice[6] == "O":
					print()
					print("Player O win!")
					print()
					print_result()
					break
				if choice[1] == "O" and choice[4] == "O" and choice[7] == "O":
					print()
					print("Player O win!")
					print()
					print_result()
					break
				if choice[2] == "O" and choice[5] == "O" and choice[8] == "O":
					print()
					print("Player O win!")
					print()
					print_result()
					break
				if choice[0] == "O" and choice[4] == "O" and choice[8] == "O":
					print()
					print("Player O win!")
					print()
					print_result()
					break
				if choice[2] == "O" and choice[4] == "O" and choice[6] == "O":
					print()
					print("Player O win!")
					print()
					print_result()
					break
				#檢查完O有沒有贏之後，要檢查是不是已經和局了
				if choice[0] != " " and choice[1] != " " and choice[2] != " " and choice[3] != " " and choice[4] != " " and choice[5] != " " and choice[6] != " " and choice[7] != " " and choice[8] != " ":
					print()
					print("Tie. Bye~")
					print()
					print_result()
					break
				print_result()
				print()
			else:
				print("Cell",n,"has been filled. Try again.") #若當下要選的已經被選過了，則要求重新輸入
				continue
			is_O=False #每當O下完決定，is_O便轉換為False，如此來判斷該輪到X了
	else:
		n=int(input("(X) Select [1-9]: "))
		if n<1 or n>9: #若不是輸入1~9的數字，則不合法，要求重新輸入
			print("Invalid input. Try again.")
			continue
		else:
			if choice[n-1] !="O" and choice[n-1] !="X": #必須判斷當下的選擇是否已經被選過
				choice[n-1]="X"
				if choice[0] == "X" and choice[1] == "X" and choice[2] == "X": #91~130行是判斷O是否獲勝了
					print()
					print("Player X win!")
					print()
					print_result()
					break
				if choice[3] == "X" and choice[4] == "X" and choice[5] == "X":
					print()
					print("Player X win!")
					print()
					print_result()
					break
				if choice[6] == "X" and choice[7] == "X" and choice[8] == "X":
					print()
					print("Player X win!")
					print()
					print_result()
					break
				if choice[0] == "X" and choice[3] == "X" and choice[6] == "X":
					print()
					print("Player X win!")
					print()
					print_result()
					break
				if choice[1] == "X" and choice[4] == "X" and choice[7] == "X":
					print()
					print("Player X win!")
					print()
					print_result()
					break
				if choice[2] == "X" and choice[5] == "X" and choice[8] == "X":
					print()
					print("Player O win!")
					print()
					print_result()
					break
				if choice[0] == "X" and choice[4] == "X" and choice[8] == "X":
					print()
					print("Player X win!")
					print()
					print_result()
					break
				if choice[2] == "X" and choice[4] == "X" and choice[6] == "X":
					print()
					print("Player X win!")
					print()
					print_result()
					break
				#檢查完X有沒有贏之後，要檢查是不是已經和局了
				if choice[0] != " " and choice[1] != " " and choice[2] != " " and choice[3] != " " and choice[4] != " " and choice[5] != " " and choice[6] != " " and choice[7] != " " and choice[8] != " ":
					print()
					print("Tie. Bye~")
					print_result()
					break
				print_result()
				print()
			else:
				print("Cell",n,"has been filled. Try again.") #若當下要選的已經被選過了，則要求重新輸入
				continue
			is_O=True #X下完之後，is_O又變為True，又回到O玩家下，如此重複直到雙方有人勝出或平手為止。

	