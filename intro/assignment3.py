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
	
	energy['Country'] = energy['Country'].str.replace(r"\(.*?\)", "")
	energy['Country'] = energy['Country'].str.replace(r"\d+", "")
	energy['Country'] = energy['Country'].str.strip()

	country_rename_map = {"Republic of Korea": "South Korea","United States of America": "United States","United Kingdom of Great Britain and Northern Ireland": "United Kingdom","China, Hong Kong Special Administrative Region": "Hong Kong"}
	energy.replace({'Country':country_rename_map}, inplace = True)
	return energy

#get GDP
def get_GDP():
	
	# 1 & 2. load the GDP data, call this DataFrame as GDP. skip the header
		#  only keep year 2006 to 2015 columns
	columns = (['Country Name'] + [str(year) for year in range(2006, 2016)])
	GDP = pd.read_csv('world_bank.csv', skiprows = 4, usecols = columns)


	# 3. rename the following country name
		# "Korea, Rep.": "South Korea", 
		# "Iran, Islamic Rep.": "Iran",
		# "Hong Kong SAR, China": "Hong Kong"

	country_rename_map = {"Korea, Rep.": "South Korea","Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"}	
	GDP.replace({'Country Name':country_rename_map}, inplace = True)


	# 4.change column name "Country Name" to "Country"

	GDP.rename(columns={'Country Name' : 'Country'}, inplace = True)

	# return GDP
	return GDP

# get ScimEn
def get_ScimEn():
	# 1. load file and name as ScimEn

	ScimEn = pd.read_excel('scimagojr-3.xlsx')

	# return ScimEn

	return ScimEn

# answer one
def answer_one():

	energy = get_energy()
	GDP = get_GDP()
	# print GDP.iloc(0)[109]['Country']
	# print energy.iloc(0)[98]
	# print energy.iloc(0)[42]
	# print GDP.iloc(0)[109]['Country'] == energy.iloc(0)[98]['Country']

	# get the top 15 country
	ScimEn = get_ScimEn()
	top_15 = ScimEn['Rank'] <= 15
	ScimEn = ScimEn[top_15]

	# Joine three datasets into a new data set (using country names)
	
	dfs = [ScimEn, energy, GDP]
	df_final = reduce(lambda left, right: pd.merge(left, right, on ='Country'), dfs)
	df_final = df_final.set_index('Country')
	return df_final


def answer_two():
    energy = get_energy()
    GDP = get_GDP()
    ScimEn = get_ScimEn()
    
    union = pd.merge(ScimEn, energy, how = 'outer',left_on = 'Country', right_on='Country')
    union = pd.merge(union, GDP, how = 'outer',left_on = 'Country', right_on='Country') 
    intersection = pd.merge(ScimEn, energy, how = 'left', left_on='Country', right_on='Country')
    intersection = pd.merge(intersection, GDP, how = 'left', left_on='Country', right_on='Country')

    return len(union)-len(intersection)

print (answer_two())


def answer_three():
	top15 = answer_one()
	avgGDP = top15[[str(year) for year in range(2006,2015)]].mean(axis = 1)
	return avgGDP.sort_values(ascending = False)

print answer_three()

def answer_four():
    Top15 = answer_one()
    avgGDP = Top15[[str(year) for year in range(2006, 2015)]].mean(axis = 1).sort_values(ascending = False)
    country_idx= (avgGDP[avgGDP == avgGDP.nlargest(6)[-1]]).index
    sixth = Top15.loc[country_idx]
    span =sixth['2015']-sixth['2006'] 
    return span.values[0]
print answer_four()

def answer_five():
	top15 = answer_one()
	avg = top15['Energy Supply per Capita'].mean()
	return avg
print answer_five()


def answer_six():
    Top15 = answer_one()
    country = Top15["% Renewable"].argmax()
    amount = Top15.loc[country]["% Renewable"]
    return (country,amount)
answer_six()

print answer_six()

def answer_seven():
    Top15 = answer_one()
    Top15['self_to_total_citations'] = Top15['Self-citations']/Top15['Citations']
    country = Top15['self_to_total_citations'].argmax()
    ratio = Top15.loc[country]['self_to_total_citations']
    return (country, ratio)

print answer_seven()

def answer_eight():
    Top15 = answer_one()
    Top15['population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    third = Top15.population.nlargest(3)[-1]
    answer = Top15[Top15.population == third].index[0]
    return answer

print answer_eight()


