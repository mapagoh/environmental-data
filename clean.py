import pandas as pd
import numpy as np


data= pd.read_csv("data/data.csv")

col = data.drop(['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'], axis=1)
row = col.drop([0, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19,20, 21, 22, 24, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37], axis=0)

row.to_csv('data/data_clean.csv')


## clean water data

df= pd.read_csv("data/water.csv")

df= df[['Country', '2010', '2015', '2016', '2017', '2018', '2019', '2020']]
df= df.loc[df['Country']. isin(['Belgium', 'Denmark', 'Luxembourg', 'Netherlands', 'Switzerland'])]

df.to_csv('data/water_clean.csv')