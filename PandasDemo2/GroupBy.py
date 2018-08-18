#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

target_file = 'F:\python\DataAnalyisForPython\homework\city_weather.csv'

df = pd.read_csv(target_file)

g = df.groupby(df['city'])
df_bj = g.get_group("BJ")
#平均值
print (df_bj.mean())
#最小值
print (df_bj.min())

#自定义聚合方法
def foo(attr):
    return attr.max() - attr.min()

g.agg(foo)






