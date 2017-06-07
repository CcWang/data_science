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

# get and clean housing data from City_Zhvi_AllHomes.csv
def get_housing_data():
	housing = pd.read_csv('City_Zhvi_AllHomes.csv')
	housing.replace({'State':states}, inplace = True)

	return housing
# convert to quarters
def convert_quarters():
	housing = get_housing_data()

	years = ["20{0:02d}".format(year) for year in range(17)]
	year_month_pattern = re.compile('20\d\d-\d\d')
	quarters = [re.compile("|".join(["{0:02d}".format(month) for month in range(start, start+3)])) for start in range(1,11,3)]
	
	all_years = housing.select(lambda x: year_month_pattern.match(x), axis = 1)
	# print all_years
	means = {}
	for year_label in years:
		year = all_years.select(lambda x: re.search(year_label, x), axis = 1)
		for i, quarter_regex in enumerate(quarters):
			quarter = year.select(lambda x: quarter_regex.search(x), axis = 1)
			means["{0}q{1}".format(year_label, i+1)] = quarter.mean(axis = 1)
	
	quarters_in_data = pd.DataFrame(means).dropna(axis = 'columns', how = 'all')
	
	return quarters_in_data
	# print housing.head()

#  clean the housing Data
def cnovert_housing_data_to_quarters():

	housing = get_housing_data()
	quarters = convert_quarters()
	state_reg = [housing.State, housing.RegionName]
	multi_index = pd.MultiIndex.from_tuples(list(zip(*state_reg)), names=["State","RegionName"])
	housing = quarters.set_index(multi_index)

	return housing


# print university_towns_df[university_towns_df.RegionName.str.startswith("Ypsilanti")].State.iloc[0]

# print get_rec_start()
# print get_rec_end()
# print get_rec_bottom()

# print cnovert_housing_data_to_quarters().shape
# step two test
class HypothesisTester(object):
	"""docstring for HypothesisTester"""
	def __init__(self):
		self._start = None
		self._bottom = None
		self._housing_data = None
		self._price_ratios = None
		self._university_towns = None
		self._university_price_ratios = None
		self._non_university_price_ratios = None
		self._p_value = None
		self._t_statistic = None
		self._better = None
		return

	@property
	def university_data(self):
		if self._university_data is None:
			self._university_data = get_list_of_university_towns(university_towns_source)
		return self._university_data

	@property
	def start(self):
		if self._start is None:
			# I was using the start of the recession but it should actually
		    # be the quarter before the recession started
			data = get_gdp()
			index = recession_index(data) -1
			self._start = data.YearQuarter.iloc[index]
		return self._start

	@property
	def bottom(self):
		if self._bottom is None:
			self._bottom = get_rec_end()
		return self._bottom

	@property
	def housing_data(self):

		if self._housing_data is None:
			self._housing_data = cnovert_housing_data_to_quarters()
		return self._housing_data

	@property
	def university_towns(self):

		if self._university_towns is None:
			self._university_towns = get_list_of_university_towns(university_towns_source)

		return self._university_towns

	@property
	def price_ratios(self):
		
		if self._price_ratios is None:
			# div returns a series
			self._price_ratios = self.housing_data[self.start].div(self.housing_data[self.bottom])
			self._price_ratios = pd.DataFrame({"PriceRatio" : self._price_ratios})
			self._price_ratios.reset_index(inplace = True)

		return self._price_ratios

	@property
	def university_price_ratios(self):
		if self._university_price_ratios is None:
			self._university_price_ratios = pd.merge(self.price_ratios, self.university_towns, how="inner", on = ['State', 'RegionName'])
			self._university_price_ratios.dropna(inplace = True)

		return self._university_price_ratios

	@property
	def non_university_price_ratios(self):
		if self._non_university_price_ratios is None:
			university_towns = (self.price_ratios.State.isin(self.university_price_ratios.State) & (self.price_ratios.RegionName.isin(self.university_price_ratios.RegionName)))
			self._non_university_price_ratios = self.price_ratios[~university_towns]
			self._non_university_price_ratios = self._non_university_price_ratios.dropna()
		
		return self._non_university_price_ratios


	@property
	def p_value(self):

		if self._p_value is None:
			self._t_statistic, self._p_value = ttest_ind(self.university_price_ratios.PriceRatio.values, self.non_university_price_ratios.PriceRatio.values)

		return self._p_value

	@property
	def better(self):
		if self._better is None:
			self._better = ("university town" if self.university_price_ratios.PriceRatio.mean() < self.non_university_price_ratios.PriceRatio.mean() else "non university town")
		
		return self._better


def run_ttest():
	tester = HypothesisTester()
	different = tester.p_value < 0.01

	# return tester.university_price_ratios
	return (different, tester.p_value, tester.better)

print run_ttest()
		