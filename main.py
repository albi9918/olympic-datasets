import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df_countries = pd.read_csv('CountriesSD.csv')
df_summer = pd.read_csv('SummerSD.csv')
df_winter = pd.read_csv('WinterSD.csv')

#print(df_countries.head())

#dataframe grouped by discipline and country
grouped_summer = df_summer.groupby(['Country', 'Discipline']).size().reset_index(name='Count')
grouped_winter = df_winter.groupby(['Country', 'Discipline']).size().reset_index(name='Count')
#print the results
print(grouped_summer.head())
print(grouped_winter.head())

#dataframe grouped by year and country
grouped_summer_year = df_summer.groupby(['Country', 'Year']).size().unstack(fill_value=0).reset_index()
grouped_winter_year = df_winter.groupby(['Country', 'Year']).size().unstack(fill_value=0).reset_index()
#print the results
print(grouped_summer_year.head())
print(grouped_winter_year.head())

#dataframe grouped by medal type (in the columns) and country
grouped_summer_medals = df_summer.groupby(['Country', 'Medal']).size().unstack(fill_value=0).reset_index()
grouped_winter_medals = df_winter.groupby(['Country', 'Medal']).size().unstack(fill_value=0).reset_index()
#print the results
print(grouped_summer_medals.head())
print(grouped_winter_medals.head())