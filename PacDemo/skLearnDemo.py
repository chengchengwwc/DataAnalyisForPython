#!/usr/bin/env python
# -*- coding:utf-8 -*-


import  numpy as np

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split


digits = datasets.load_digits()

x = digits.data

y = digits.target

X_train,X_test,y_train,y_test = train_test_split(x,y,random_state=0.6)
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train,y_train)
knn_clf.score(X_test,y_test)

pca = PCA(n_components=2)

pca.fit(X_train)
X_train_reduction = pca.transform(X_train)
X_test_reduction  = pca.transform(X_test)






