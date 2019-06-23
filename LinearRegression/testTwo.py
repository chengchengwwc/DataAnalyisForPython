#!/usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from sklearn import  datasets





if __name__ == "__main__":
    boston = datasets.load_boston()
    x = boston.data[:,5]
    y = boston.target
    plt.scatter(x,y)
    plt.show()
    x = x[y<50.0]
    y = y[y<50.0]


