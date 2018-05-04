#encoding:utf-8
accusation = {'room':'ballroom', 'weapon':'lead pipe', 'person':'Col. Mustard'}

for card in accusation:
	print(card)
print('')
for value in accusation.values(): #要迭代字典裡面的值，使用'values()'涵式。“字典裡沒有value涵式！！！”
	print(value)
print()
for item in accusation.items(): #要迭代字典裡面的'鍵'與'值'，使用items涵式。
	print(item)

#使用 zip() 函式來迭代多個序列
days = ['Monday','Tuesday','Wendsday']
fruits = ['banana','apple','peach']
drinks = ['coffee','tea','beer']
desserts = ['tiramisu','ice cream','pie','pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
	print(day,': drink', drink, '- eat', fruit, '- enjoy', dessert)

print('')

# zip 來配對 tuple！
# zip 回傳的值不是 tuple 或 串列，而是一個可迭代的合併值
english = 'Monday', 'Tuesday', 'Wendsday'
French = 'Lundi', 'Mardi', 'Mercredi'

print( list( zip(english,French) ) )
print( dict( zip(english,French) ) )