#!/usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np
from sklearn.datasets import fetch_mldata
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA


mnist = fetch_mldata("MNIST original")

x,y = mnist["data"],mnist["target"]

X_train = np.array(x[:60000],dtype=float)
Y_train = np.array(y[:60000],dtype=float)
X_test = np.array(x[60000:],dtype=float)
Y_test = np.array(y[60000:],dtype=float)

knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train,Y_train)
knn_clf.score(X_test,Y_test)
#################
pca = PCA(0.9)
pca.fit(X_train)
X_train_reduction = pca.transform((X_train))
