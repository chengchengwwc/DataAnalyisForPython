#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np


target_file = 'F:\python\DataAnalyisForPython\homework\sales-funnel.xlsx'

df = pd.read_excel(target_file)
#print (df)
#默认通过平均聚合
print (pd.pivot_table(df,index=['Manager','Rep'],values=['Price','Quantity'],aggfunc='sum'))


