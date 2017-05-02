import pandas as pd 

import numpy as np

# redefine sports 
sports ={'Archery' : 'Bhutan',
		'Golf': 'Scotland',
		'Sumo': 'Japan',
		'Taekwondo': 'South Korea'}
s = pd.Series(sports)		

# to located the 4th element -- using index number
#safer
print s.iloc[3]
#  same as
print s[3]

# use index name to locate the element
# safer
print s.loc['Golf']

# same as 
print s['Golf']

sports1 = {99:'Bhutan',
			100:'Scotland',
			101:'Japan',
			102:'South Korea'}

s1=pd.Series(sports1)

# using s1.iloc[0], to access the first item. not s1[0]
print s1.iloc[0]

# same as
print s1[99]

s3=pd.Series([100.00,120.00,101.00,3.00])
print s3

total = 0
for item in s3:
	total +=item
print total

#  using vectorization
total_sum = np.sum(s3)
print total_sum

# create a big series of random numbers
s4 = pd.Series(np.random.randint(0,100,1000))

# will only print the first five, but the lenth of s4 is still 1000
print s4.head()
print len(s4)

#  for in function is slower than numpy.sum() function
summary = 0
for item in s4:
	summary +=item
print summary

summary1 = np.sum(s4)

print summary1

s4+=2 #adds two to each item in s using broadcasting (increase every random variable by 2)
print s4.head()

# tanditional way
for label, value in s4.iteritems():
	s4.set_value(label, value+2)
print s4.head()

origianl_sports = pd.Series({'Archery' : 'Bhutan',
							'Golf': 'Scotland',
							'Sumo': 'Japan',
							'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
										'Barbados',
										'Pakistan',
										'England'],
										index=['Cricket',
												'Cricket',
												'Cricket',
												'Cricket'])
all_countries = origianl_sports.append(cricket_loving_countries)

print origianl_sports
print cricket_loving_countries
print all_countries
print all_countries['Cricket']

