#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pandas as pd
import numpy as np

target_file = 'F:\python\DataAnalyisForPython\homework\demo_duplicate.csv'

df = pd.read_csv(target_file)

df['Seqno'].duplicated()
df['Seqno'].drop_duplicates()
df.drop_duplicates(['Seqno'],keep='last')
