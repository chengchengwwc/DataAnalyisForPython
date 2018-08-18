#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

target_file = r'F:\python\DataAnalyisForPython\homework\apply_demo.csv'

df1 = pd.read_csv(target_file)

df1['A'] = df1['A'].apply(str.upper)

tmp_list = df1['data'][0].strip().split(' ')

def foo(line):
    items = line.strip().split(" ")
    return pd.Series([items[1],items[3],items[5]])

def_tmep = df1['data'].apply(foo)
df_new = df1.combine_first(def_tmep)
df_new.to_csv("DDD.csv")
