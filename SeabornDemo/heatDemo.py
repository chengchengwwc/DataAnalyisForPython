#!/usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset('flights')

df = df.pivot(index="month",columns="year",values="passenger")

sns.heatmap(df,annot=True,fmt='d')

new_df = df.sum()
s = new_df.index
yz = new_df.values
sns.barplot(x=s,y=yz,)

