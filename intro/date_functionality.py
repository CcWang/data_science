import pandas as pd
import numpy as np

print "Timestamp"
print pd.Timestamp('5/21/2017')

print "Period"
print pd.Period('3/5/2016')

print "DatetimeIndex"
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
print t1
print type(t1.index)

print "PeriodIndex"
t2 = pd.Series(list('def'),[pd.Period('2016-09'),pd.Period('2016-10'), pd.Period('2016-11')])
print t2
print type(t2.index)

print "Converting to Datetime"
d1=['2 June 2013', 'Aug 29, 2014', '2015-06-26','7/12/16']
ts3 = pd.DataFrame(np.random.randint(10,100,(4,2)), index = d1,columns = list('ab'))
print ts3
# change different date format to datetime
# pandas.to_datetime
ts3.index = pd.to_datetime(ts3.index)
print "after to_datetime"
print ts3
print pd.to_datetime('4.7.12', dayfirst=True)

print "Timedeltas - time differences"
print pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016')
print pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')

print "working with Dates in a DataFrame"
# print "Suppose we want to look at nine measurements, taken bi-weekly, every Sunday. Starting in October 
dates = pd.date_range('10-01-2016', periods = 9, freq='2W-SUN')
# let's create DataFrame using these dates, and some random data, and see what we can do with it. 
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5,10,9).cumsum(),
                  'Count 2': 120+ np.random.randint(-5,10,9)}, index = dates)
print df
# we can see that all the dates in our index are on a Sunday
print df.index.weekday_name
# we can use diff to find the difference between each date's value
print df.diff()
# Suppose we wanted to know what the mean count is for each month in our DataFrame. We can do this using resample.
print df.resample('M').mean()
# to find particular year, month, slice range of dates
print df['2017']
print df['2016-12']
# after 2016-12

# could change the frequence use asfreq
# we use this to change the frequency from bi-weekly to weekly We'll end up with missing values every other week. So let's use the forward fill method on those missing values. 
print df.asfreq('W', method='ffill')
print df['2016-12':]

print "plottng time series"

import matplotlib.pyplot as plt
%matplotlib inline
# from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'inline')
print df.plot()
