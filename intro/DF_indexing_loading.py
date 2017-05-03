import pandas as pd
purchase_1 = pd.Series({'Name':'Chris',
						'Item Purchased': 'Dog Food',
						'Cost': 22.50})
purchase_2 = pd.Series({'Name':'Kevyn',
						'Item Purchased':'Kitty Litter',
						'Cost':2.50})
purchase_3 = pd.Series({'Name':'Vinod',
						'Item Purchased':'Bird Seed',
						'Cost':5.00})
df_purchase=pd.DataFrame([purchase_1,purchase_2,purchase_3],index=['Store 1','Store 1', 'Store 2'])

costs = df_purchase['Cost']

print costs

print '\n','*'*50,'\n'

print 'increase the cost in this series using broadcasting'

costs +=2

print '\n','*'*50,'\n'
print costs

print '\n','*'*50,'\n'
print "original DataFrame, those costs have risen as well.so be awaring if you need to use copy method"
print df_purchase

# using olympics.csv
df=pd.read_csv('olympics.csv')
print df.head()

# Read csv has a number of parameters that we can use to 
# indicate to Pandas how rows and columns should be labeled. 
# For instance, we can use the index call to indicate which column should be the index 
# and we can also use the header parameter to indicate which row from the data file 
# should be used as the header.
# Let's re-import that data and center index value to be 0 which is the first column and 
# let set a column headers to be read from the second row of data. 
# We can do this by using the skip rows parameters, to tell Pandas to ignore the first row, which was made up of numeric column names. 

df=pd.read_csv('olympics.csv',index_col = 0, skiprows = 1)
print '\n','*'*50,'\n'
print df.head()

print '\n','*'*50,'\n'
print "print all columns"

print df.columns

# to change 01,02...to easy to read colunms and still keep the unique '.1, .2 ...'from Pandas
for col in df.columns:
	# print col[:2]
	if col[:2] == '01' :
		df.rename(columns={col:'Gold' + col[4:]}, inplace = True)
	if col[:2] == '02' :
		df.rename(columns={col:'Silver' + col[4:]}, inplace = True)
	if col[:2] == '03' :
		df.rename(columns={col:'Bronze' + col[4:]}, inplace = True)
	

print df.head()
# Querying a DataFrame

print '\n','*'*50,'\n'
# Boolean mask
#  using where function to overlaid the mask on the DataFrame 
only_gold = df.where(df['Gold'] > 0)
print only_gold.head()

# count
print only_gold['Gold'].count()

print df['Gold'].count()

#  to drop NaN 
only_gold = only_gold.dropna()
print only_gold.head()


#  use & |

print len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])

print df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]


