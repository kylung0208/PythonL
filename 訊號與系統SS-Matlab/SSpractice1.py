#encoding:utf-8
import numpy as np 
a_ran = np.random.random((5))
print(a_ran)

#陣列輸出隨機整數數字0~1
b_ran = np.random.randint(0,2,(5))
print(b_ran)
print(np.bincount(b_ran)) #要算矩陣內各個元素出現次數要用 np.bincount()

#SS作業1
s = np.random.randint(0,2,(500))
print(s)
print(np.bincount(s))
