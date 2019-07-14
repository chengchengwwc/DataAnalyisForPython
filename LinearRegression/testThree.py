#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 多元线性回归

import numpy as np
from sklearn.preprocessing import StandardScaler #归一化处理




class LinearRegression:

    def __init__(self):
        self.coef_ = None
        self.interception_ = None
        self._theta   = None


    def fit_normal(self,X_train,y_train):
        assert X_train.shape[0] == y_train.shape[0],\
        "the size of X_train must be equal to the size of y_train"
        X_b = np.hstack([np.ones(len(X_train),1),X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        self.interception_ = self._theta[0]
        self.coef_ = self._theta[1:]
        return self


    def dj(self,theta,X_b,y):
        return X_b.T.dot(X_b.dot(theta) - y) * 2











    def predict(self,X_predict):
        assert self.interception_ is not None and self.coef_ is not None,\
        "Must fit before predict"
        assert X_predict.shape[1] == len(self.coef_),\
        "The feature number o X_predict must be equal to X_train"
        X_b = np.hstack([np.ones(len(X_predict), 1), X_predict])
        return X_b.dot(self._theta)

    def mean_squared_error(self,y_true, y_predict):
        assert len(y_true) == len(y_predict), \
            "the size of y_true must be equal to the size of y_predict"

        return np.sum((y_true - y_predict) ** 2) / len(y_true)

    def r2_score(self,y_true, y_predict):
        return 1 - self.mean_squared_error(y_true, y_predict) / np.var(y_true)


    def score(self,X_test,y_test):
        """
        比较结果
        :param X_test:
        :param y_test:
        :return:
        """
        y_predict = self.predict(X_test)
        return self.r2_score(y_test,y_predict)


    def __repr__(self):
        return "LinearRegression()"




def test(X_train):
    standarScaler = StandardScaler()
    standarScaler.fit(X_train)
    X_train.standard = standarScaler.transform(X_train)





