import pandas as pd 
import numpy as np
import xlrd 
import re
#question one
# Engergy Indicators 

def get_energy():
	#1 & 2. put Energy Indicators.xls into a DataFrame with the variable name of energy exclude the footer and the hader
	#	For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
	energy = pd.read_excel('energy_indicators.xls',skiprows = 17, skip_footer = (283-246+1),na_values = '...')
	
	#3. get rid of first two columns
	# drop by index

	energy.drop(energy.columns[[0,1]], axis = 1, inplace = True)

	#4. change the column labels so that the columns are:
	#	['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
	energy.rename(columns={'Unnamed: 2':"Country", 'Petajoules':'Energy Supply','Gigajoules':'Energy Supply per Capita', '%':"% Renewable"}, inplace = True)
	
	# 5. Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule).
	energy['Energy Supply'] *=1000000

	# 6. Rename the following list of countries (for use in later questions):
	#	"Republic of Korea": "South Korea",
	#	"United States of America": "United States",
	#	"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
	#	"China, Hong Kong Special Administrative Region": "Hong Kong"
	#	There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these
	
	country_rename_map = {"Republic of Korea": "South Korea",
							"United States of America20": "United States",
							"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
							"China, Hong Kong Special Administrative Region": "Hong Kong"}
	energy.replace({'Country':country_rename_map}, inplace = True)
	# remove_num_par = "(?P<{0}>[a-zA-Z\s\-]+)\b?(\(|\d)*"
	energy['Country'] = energy['Country'].str.replace(r"[\(\)\d]+", "")

	return energy

#get GDP
def get_GDP():
	
	

get_energy()




# 7.  load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.
