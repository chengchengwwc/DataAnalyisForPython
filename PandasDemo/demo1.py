#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

target_file = 'F:\python\DataAnalyisForPython\homework\movie_metadata.csv'
imdb = pd.read_csv(target_file)
#print (imdb.shape)
#print (imdb.head())
#print (imdb[['color','director_name']])
sub_df = imdb[['director_name','movie_title']]
#print (sub_df.head())
#print (sub_df.iloc[10:20,0:1])






