import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
	# print col[:1]
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
   
# print df.head()


names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[0].str[:3]
df=df.drop("Totals")
# print df.tail()
def answer_zero():
	return df.iloc[0]

# print answer_zero()
 # answer_one
 # remove those country who has no gold medal
def answer_one():
	only_summer_gold = df.where(df['Gold'] > 0).dropna()
 	
 	gold_max = only_summer_gold.loc[only_summer_gold['Gold'].idxmax()]
 	# gold_max.index.name = ['Country']
 	gold_max_id = gold_max['ID']

 	print gold_max

# answer_one()

def answer_two():

	df['Summer_minus_Winter'] = abs(df['Gold']-df['Gold.1'])

	max_dif = df.sort_values(['Summer_minus_Winter'], ascending = False)
	return max_dif.iloc[0].name

# print answer_two()

def answer_three():
	only_gold = df.where((df['Gold'] > 0) & (df['Gold.1'] >0)).dropna()
	only_gold['biggest_dif'] = abs(only_gold['Gold']-only_gold['Gold.1']) / only_gold['Gold.2']
	only_gold = only_gold.sort_values(['biggest_dif'], ascending = False)
	
	return only_gold.iloc[0].name

# print answer_three()

def answer_four():
	df['Points'] =df['Gold.2'] *3 + df['Silver.2'] *2 + df['Bronze.2'] *1

	return df['Points']
# print answer_four()
	
census_df = pd.read_csv('census.csv')

census_df = census_df[census_df['SUMLEV'] == 50]
census_df = census_df.reset_index()
def answer_five():
	unique_counties = census_df.groupby('STNAME')['CTYNAME'].count().sort_values(ascending = False)
	
	
	print unique_counties.index[0]

# answer_five()

def answer_five_op2():
	unique_counties = census_df.groupby('STNAME').count().sort_values(['CTYNAME'], ascending = False)

	return unique_counties.iloc[0].name

def answer_five_op3():
	unique_counties = census_df.groupby('STNAME').count().COUNTY.argmax()

	return unique_counties

# print answer_five_op3()

def answer_six():
	top_threes = census_df.groupby('STNAME')['CENSUS2010POP'].nlargest(3)

	states = top_threes.groupby(level= 0).sum()

	print list(states.nlargest(3).index)

# answer_six()

population_estimates =["POPESTIMATE2010","POPESTIMATE2011","POPESTIMATE2012","POPESTIMATE2013","POPESTIMATE2014","POPESTIMATE2015"]
def answer_seven():
	max_population = census_df[population_estimates].max(axis = 1)
	min_population = census_df[population_estimates].min(axis = 1)
	# county_name = census_df.iloc[(max_population - min_population).argmax()]['CTYNAME']
	county_name = census_df.iloc[
		(census_df[population_estimates].max(axis=1) - 
		census_df[population_estimates].min(axis=1)
		).argmax()]['CTYNAME']
	print county_name


answer_seven()


