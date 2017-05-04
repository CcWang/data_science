import pandas as pd
df=pd.read_csv('olympics.csv',index_col = 0, skiprows = 1)


df['country'] = df.index
# change columns to "Gold Silver Bronze"
for col in df.columns:
	# print col[:2]
	if col[:2] == '01' :
		df.rename(columns={col:'Gold' + col[4:]}, inplace = True)
	if col[:2] == '02' :
		df.rename(columns={col:'Silver' + col[4:]}, inplace = True)
	if col[:2] == '03' :
		df.rename(columns={col:'Bronze' + col[4:]}, inplace = True)

# set Gold value as index
df = df.set_index('Gold')

# print df.head()

# clear index
df = df.reset_index()
# print df.head()


#  using census.csv
df_census = pd.read_csv('census.csv')
print df_census.head()


print df_census['SUMLEV'].unique()

df_census = df_census[df_census['SUMLEV'] == 50]
# print df_census.head()

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']

df_census = df_census[columns_to_keep]
print df_census.head()

print '\n','*'*55,'\n'
df_census = df_census.set_index(['STNAME', 'CTYNAME'])
print df_census.head()