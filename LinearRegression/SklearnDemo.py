#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Sklean demo
"""
线性回归对数据具有可解释性
"""

import  numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV


boston = datasets.load_boston()
x = boston.data
y = boston.target
plt.scatter(x,y)
plt.show()

X_train,X_test,y_train,y_test = train_test_split(x,y,random_state=33)
lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)
lin_reg.score(X_test,y_test)

# KNN Regressor
knn_reg = KNeighborsRegressor()
knn_reg.fit(X_train,y_train)
knn_reg.score(X_test,y_test)


param_grid = [
    {
        "weights":["uniform"],
        "n_neighbors":[i for i in range(1,11)]
    },
    {
        "weights":["distance"],
        "n_neighbors":[for i in range(1,11)],
        "p":[i for i in range(1,6)]
    }
]
knn_new_reg = KNeighborsRegressor()
grid_search = GridSearchCV(knn_new_reg,param_grid,n_jobs=-1,verbose=1)
grid_search.fit(X_train,y_train)







