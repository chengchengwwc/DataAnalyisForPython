#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np


#s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
#print (s1)
#print (s1.reindex(index=["SS","DFD","DFD","DDF","DDD"],fill_value=10,method="ffill"))

df1 = pd.DataFrame(np.random.rand(25).reshape(5,5),index=["A","B","C","D","E"],columns=["DD","DD","DD","DD","DD"])

print (df1.reindex())

df1.drop("A",axis=0)