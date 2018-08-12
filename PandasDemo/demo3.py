#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

n = np.nan

s1 = pd.Series([1,2,np.nan,3,4],index=["A","B","C","D","E"])
#print(s1)
#print(s1.isnull())
#print (s1.notnull())
#s1.dropna()
#print(s1)

df1 = pd.DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
print (df1)
print (df1.isnull())
print (df1.notnull())
df2 = df1.dropna(axis=0,how="all")

df2.fillna(value={0:0,1:1,2:2})







