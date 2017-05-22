# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np 

df = pd.read_csv('census.csv')

# print (df.where(df['SUMLEV']==50)
#     .dropna()
#     .set_index(['STNAME','CTYNAME'])
#     .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})).head()

def min_max(row):
	data = row[['POPESTIMATE2010',
				'POPESTIMATE2011',
				'POPESTIMATE2012',
				'POPESTIMATE2013',
				'POPESTIMATE2014',
				'POPESTIMATE2015']]
	return pd.Series({'min': np.min(data), 'max':np.max(data)})

# print (df.apply(min_max,axis = 1))

def min_max_2(row):
	data = row[['POPESTIMATE2010',
				'POPESTIMATE2011',
				'POPESTIMATE2012',
				'POPESTIMATE2013',
				'POPESTIMATE2014',
				'POPESTIMATE2015']]
	row['max'] = np.max(data)
	row['min'] = np.min(data)

	return row

# print (df.apply(min_max_2, axis = 1)).head()

df_scales = pd.DataFrame(['A+','A','A-','B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],index = ['excellent','excellent','excellent','good','good','good','ok','ok','ok','poor','poor'])
df_scales.rename(columns={0:'Grades'}, inplace = True)
print df_scales
print "********************"
print df_scales['Grades'].astype('category').head()
print "***************"
# If we want to indicate to Pandas that this data is in a logical order,
# we pass the ordered equals True flag and we see that’s reflected 
# in the category dtype using the less than sign.
grades = df_scales['Grades'].astype('category',categories = ['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],ordered=True)
print grades.head()

print '*************'

print grades > 'C'

s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
# cast this series to categorical with the ordering Low < Medium < High
s = s.astype('category', categories = ['Low','Medium','High'], ordered = True)
print s

# reducing a value which is on the interval or ratio scale, 
# like a number grade, into one that is categorical like a letter grade. 
# bin s_example to 3 bins
s_example = pd.Series([168,180,174,190,170,185,179,181,175,169,182,177,180,171])
print pd.cut(s,3)
# can also add labels for the sizes
print pd.cut(s,3,labels=['Small','Medium','Large'])