#encoding:utf-8

'''
from pylab import * #引入兼容MATLAB包: pylab

#準備一些數據，注意和MATLAB不同！
t1 = arange(0.0, 4.0, 0.1)
t2 = arange(0.0, 4.0, 0.05)

figure
#第一個子圖211
subplot(211)

plot(t1 , sin(2*pi*t1) , '--g*')
title('sine function demo')
xlabel('time(s)')
ylabel('voltage(mV)')
xlim([0.0 , 5.0]) #注意裡面還要一個鐘括弧把上下界定義出來！
ylim([-1.2 , 1.2])

grid('on') #控制網格顯示和grid(True)一樣。不帶參數的grid起到toggle作用。

#第二個子圖212
subplot(212)

plot(t2 , exp(-t2) , ':r'
hold('on') #前一條線保持，用法和grid類似
plot(t2 , cos(2*pi*t2) , '--b')
xlabel('time')
ylabel('amplitude')

show
###不知哪裡錯了###
'''

import pylab as pl  #引入pylab為matplotlib的一個子包。或是直接 import matplotlib as plt 也可以。

x = range(10) #橫軸數據
y = [ i*i for i in x ] #縱軸數據

pl.plot(x,y) #調用pyplot的plot函數繪製曲線

#設定x,y邊界
pl.xlim(-5 , 15) 
pl.ylim(-10, 100)

#設定標題與x,y軸名稱
pl.xlabel('xlabel')
pl.ylabel('ylabel')
pl.title('The title')

#在此之前都還在「畫圖」，經過這個步驟才會「秀圖」，不然只會跑程式，但沒有圖跑出來。
pl.show() #顯示繪製出的圖，記得show後面要打***括弧***



























