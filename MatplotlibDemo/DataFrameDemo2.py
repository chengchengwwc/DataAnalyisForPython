#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(np.random.randn(10))
print (s)
s.plot(kind="kde")
#plt.hist(s,rwidth=0.9,bins=20)
plt.show()