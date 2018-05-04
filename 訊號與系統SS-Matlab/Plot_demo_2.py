#encoding:utf-8
#導入數據包
import pylab as pl 
import numpy as np

#設定三組數據
x1 = np.arange(0,360,5)
y1 = np.sin(2 * np.pi * x1 / 360)

x2 = x1
y2 = np.cos(2 * np.pi * x2 / 360)

x3 = x1 
y3 = np.tan(2 * np.pi * x3 / 360)

#繪圖
pl.plot(x1 , y1 , lw = 3)
pl.plot(x2 , y2 , 'ro')
pl.plot(x3 , y3 , 'y--' , lw = 5)

#設定xy軸名稱及標題
pl.xlabel('Label_x')
pl.ylabel('Label_y')
pl.title('My Title')

#設定上下界
pl.xlim(-30 , 390)
pl.ylim(-5 , 5)

#秀圖
pl.show()












