#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s1 = pd.Series(np.random.randn(1000)).cumsums
s1.plot()
plt.legend()
plt.show()

fig,ax = plt.subplots(2,1)
s1.plot(ax=ax[0],label="S1")
s1.plot(ax=ax[1],label="S2")
plt.show()


