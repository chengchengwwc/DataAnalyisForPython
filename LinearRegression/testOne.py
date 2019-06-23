#!/usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


class SimpleLinearRegression1():

    def __init__(self):
        self.a_ = None
        self.b_ = None


    def fit(self,x_train,y_train):
        assert x_train.ndim == 1,\
        "Simple Linnar Regressor can only solve single feature training data"
        assert len(x_train) == len(y_train),\
        "the size of x_train must be equal to the size of y_train"

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0
        d   = 0.0
        for x,y in zip(x_train,y_train):
            num += (x - x_mean) * (y -y_mean)
            d   += (x - x_mean) **2

        self.a_ = num/d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self,x_predict):
        assert x_predict.ndim == 1,\
        "Simple Linear Regressor can only solve single feature training data"
        assert self.a_ is not None and self.b_ is not None,\
        "Must fit before prefict"

        return np.array([self._predict(x) for x in x_predict])


    def _predict(self,x_single):
        return self.a_ * x_single + self.b_


    def __repr__(self):
        return "SimpleLinearRegression1()"



class SimpleLinearRegression2():

    def __init__(self):
        self.a_ = None
        self.b_ = None


    def fit(self,x_train,y_train):
        assert x_train.ndim == 1,\
        "Simple Linnar Regressor can only solve single feature training data"
        assert len(x_train) == len(y_train),\
        "the size of x_train must be equal to the size of y_train"

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        #向量计算
        num = (x_train - x_mean).dot(y_train - y_mean)
        d   = (x_train - x_mean).dot(x_train -x_mean)


        self.a_ = num/d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self,x_predict):
        assert x_predict.ndim == 1,\
        "Simple Linear Regressor can only solve single feature training data"
        assert self.a_ is not None and self.b_ is not None,\
        "Must fit before prefict"

        return np.array([self._predict(x) for x in x_predict])


    def _predict(self,x_single):
        return self.a_ * x_single + self.b_


    def __repr__(self):
        return "SimpleLinearRegression2()"



def mean_squared_error(y_true,y_predict):
    assert len(y_true) == len(y_predict),\
        "the size of y_true must be equal to the size of y_predict"

    return np.sum((y_true -y_predict)**2)/len(y_true)


def root_mean_squared_error(y_true,y_predict):
    return sqrt(mean_squared_error(y_true,y_predict))


def mean_absoult_error(y_true,y_predict):
    assert len(y_true) == len(y_predict),\
    "the size of y_true must be equal to the size of y_predict"
    return np.sum(np.absolute(y_true-y_predict))/len(y_true)


def r2_score(y_true,y_predict):
    return 1 - mean_squared_error(y_true,y_predict) /np.var(y_true)


















if __name__ == "__main__":
    x = np.array([1.,2.,3.,4.,5.])
    y = np.array([1.,3.,2.,3.,5.])

    plt.scatter(x,y)
    plt.axis([0,6,0,6])
    plt.show()

    x_mean = np.mean(x)
    y_mean = np.mean(y)




