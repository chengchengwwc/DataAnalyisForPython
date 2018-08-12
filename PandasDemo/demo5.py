#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

df1 = pd.DataFrame({"CITY":["BJ","SH","GZ"],"PEOPLE":[1000,2000,1500]})
#df1["GDP"] = pd.Series([1000,2000,1000])

gdp_map = {"BJ":1000,"SH":2000,"GZ":1500}

df1["GDP"] = df1['CITY'].map(gdp_map)

s1 = pd.Series(np.arange(10))
new_s1 = s1.replace(1,np.nan)


