#!/usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


def getLine():
    plot_x = np.linspace(-1,6,141)
    plot_y = (plot_x-2.5)**2 -1
    plt.plot(plot_x,plot_y)
    plt.show()


def dj(theta):
    # 求导
    return 2*(theta - 2.5)





def gradient_descent(initial_theta,eta,epsilon=1e-8):
    theta = initial_theta



def test():
    x = 2 * np.random.random(size=100)
    y = x * 3. + 4. + np.random.normal(size=100)


"""
使用梯度下降法进行线性回归
"""
def J(theta,X_b,y):
    return np.sum((y - X_b.dot(theta))**2) / len(X_b)

