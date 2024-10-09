import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read csv
csv_data = pd.read_csv('matches.csv')

# print(csv_data) # print whole csv data
#------
# print(csv_data.head()) # print only the top 5 rows including row header
#------
# print(csv_data.tail()) # print only the last 5 rows including row header
#------
# print(csv_data.shape) # this attribute returns a tuple containing csv row and column count (NOTE: csv_data.shape[0] = row count, csv_data.shape[1] = column count)
#------
# print(csv_data.info()) # print preview of data in csv
#------
# print(csv_data.describe()) # provide mathematical preview (count, mean, min, max, std[Standard deviation], etc.) of only numerical columns and ignore columns having object (string) data
#------
# print(csv_data['winner']) # print a single column. the result will be in series format
#------
# print(csv_data[['season','team1','team2','winner']]) # prints multiple columns, and the result will be in DataFrame format
#------
# print(csv_data.iloc[0]) # print a single column. the result will be in series format
#------
# print(csv_data.iloc[0:4]) # prints multiple rows, and the result will be in DataFrame format || csv_data.iloc[[1,3,5]] - you can also use fancy indexing || csv_data.iloc[:,[3,4,5,10]]
# -- Masking --
# --> masking with single condition
# mask_condition = csv_data['city'] == 'Hyderabad'
# # -- mask_condition contains a boolean series for the condition that city == hyderabad
# print(csv_data[mask_condition])
#------
# --> masking with multiple condition
# condition_1 = csv_data['city'] == 'Hyderabad'
# condition_2 = csv_data['season'] > 2015
# print(csv_data[condition_1 & condition_2])
# using & operator in place of 'and' because condition_1 and condition_2 are boolean
#------
# value_count() returns the frequency count of data in a particular series/column
print(csv_data['winner'].value_counts())
#------
# for plot(), import matplotlib.pyplot as plt
# plot() creates a bar/graph of a particular series/column
print(csv_data['winner'].value_counts().plot(kind='bar'))
#------
