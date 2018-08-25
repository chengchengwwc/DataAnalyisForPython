#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(0,14,100)

y1 = np.sin(x)
y2 = np.sin(x+2)*1,25
plt.plot(x,y1)
plt.show()
style = ['darkgrid','dark','white','whitegrid','tricks']

sns.set_style(style[0])
sns.set_context()
sns.color_palette('his',8)