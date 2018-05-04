#encoding:utf-8
#給輸入者的提醒標題
print('Change Counter')
print('Please enter the count of each coin type.')

#由使用者方取得各硬幣種類數量
Quarters_str = input('Quarters: ')
Dimes_str = input('Dimes: ')
Nickels_str = input('Nickels: ')
Pennyies_str = input('Pennies: ')

#將輸入的字串換成浮點數
Quarters = float(Quarters_str)
Dimes = float(Dimes_str)
Nickels = float(Nickels_str)
Pennies = float(Pennyies_str)

#計算硬幣總額
count_total = Quarters*0.25 + Dimes*0.1 + Nickels*0.05 + Pennies*0.01

#輸出硬幣總額結果
print('The total value of your change is $%.2f' % (count_total))