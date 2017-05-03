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
# use DataFrame to put series into one table
df=pd.DataFrame([purchase_1,purchase_2,purchase_3],index=['Store 1','Store 1', 'Store 2'])
print df.head()
print '\n',"*"*50,'\n'
# use index name to access one group of data
print 'print out ["Store 2"]'
print df.loc['Store 2']
print '\n','print out the type:','\n'
print type(df.loc['Store 2'])

print '\n',"*"*50,'\n'

# can quickly select data based on multiple axis
print 'Print out hte store 1 cost only\n'
print df.loc['Store 1','Cost']
print df['Cost']

print '\n',"*"*50,'\n'

# slicing (better way of 
# selecting and projecting data from a DataFrame based on 
# row and column labels)
print df.loc[:,['Name','Cost']]

print '\n',"*"*50,'\n'

# drop data
print df.drop('Store 1')

print '\n',"*"*50,'\n'

print df

print "make a copy of df, then try drop in place"
print '\n',"*"*50,'\n'
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
print copy_df

del copy_df['Name']
print copy_df

df['Location'] = None
print df
