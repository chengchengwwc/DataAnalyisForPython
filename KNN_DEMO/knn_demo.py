#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn.model_selection import  train_test_split
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm






digits = load_digits()

data = digits.data

#数据探索
print (data.shape)
#加载第一幅图
print (digits.images[0])
#图像代表的数字意义
print (digits.target[0])
plt.gray()
plt.imshow(digits.images[0])
plt.show()

#分割数据 将25%的数据作为测试集，其他的作为训练集
train_x,test_x,train_y,test_y = train_test_split(data,digits.target,test_size=0.25,random_state=33)

#采用Z-Score规范化
ss = preprocessing.StandardScaler()
train_x = ss.fit_transform(train_x)
test_x  = ss.fit_transform(test_x)

#创建 KNN分类器
knn = KNeighborsClassifier()
knn.fit(train_x,train_y)
predict_y = knn.predict(test_x)
print(accuracy_score(predict_y,test_y))

#创建SVM分类器
svm_ = svm.SVC()
svm_.fit(train_x,train_y)
predict_y = svm_.predict(test_x)
print (accuracy_score(predict_y,test_y))






