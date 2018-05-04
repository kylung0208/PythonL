#encoding:utf-8
import numpy as np 
array1 = np.array([[1,2,3],
	               [4,5,6],
	               [7,8,9]])
print(array1)
print('number of dimention: ', array1.ndim ) #代表此矩陣為二維，並非線性
print('shape: ', array1.shape ) #代表此矩陣之高,長
print('size: ',array1.size ) #代表此矩陣中有多少元素

#全部為零矩陣
a = np.zeros( (3,4) )
print(a)

#全部為一矩陣
b = np.zeros( (3,4) )
print(b)

#生成一個數列
c = np.arange(10,20,2)
print(c)

#生成數列轉為3*4矩陣
d = np.arange(12).reshape( (3,4) )
print(d)

#另一個矩陣
array2 = np.array([[9,8,7],
	               [6,5,4],
	               [3,2,1]])
print(array2)

#矩陣加減法
print(array2 - array1)

#矩陣平方
print(array1 ** 2)

#將矩陣變成sin值，再乘倍數
x = 10 * np.sin(array1)
print(x)

#矩陣乘法分兩種，一種是逐個相乘(*)，另一種是一般的矩陣運算要用np.dot(a,b)
multiply = array1 * array2 #逐個相乘
dot = np.dot( array1,array2 ) #矩陣相乘
dot2 = array1.dot(array2) #另一種矩陣相乘表示法

print(multiply)
print(dot)
print(dot2)

#矩陣的對角線交換Transpose
print(np.transpose(array1))
print(array1.T)

#反矩陣inverse（錯誤！！！！！）
array1_inverse = array1 ** -1
print(array1_inverse)
print( array1_inverse.dot(array1) )

#據陣行列式值
m = np.matrix([[1,1],
	           [2,4]])
print(np.linalg.det(m))

#反矩陣inverse（正確！！！！！）
print(np.linalg.inv(m))
print(np.linalg.inv(m).dot(m)) #單位矩陣






