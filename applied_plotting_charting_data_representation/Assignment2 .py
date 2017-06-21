
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fd403b3054061a52e5c4a08dadc245bc6e1b0adabbf12a9eadba68e8.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Santa Clara, California, United States**, and the stations the data comes from are shown on the map below.

# In[1]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fd403b3054061a52e5c4a08dadc245bc6e1b0adabbf12a9eadba68e8')


# In[2]:

# get data
def get_data():
    # get data from csv file    
    df_data = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fd403b3054061a52e5c4a08dadc245bc6e1b0adabbf12a9eadba68e8.csv')
    
    #sort data
    df_data = df_data.sort(['ID','Date'])
    
    #separate the Date by Year and Month-Date for later use
    df_data['Year'],df_data['Month-Date'] = zip(*df_data['Date'].apply(lambda x: (x[:4], x[5:])))
    
    #remove leap days
    df_data = df_data[df_data['Month-Date'] != '02-29']
    
    return df_data
get_data().head()


# In[3]:


# get lists for TMAX and TMIN 
import numpy as np
def get_tmax(df):
    tmax = df[(df['Element'] == 'TMAX') & (df['Year'] !='2015')].groupby('Month-Date').aggregate({'Data_Value':np.max})

    return tmax

def get_tmin(df):
    tmin = df[(df['Element'] == 'TMIN') & (df['Year'] != '2015')].groupby('Month-Date').aggregate({'Data_Value':np.min})
    
    return tmin
def get_2015_tmax(df):
    tmax_2015 = df[(df['Element'] == 'TMAX') & (df['Year'] =='2015')].groupby('Month-Date').aggregate({'Data_Value':np.max})
    
    return tmax_2015

def get_2015_tmin(df):
    tmin_2015 = df[(df['Element'] == 'TMIN') & (df['Year'] == '2015')].groupby('Month-Date').aggregate({'Data_Value':np.min})
    
    return tmin_2015
# df = get_data()

# get_tmax(df)
# get_tmin(df)
# get_2015_tmax(df)
# get_2015_tmin(df)


# In[4]:

# get broken point
def get_broken_min(tmin, tmin_15):
    broken_min = np.where(tmin_15['Data_Value'] < tmin['Data_Value'])[0]
    
    return broken_min

def get_broken_max(tmax, tmax_15):
    
    broken_max = np.where(tmax_15['Data_Value'] > tmax['Data_Value'])[0]
    
    return broken_max

# df = get_data()

# tmax = get_tmax(df)
# tmin = get_tmin(df)
# tmax_15 = get_2015_tmax(df)
# tmin_15 = get_2015_tmin(df)
# get_broken_min(tmin,tmin_15)
# get_broken_max(tmax,tmax_15)


# In[6]:

# draw the line
def plotting_weather():
    df = get_data()
    tmax = get_tmax(df)
    tmin = get_tmin(df)
    tmax_15 = get_2015_tmax(df)
    tmin_15 = get_2015_tmin(df)
    broken_min = get_broken_min(tmin,tmin_15)
    broken_max = get_broken_max(tmax,tmax_15)
    plt.figure()

    plt.plot(tmin.values, color='b', label = 'Low Temperatures 2005-2014')
    plt.plot(tmax.values, color = 'r', label = "High Temperatures 2005-2014")
    # shades
    plt.gca().fill_between(range(len(tmin)), tmin['Data_Value'], tmax['Data_Value'], facecolor = 'gray',alpha = 0.15)
    
    #scatter
    
    plt.scatter(broken_min, tmin_15.iloc[broken_min], s = 18, c = 'black', label = '2015 Broken Low')
    plt.scatter(broken_max, tmax_15.iloc[broken_max], s =18, c = 'm', label = '2015 Broken High')
    
    # make the visual nice
    plt.title('Temperature Summary Plot for Year 2005-2015', alpha=0.8)
    plt.ylabel("Temperatur(Tenths of Degrees C)", alpha = 0.8)
    plt.xlabel("Date", alpha = 0.8)
    plt.xticks(range(0, len(tmin),20), tmin.index[range(0, len(tmin), 20)],rotation = '45')
    
    plt.gca().axis([-5, 370, -150, 650])
    
    plt.legend(loc = 2, frameon = False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.show()

    
plotting_weather()


# In[ ]:



