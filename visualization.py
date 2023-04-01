from matplotlib import colors
from matplotlib.colors import to_rgba
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data= pd.read_csv("data/data_clean.csv")

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [84150.23, 82007.46, 79309.94, 79772.02, 76235.15, 78486.74, 79468.30, 81792.16, 78558.03, 79740.74, 73592.02]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Austria')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [133645.77, 123133.69, 120361.60, 120458.32, 114768.44, 118955.47, 117417.88, 117097.88, 117594.04, 116448.19, 106433.26]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Belgium')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [512753.49, 488753.45, 490256.23, 491335.79, 461189.49, 464491.27, 466376.98, 469718.63, 450787.08, 441488.01, 399412.67]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('France')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [61948.12, 57742.79, 58764.94, 58550.21, 58006.16, 60477.26, 62714.61, 62066.84, 62351.96, 59855.48, 57716.09]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Ireland')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [12168.53, 12052.28, 11809.92, 11276.75, 10797.43, 10317.72, 10078.73, 10261.75, 10561.47, 10732.70, 9064.90]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Luxembourg')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [211583.23, 197244.08, 193009.40, 193342.44, 185548.93, 192648.93, 193058.39, 190568.24, 185596.91, 179837.65, 163915.18]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Netherlands')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
emissions= [54669.67, 50552.38, 51901.42, 52785.70, 48845.03, 48355.48, 48631.38, 47754.08, 46256.93, 45973.87, 43290.99]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'r', 'b', 'r', 'g', 'b']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:red', 'tab:blue', 'tab:red', 'tab:green', 'tab:blue']
ax.bar(year, emissions, label=bar_labels, color=bar_colors)
plt.title('Switzerland')
fig.set_size_inches(10,5)
plt.show()

## visualization of water data

df= pd.read_csv("data/water_clean.csv")

fig, ax= plt.subplots()
year= ['2010', '2015', '2016', '2017', '2018', '2019', '2020']
public_water= [583.3, 568.2, 562.7, 565.8, 569.2, 570.9, 0]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan']
ax.bar(year, public_water, label=bar_labels, color=bar_colors)
plt.title('Belgium')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2015', '2016', '2017', '2018', '2019', '2020']
public_water= [363, 345.4, 351.8, 350.2, 361.2, 354, 365.9]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan']
ax.bar(year, public_water, label=bar_labels, color=bar_colors)
plt.title('Denmark')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2015', '2016', '2017', '2018', '2019', '2020']
public_water= [0, 42.2, 42.4, 43.2, 49.2, 43.7, 42.8]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan']
ax.bar(year, public_water, label=bar_labels, color=bar_colors)
plt.title('Luxembourg')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2015', '2016', '2017', '2018', '2019', '2020']
public_water= [1083.60, 1077.40, 1091.40, 1097.50, 1135.00, 1121.30, 0]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan']
ax.bar(year, public_water, label=bar_labels, color=bar_colors)
plt.title('Netherlands')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2015', '2016', '2017', '2018', '2019', '2020']
public_water= [816, 803, 804, 810, 829, 815, 824]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan']
ax.bar(year, public_water, label=bar_labels, color=bar_colors)
plt.title('Switzerland')
fig.set_size_inches(10,5)
plt.show()

## visualization of biodiversity data

df= pd.read_csv("data/biodiversity_clean.csv")

fig, ax= plt.subplots()
species= ['Mammals',	'Birds',	'Reptiles',	'Amphibians',	'Fish',	'Marine Fish',	'Freshwater Fish',	'Vascular plants',	'Mosses',	'Lichens',	'Invertebrates']
percentage_of_threat= [26,	28.8,	64.3,	57.1,	39.4,	0, 39.4,	35.8,	23.4,	21.1,	1.8]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(species, percentage_of_threat, label=bar_labels, color=bar_colors)
plt.title('Austria')
fig.set_size_inches(18,5)
plt.show()

fig, ax= plt.subplots()
species= ['Mammals',	'Birds',	'Reptiles',	'Amphibians',	'Fish',	'Marine Fish',	'Freshwater Fish',	'Vascular plants',	'Mosses',	'Lichens',	'Invertebrates']
percentage_of_threat= [21.4,	27.8,	40,	31.6,	20.4,	14.1,	34.9,	23.3,	26.9,	59.1,	10.8]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(species, percentage_of_threat, label=bar_labels, color=bar_colors)
plt.title('Belgium')
fig.set_size_inches(18,5)
plt.show()

fig, ax= plt.subplots()
species= ['Mammals',	'Birds',	'Reptiles',	'Amphibians',	'Fish',	'Marine Fish',	'Freshwater Fish',	'Vascular plants',	'Mosses',	'Lichens',	'Invertebrates']
percentage_of_threat= [12.7,	34.9,	12.5,	33.3,	3.4, 0, 14.5,	5.6,	11.3,	22.1,	14.1]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(species, percentage_of_threat, label=bar_labels, color=bar_colors)
plt.title('Denmark')
fig.set_size_inches(18,5)
plt.show()

fig, ax= plt.subplots()
species= ['Mammals',	'Birds',	'Reptiles',	'Amphibians',	'Fish',	'Marine Fish',	'Freshwater Fish',	'Vascular plants',	'Mosses',	'Lichens',	'Invertebrates']
percentage_of_threat= [0,	19.8,	33.3,	28.6,	27.9, 0,	27.9,	26.8,	0,	0,	15.4]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(species, percentage_of_threat, label=bar_labels, color=bar_colors)
plt.title('Luxembourg')
fig.set_size_inches(18,5)
plt.show()

fig, ax= plt.subplots()
species= ['Mammals',	'Birds',	'Reptiles',	'Amphibians',	'Fish',	'Marine Fish',	'Freshwater Fish',	'Vascular plants',	'Mosses',	'Lichens',	'Invertebrates']
percentage_of_threat= [18.9,	24.4,	71.4,	43.8,	23.7,	17.5,	32.5,	25.5,	23.6,	22.8,	32]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(species, percentage_of_threat, label=bar_labels, color=bar_colors)
plt.title('Netherlands')
fig.set_size_inches(18,5)
plt.show()

fig, ax= plt.subplots()
species= ['Mammals',	'Birds',	'Reptiles',	'Amphibians',	'Fish',	'Marine Fish',	'Freshwater Fish',	'Vascular plants',	'Mosses',	'Lichens',	'Invertebrates']
percentage_of_threat= [34,	37.1,	68.4,	73.7,	37.8,	0,	37.8,	27.2,	33.6,	32.7,	34.5]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(species, percentage_of_threat, label=bar_labels, color=bar_colors)
plt.title('Switzerland')
fig.set_size_inches(18,5)
plt.show()

## visualization of electricity generation data

df= pd.read_csv("data/electricity_clean.csv")

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
electricity_generation= [67709,	62592,	69525,	65260,	62248,	61928,	64961,	68093.595,	65383.711,	71101.128,	69424.515]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(year, electricity_generation, label=bar_labels, color=bar_colors)
plt.title('Austria')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
electricity_generation= [91007,	87121,	79919,	80300,	69818,	67380,	82401,	83122.900,	72065.100,	89913.400,	86055.100]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(year, electricity_generation, label=bar_labels, color=bar_colors)
plt.title('Belgium')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
electricity_generation= [36872,	33549,	29200,	33138,	30815,	27921,	29081,	29638.300,	29315.485,	28689.557,	27880.596]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(year, electricity_generation, label=bar_labels, color=bar_colors)
plt.title('Denmark')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
electricity_generation= [544299,	547532,	547922,	557982,	548732,	555145,	540420,	537849.217,	557797.779,	547042.793,	509273.719]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(year, electricity_generation, label=bar_labels, color=bar_colors)
plt.title('France')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
electricity_generation= [27442,	26365,	26479,	25116,	25312,	27623,	29691,	30093.248,	30357.337,	30274.252,	31519.746]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(year, electricity_generation, label=bar_labels, color=bar_colors)
plt.title('Ireland')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
electricity_generation= [4561,	3694,	3787,	2860,	2938,	2738,	2168,	2204.811,	2170.172,	1877.378,	2209.680]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(year, electricity_generation, label=bar_labels, color=bar_colors)
plt.title('Luxembourg')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
electricity_generation= [114825,	109145,	99174,	97450,	98715,	105731,	110979,	113402.763,	110842.489,	117856.188,	120157.982]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(year, electricity_generation, label=bar_labels, color=bar_colors)
plt.title('Netherlands')
fig.set_size_inches(10,5)
plt.show()

fig, ax= plt.subplots()
year= ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
electricity_generation= [66131,	62959,	68159,	68515,	69986,	66118,	61695,	61652.047,	67449.571,	71739.208,	70004.714]
bar_labels= ['b', 'g', 'b', 'c', 'r', 'g', 'c', 'b', 'g', 'b', 'c']
bar_colors= ['tab:blue', 'tab:green', 'tab:blue', 'tab:cyan', 'tab:red', 'tab:green', 'tab:cyan', 'tab:blue', 'tab:green', 'tab:blue', 'tab:cyan']
ax.bar(year, electricity_generation, label=bar_labels, color=bar_colors)
plt.title('Switzerland')
fig.set_size_inches(10,5)
plt.show()