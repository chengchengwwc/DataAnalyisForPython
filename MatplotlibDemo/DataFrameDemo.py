#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randint(1,10,40).reshape(10,4),columns=["A","B","C","D"])
#df.plot(kind="bar")
#df.plot(kind="barh")
#df.plot(kind="bar",stacked=True)
df.plot(kind="area")
for i in df.index:
    df.iloc[i].plot(label=str(i))
df["A"].plot()

new_df = df.T
new_df.plot()


plt.show()

