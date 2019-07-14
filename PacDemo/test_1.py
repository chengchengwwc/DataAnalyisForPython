#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
主成分分析
一个非监督机器学习算法
主要用于数据降维
通过降维，可以发现更加便于人类理解的特征
其他应用:可视化，去燥

1 对所有的样本进行demean进行处理
2 我们想要求一个轴的方向 w=(w1,w2)

使用梯度上升法求解主成分
"""
import  numpy as np
import  matplotlib.pyplot as plt
from sklearn.decomposition import pca

X = np.empty((100,2))
X[:,0] = np.random.uniform(0.,100.,size=100)
X[:,1] = 0.75 * X[:,0] +3. + np.random.normal(0,100,size=100)
plt.scatter(X[:,0],X[:,1])

def deman(X):
    return X - np.mean(X,axis=0)

## 梯度上升发
def f(w,x):
    return  np.sum((x.dot(w)**2)) / len(x)

def df_math(w,x):
    return x.T.dot(x.dot(w)) * 2. / len(x)


def first_n_components(n,x,eta=0.01,n_iters=1e4,epsilon=1e-8):
    X_pca = x.copy()
    X_pca = deman(X_pca)
    res = []
    for i in range(n):
        initial_w = np.random.random(X_pca.shape[1])


class PCA:

    def __init__(self,n_components):
        self.n_components = n_components
        self.components_ = None


    def fit(self,X,eta=0.01,n_iters=1e4):

        def demean(X):
            return X - np.mean(X,axis=0)

        def f(w,X):
            return np.sum((X.dot(w) ** 2)) / len(X)

        def df(w,X):
            return X.T.dot(X.dot(w) * 2) /len(X)

        def direction(w):
            return w / np.linalg.norm(w)

        def first_component(X,initial_w,eta=0.01,n_iters=1e4,epsilon=1e-8):

            w = direction(initial_w)
            cur_iter = 0
            while cur_iter < n_iters:
                gradient = df(w,X)
                last_w = w
                w = w + eta * gradient
                w = direction(w)
                if(abs(f(w,X) - f(last_w,X)) < epsilon ):
                    break
                cur_iter += 1
            return  w

        X_pca = deman(X)
        self.components_ = np.empty(shape=(self.n_components,X.shape[1]))
        for i in range(self.n_components):
            initial_w = np.random.random(X_pca.shape[1])
            w = first_component(X_pca,initial_w,eta,n_iters)
            self.components_[i,:] = w
            X_pca = X_pca - X_pca.dot(w).reshape(-1,1) * w
        return self

    def transform(self,X):
        """
        将给定的X，映射到各个主成分分量中
        :param X:
        :return:
        """

        return X.dot(self.components_.T)


    def inverse_transform(self,X):
        """
        将给定的X，反向映射回原来的特征空间
        :param X:
        :return:
        """
        return X.dot(self.components_)


    def __repr__(self):
        return "PCA(n_components=%d)" % self.n_components



pca = PCA(n_components=1)


















