#encoding:utf-8
import numpy as np
#practice1
x = np.random.random((10))
print(x)
print(np.max(x))
print(np.min(x))

y = np.random.random((4,5))
print(y)
print(np.max(y))
print(np.argmax(y))
print(np.where(y == np.max(y)))