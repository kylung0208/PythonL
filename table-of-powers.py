#encoding:utf-8
f = open('Table-of-powers.txt','w')
LIMIT = 10 #程式不要寫死！！！如過要變更最大值就只要改變LIMIT這個變數就好。
header = 'Table of powers from 1 to %d\n' % LIMIT
bar = '=' * len(header) + '\n\n' #也是一個使bar對齊標題的排版方式。

f.write(header)
f.write(bar)

#use loop to generate the powers from 1 to LIMIT
for n in range(1, LIMIT+1):
	f.write('%3d    %5d    %5d\n'%(n, n**2, n ** 3)) #如過要輸出一個比較工整的格式，建議使用 % 
f.close()