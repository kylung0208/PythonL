from sklearn.datasets import load_digits
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

digits = load_digits()

# split the data into training and validation sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

# train the model
clf = GaussianNB()
clf.fit(X_train, y_train)
GaussianNB(priors=None)

# use the model to predict the labels of the test data
predicted = clf.predict(X_test)
expected = y_test
print(predicted) 
# [1 7 7 7 8 2 8 0 4 8 7 7 0 8 2 3 5 8 5 3 7 9 6 2 8 2 2 7 3 5...]
print(expected) 
# [1 0 4 7 8 2 2 0 4 3 7 7 0 8 2 3 4 8 5 3 7 9 6 3 8 2 2 9 3 5...]

matches = (predicted == expected)
print(matches.sum())
# 367
print(len(matches))
# 450
matches.sum() / float(len(matches))
# 0.81555555555555559

from sklearn import metrics
print(metrics.classification_report(expected, predicted))

print(metrics.confusion_matrix(expected, predicted))