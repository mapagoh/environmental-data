import pandas as pd
import numpy as np


data= pd.read_csv("data/data.csv")

countries= ['Austria', 'Belgium', 'France', 'Ireland', 'Luxembourg', 'Netherlands', 'Switzerland']

df = pd.read_csv('data.csv', index_col=1)

df= df.loc[df['country']. isin(countries)]

df.to_csv('data/data_clean.csv')


## clean water data

df= pd.read_csv("data/water.csv")

countries= ['Belgium', 'Denmark', 'Luxembourg', 'Netherlands', 'Switzerland']

df = pd.read_csv('water.csv', index_col=1)

df= df.loc[df['Country']. isin(countries)]

df.to_csv('data/water_clean.csv')


## clean biodiversity data

countries= ['Austria', 'Belgium', 'Denmark', 'Luxembourg', 'Netherlands', 'Switzerland']

df = pd.read_csv('biodiversity.csv', index_col=1)

df= df.loc[df['Country']. isin(countries)]

df.to_csv('data/biodiversity_clean.csv')

## clean electricity generation data

df= pd.read_csv("data/electricity.csv")

def plot_country(country_name):
    df = pd.read_csv("electricity.csv")
    df = df[['Country', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']]
    df = df.loc[df['Country'] == country_name]

df.to_csv('data/electricity_clean.csv')