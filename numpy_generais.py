import numpy as np 
'''
mat1 = np.zeros((3,4))
print(mat1)
print(mat1.ndim)
print(mat1.shape)

mat2 = np.ones((3,3))*2
mat2_2 = mat2 * 2 
mat2_3 = mat2 * mat2_2
mat2_4 = np.matmul(mat2 , mat2_2)
#矩陣的乘法在numpy中要使用 np.matmul(矩陣一 , 矩陣二) ,記得兩個矩陣的行列要是符合運算的！！ 
#若只要單純乘起來的矩陣就用乘號 * 就好。
print(mat2)
print(mat2_2)
print(mat2_3)
print(mat2_4)

#對角化矩陣
mat3 = np.eye(3,3)
print(mat3)
print(mat2 * mat3)
print(np.matmul(mat2 , mat3))
'''

import matplotlib.pyplot as plt 
#隨機矩陣
arr_x = np.arange(10)
a = np.random.rand(10)
b = np.random.randint(5,10,10)
print(a)
print(b)
plt.plot(arr_x, a, '-r^', arr_x , b, '--go')
plt.show()