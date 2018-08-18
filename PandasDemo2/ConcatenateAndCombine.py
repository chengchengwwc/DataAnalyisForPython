#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

arr1 = np.arange(9).reshape(3,3)
arr2 = np.arange(9).reshape(3,3)


np.concatenate(arr1,arr2)


s1 = pd.Series([1,2,3],index=['X','Y','Z'])
s2 =pd.Series([2,3],index=['A',"B"])
pd.concat([s1,s2])


s3 = pd.Series([2,np.nan,4,np.nan],index=['A','B','C','D'])
s4 = pd.Series([2,np.nan,4,np.nan],index=['A','B','C','D'])

s3.combine_first(s4)



