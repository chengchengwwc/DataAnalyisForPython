#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

target_file = r"F:\python\DataAnalyisForPython\homework\iris.csv"


if __name__ == "__main__":
    s1 = pd.Series(np.random.randn(1000))
    #plt.hist(s1)
    #plt.show()
    #sns.distplot(s1,hist=True,kde=False,rug=True)
    sns.kdeplot(s1)
