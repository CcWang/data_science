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

print census_df.head()