import pandas as pd 

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
					{'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
					{'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
					index = ['Store 1', 'Store 1', 'Store 2'])

# add new column called 'Date'

df['Date'] = ['December 1', 'January 1', 'mid-May']

#add new column called 'Delivered'

df['Delivered'] = True

df['Feedback'] = ['Positive', None, 'Negative']

# print df

# make a copy of df, but reset index
# will remove the index, set the index to 0 from length
adf = df.reset_index()
print adf