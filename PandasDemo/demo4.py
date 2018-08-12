#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

s1 = pd.Series(np.random.randn(6),index=[['1','1','1','2','2','2'],['a','a','a','b','b','b']])
print (s1)
#df1 = s1.unstack()
#print (df1)
#df2 = pd.DataFrame([s1['1'],s1['2']])
#print (df2)

df  = pd.DataFrame(np.arange(16).reshape(4,4),index=[['a','a','b','b'],['c','c','d','d'],['e','e','f','f']])
print (df)


