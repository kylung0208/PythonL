#Tuple 裡面不一定是一樣類型的東西（不像Dictionary裡面都是一樣的物件），可能跟某個主題有關，其中的東西可以是不同的物件！
book1 = ("#010", "Stone Programming", 330)
(id1, title1, price1) = book1

book2 = "#025", "Python Programming", 230
id2, title2, price2 = book2
# book2 跟 book1一樣！ 兩種寫法都一樣，但上面那種比較清楚是tuple!!

print(book1)
print(book1[0],book1[1],book1[2])

print('以前用的enumerate函數其中的變數 idx 及 val 也是tuple!')
arr = [100, 200, 300]
for i in range(0,len(arr)):
    print(arr[i])
for idx, val in enumerate(arr):
    print(val)
for (idx, val) in enumerate(arr):  #較精準的tuple寫法
    print(val)