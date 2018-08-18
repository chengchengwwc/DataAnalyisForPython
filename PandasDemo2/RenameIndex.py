#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np


df1 = pd.DataFrame(np.arange(9).reshape(3,3),index=['BJ','SH','GZ'],columns=['A','B','C'])
df1.index = pd.Series(['bj','sh','gz'])
df1.index = df1.index.map(str.upper)
df2 = df1.rename(index=str.lower,columns=str.lower)

