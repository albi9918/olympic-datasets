import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df_countries = pd.read_csv('CountriesSD.csv')
df_summer = pd.read_csv('SummerSD.csv')
df_winter = pd.read_csv('WinterSD.csv')

print(df_countries.head())