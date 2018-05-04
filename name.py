#encoding:utf-8
name = 'Henny'
name2 = name.replace('H','P')
print(name, name2)
print(name.replace('H','P'))
print(name)
print(name2)

'''
注意：name.replace('H','P')是一個新的變數，不會改變原本的name變數。
'''

name3 = 'P' + name[1:]
print(name3)
name4 = 'K' + name.replace('H','P')[1:]   #name4 = 'K' + name2[1:]
print(name4)
