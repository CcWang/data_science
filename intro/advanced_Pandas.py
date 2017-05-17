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
# print adf

# change 'Date' column
# since did not give the value to index[1], will give a NaN value
adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})

# print adf

# merge
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
						{'Name': 'Sally', 'Role': 'Course liasion'},
						{'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
						{'Name': 'Mike', 'School': 'Law'},
						{'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

print(staff_df.head())
print()
print(student_df.head())

# union staff_df and student_df
# left_index = True, right_index = True, means using the index to merge
outer_df = pd.merge(staff_df,student_df,how='outer', left_index = True, right_index = True)
print outer_df

# intersection

inner_df = pd.merge(staff_df,student_df, how = 'inner', left_index = True, right_index = True)

print inner_df

#  left join 
# show the left DataFrame infor, is has interaction with right DataFrame, show that infor too
#  get a list of all staff regardless of whether they were students or not. But if they were students
#  we would want to get their student details as well. To do this we would use a left join. 
left_join = pd.merge(staff_df, student_df, how = 'left', left_index = True, right_index = True)

print left_join

# show a list of all of the students and their roles if they were also staff. 
right_join = pd.merge(staff_df, student_df, how = 'right', left_index = True, right_index = True)

# print right_join

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
column_merge = pd.merge(staff_df, student_df, how = 'left', left_on = 'Name', right_on = 'Name')
print column_merge

# conflicts merger, will show _x and _y
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])

conflicts = pd.merge(staff_df, staff_df, how = 'left', left_on = 'Name', right_on = 'Name')

print conflicts

# multi-column/multi-index
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
multi_merge = pd.merge(staff_df, student_df, how = 'inner', left_on=['First Name', 'Last Name'], right_on=['First Name', 'Last Name'] )

print multi_merge

