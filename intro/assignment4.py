import pandas as pd 
import numpy as np
from scipy.stats import ttest_ind
import re
import operator

# Definitions:
# Q1 Jan - Mar, Q2 Apr - Jun, Q3 Jul - Sep, Q4 Oct - Dec
# A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
# A recession bottom is the quarter within a recession which had the lowest GDP.
# A university town is a city which has a high percentage of university students compared to the total population of the city

# Hypothesis: University towns have their mean housing prices less effected by recessions. 
# Run a t-test to compare the ratio of the mean price of houses in university towns the quarter 
# before the recession starts compared to the recession bottom. 
# (price_ratio=quarter_before_recession/recession_bottom)

#  step one: get all your data, make them clean and easy to use
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
city_home_source = 'City_Zhvi_AllHomes.csv'
university_towns_source = 'university_towns.txt'
gdp_source = 'gdplev.xls'
chained_dollars = 'Quarterly GDP 2009 Billions'

def get_list_of_university_towns(data_source):
	if data_source is not None:
		lines = []
		with open(data_source) as data:
			for l in data:
				if "[edit]" in l:
					state = l.split('[')[0].strip()
				else:
					region = l.split('(')[0].strip()
					lines.append([state, region])
		university_towns_df = pd.DataFrame(lines, columns = ['State','RegionName'])
	else:
		university_towns_df = pd.DataFrame("None")

	return university_towns_df;

def get_gdp():
	columns = ["Year", "Annual GDP Current Billions",
	       "Annual GDP 2009 Billions", "to_del", "YearQuarter",
	       "Quarterly GDP Current Billions", "Quarterly GDP 2009 Billions",
	       "to_del"]
	gdp = pd.read_excel(gdp_source,skiprows = 8, names = columns)
	gdp=gdp.drop("to_del", axis = 1)

	# only use data from the first quarter of 2000 onward
	gdp = gdp.iloc[gdp[gdp.YearQuarter == '2000q1'].index[0]:]
	return gdp.dropna(1).reset_index()

# to get recession index for recession start index or recession end index
def recession_index(data, compare = operator.gt):
	for i, gdp in enumerate(data[chained_dollars]):
		# print "index: {}; GDP: {}".format(i, gdp)
		next_gdp=data[chained_dollars].iloc[i+1]
		# print compare(data[chained_dollars].iloc[i-1],gdp)
		# if gdp[1] > gdp[2] > gdp [3] means gdp[2] is the recession start point. since number started to drop, is the point that recession started
		if(i !=0 and (compare(data[chained_dollars].iloc[i-1], gdp) and compare(gdp, next_gdp))):
			return i
		elif compare(gdp,next_gdp) and compare(next_gdp , data[chained_dollars].iloc[i+2]):
			return i+1

# get recession start 
def get_rec_start():
	data = get_gdp()
	start_i = recession_index(data)

	return data.YearQuarter.iloc[start_i]

# get recession end
def get_rec_end():
	# need to find the start first, then find the end
	data = get_gdp()
	start = get_rec_start()
	# chop the data, get all the data after the recession started
	data= data[data[data.YearQuarter == start].index[0]:]
	# find the recession end
	#  recession_index will get the last quarter of the recession, not the end (first quarter out of the recession)
	#  so need to add 1
	end_i = recession_index(data, operator.lt) +1

	return data.YearQuarter.iloc[end_i]

# find the recession bottom
def get_rec_bottom():
	data = get_gdp()
	start = get_rec_start()
	end = get_rec_end()
	data = data[data[data.YearQuarter == start].index[0]: data[data.YearQuarter == end].index[0]]

	bottom = data.YearQuarter.loc[data[chained_dollars].argmin()]

	return bottom



university_towns_df = get_list_of_university_towns(university_towns_source)
# print university_towns_df[university_towns_df.RegionName.str.startswith("Ypsilanti")].State.iloc[0]

print get_rec_start()
print get_rec_end()
print get_rec_bottom()
