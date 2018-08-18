#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#data_tiem_list = pd.date_range('2017-01-01',periods=365)
#s1 = pd.Series(np.random.rand(len(data_tiem_list)),index=data_tiem_list)

#s1_month = s1.resample('M').mean()
#print (s1_month)
#s1.resample('H').ffill()

t_range = pd.date_range('2016-01-01','2016-12-31',freq='H')
stock_df = pd.DataFrame(index=t_range)
stock_df['BABA'] = np.random.randint(80,160,size=len(t_range))
stock_df['TENCENT'] = np.random.randint(30,160,size=len(t_range))

weekly_df = pd.DataFrame()
weekly_df['BABA'] = stock_df['BABA'].resample('W').mean()
weekly_df['TENCENT'] = stock_df['TENCENT'].resample('W').mean()





