#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

score_list = np.random.randint(30,100,size=25)
print (score_list)
bins = [0,59,70,80,100]

mm =pd.cut(score_list,bins)
print (pd.value_counts(mm))

df = pd.DataFrame()
df['score'] = score_list
#df['student'] = [pd.util.testing.rands(3) for i in range(20)]
df['catranf']=pd.cut(df['score'],bins)
print (df)