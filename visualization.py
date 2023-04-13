import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data= pd.read_csv("data/data_clean.csv")

def graph(title, emissions):
      years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
colors = {'2010': ('tab:blue', 'b'), '2011': ('tab:green', 'g'), '2012': ('tab:blue', 'b'), '2013': ('tab:cyan', 'c'),
               '2014': ('tab:red', 'r'), '2015': ('tab:green', 'g'), '2016': ('tab:cyan', 'c'), '2017': ('tab:blue', 'b'), 
                '2018': ('tab:green', 'g'), '2019': ('tab:blue', 'b'), '2020': ('tab:cyan', 'c')}

fig, ax = plt.subplots()
for i, years in enumerate(years):
        ax.bar(years, emissions[i], label=colors[years][1], color=colors[years][0])
plt.title(title)
fig.set_size_inches(10, 5)
plt.show()

graph('Austria', [84150.23, 82007.46, 79309.94, 79772.02, 76235.15, 78486.74, 79468.30, 81792.16, 78558.03, 79740.74, 73592.02])
graph('Belgium', [133645.77, 123133.69, 120361.60, 120458.32, 114768.44, 118955.47, 117417.88, 117097.88, 117594.04, 116448.19, 106433.26])
graph('France', [512753.49, 488753.45, 490256.23, 491335.79, 461189.49, 464491.27, 466376.98, 469718.63, 450787.08, 441488.01, 399412.67])
graph('Ireland', [61948.12, 57742.79, 58764.94, 58550.21, 58006.16, 60477.26, 62714.61, 62066.84, 62351.96, 59855.48, 57716.09])
graph('Luxembourg', [12168.53, 12052.28, 11809.92, 11276.75, 10797.43, 10317.72, 10078.73, 10261.75, 10561.47, 10732.70, 9064.90])
graph('Netherlands', [211583.23, 197244.08, 193009.40, 193342.44, 185548.93, 192648.93, 193058.39, 190568.24, 185596.91, 179837.65, 163915.18])
graph('Switzerland', [54669.67, 50552.38, 51901.42, 52785.70, 48845.03, 48355.48, 48631.38, 47754.08, 46256.93, 45973.87, 43290.99])

## visualization of water data

df= pd.read_csv("data/water_clean.csv")

def graph(title, public_water)
years = ['2010', '2015', '2016', '2017', '2018', '2019', '2020']
colors = {'2010': ('tab:blue', 'b'), '2015': ('tab:green', 'g'), '2016': ('tab:blue', 'b'), '2017': ('tab:cyan', 'c'),
               '2018': ('tab:red', 'r'), '2019': ('tab:green', 'g'), '2020': ('tab:cyan', 'c')}

fig, ax = plt.subplots()
for i, years in enumerate(years):
        ax.bar(years, public_water[i], label=colors[years][1], color=colors[years][0])
plt.title(title)
fig.set_size_inches(18, 5)
plt.show()

graph('Belgium', [583.3, 568.2, 562.7, 565.8, 569.2, 570.9, 0])
graph('Denmark', [363, 345.4, 351.8, 350.2, 361.2, 354, 365.9])
graph('Luxembourg', [0, 42.2, 42.4, 43.2, 49.2, 43.7, 42.8])
graph('Netherlands', [1083.60, 1077.40, 1091.40, 1097.50, 1135.00, 1121.30, 0])
graph('Switzerland', [816, 803, 804, 810, 829, 815, 824])

## visualization of biodiversity data

df= pd.read_csv("data/biodiversity_clean.csv")

def graph(title, percentage):
    species = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish', 'Marine Fish', 'Freshwater Fish', 'Vascular plants', 'Mosses', 'Lichens', 'Invertebrates']
colors = {'Mammals': ('tab:blue', 'b'), 'Birds': ('tab:green', 'g'), 'Reptiles': ('tab:blue', 'b'), 'Amphibians': ('tab:cyan', 'c'),
               'Fish': ('tab:red', 'r'), 'Marine Fish': ('tab:green', 'g'), 'Freshwater Fish': ('tab:cyan', 'c'), 'Vascular plants': ('tab:blue', 'b'),
               'Mosses': ('tab:green', 'g'), 'Lichens': ('tab:blue', 'b'), 'Invertebrates': ('tab:cyan', 'c')}

fig, ax = plt.subplots()
for i, species in enumerate(species):
        ax.bar(species, percentage[i], label=colors[species][1], color=colors[species][0])
plt.title(title)
fig.set_size_inches(18, 5)
plt.show()

graph('Austria', [26, 28.8, 64.3, 57.1, 39.4, 0, 39.4, 35.8, 23.4, 21.1, 1.8])
graph('Belgium', [21.4, 27.8, 40, 31.6, 20.4, 14.1, 34.9, 23.3, 26.9, 59.1, 10.8])
graph('Denmark', [12.7, 34.9, 12.5, 33.3, 3.4, 0, 14.5, 5.6, 11.3, 22.1, 14.1])
graph('Luxembourg', [0,	19.8,	33.3,	28.6,	27.9, 0,	27.9,	26.8,	0,	0,	15.4])
graph('Netherlands', [18.9,	24.4,	71.4,	43.8,	23.7,	17.5,	32.5,	25.5,	23.6,	22.8,	32])
graph('Switzerland', [34,	37.1,	68.4,	73.7,	37.8,	0,	37.8,	27.2,	33.6,	32.7,	34.5])

## visualization of electricity generation data

df= pd.read_csv("data/electricity_clean.csv")

year = df.columns[1:]
electricity_generation = df.values[0][1:]

bar_colors = ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']

fig, ax = plt.subplots()
ax.bar(year, electricity_generation, color=bar_colors)
plt.title(country_name)
fig.set_size_inches(10,5)
plt.show()

countries = ['AUT', 'BEL', 'DNK', 'FRA', 'IRL', 'LUX', 'NLD', 'CHE']

for country in countries:
    plot_country(country)