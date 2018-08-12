#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

s1 = pd.Series([1,2,3],index=['A','B','C'])
s2 = pd.Series([4,5,6],index=['A','B','C'])

df1 = pd.DataFrame(np.arange(4).reshape(2,2),index=['A',"B"],columns=['BJ','SH'])
df2 = pd.DataFrame(np.arange(9).reshape(3,3),index=['A',"B",'C'],columns=['BJ','SH','GZ'])

print (df1+df2)

df2.sum(axis=1)
df2.min()
df2.max()
df2.describe()

