#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pandas as pd
import numpy as np


target_file = r'F:\python\DataAnalyisForPython\homework\usa_flights.csv'
df = pd.read_csv(target_file)
#获取延误时间最长top10
print (df.sort_values('arr_delay',ascending=False)[:10])
#计算延误和没有延误的所占比例
print (df['cancelled'].value_counts())
df['delayed'] = df['arr_delay'].apply(lambda x:x>0)
delay_data = df['delayed'].value_counts()
#每一个航空公司的延误情况
delay_group = df.groupby(['unique_carrier','delayed'])
df_delay = delay_group.size().unstack()




