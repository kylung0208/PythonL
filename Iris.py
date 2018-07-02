'''
from sklearn.datasets import load_iris
iris = load_iris()

#iris.data :  花托長寬 與 花瓣長寬 資料

print(iris.data.shape)                   # (150, 4) :150朵花已知品種及資料，用來訓練model
n_samples, n_features = iris.data.shape
print(n_samples)                         # 150
print(n_features)                        # 4
print(iris.data[0])                      # [5.1 3.5 1.4 0.2]

print(iris.target.shape)  # (150,)
print(iris.target)

#[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2]

print(iris.target_names)   # ['setosa' 'versicolor' 'virginica']
'''
# Load the data
from sklearn.datasets import load_iris
iris = load_iris()

from matplotlib import pyplot as plt

# The indices of the features that we are plotting
#更改這邊的數字可以選擇兩種不同的特性來做圖
x_index = 1
y_index = 2

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.figure(figsize=(5, 4))
plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

plt.tight_layout()
plt.show()