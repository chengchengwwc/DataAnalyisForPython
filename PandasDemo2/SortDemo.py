#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pandas as pd
import numpy as np


s1 = pd.Series(np.random.randn(10))
#排序,默认是升序
s2 = s1.sort_values()
print(s2)
#按照index排序
s3 = s1.sort_index()

df1 = pd.DataFrame(np.random.randn(40).reshape(8,5),columns=['A','B','C',"D",'E'])
#df1['A'].sort_values()
df2 = df1.sort_values('A')
df3 = df2.sort_index()



