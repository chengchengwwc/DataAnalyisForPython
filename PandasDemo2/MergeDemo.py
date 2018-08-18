#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key':['x','y','z'],'data_set_1':[1,2,3]})

df2 = pd.DataFrame({'key':['x','y','z'],'data_set_2':[1,2,3]})

pd.merge(df1,df2,how='inner',on='key')


