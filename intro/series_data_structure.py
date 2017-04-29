import pandas as pd 

import numpy as np

animals = ['Tiger', 'Bear', 'Moose']
# pd.Series(animals)

numbers = [1,2,3,None]
# pd.Series(numbers)
animals = ['Tiger', 'Bear', None]
print pd.Series(animals)
num = pd.Series(numbers)
print num


# will return False
print np.nan == None 

# will return True
print np.isnan(np.nan)

sports ={'Archery' : 'Bhutan',
		'Golf': 'Scotland',
		'Sumo': 'Japan',
		'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print s
print s.index
print num.index

# another way to create series. separate index creation from the data
s1 = pd.Series(['Tiger','Bear', 'Moose'], index = ['India','America','Canada'])
print s1