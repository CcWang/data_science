##NumPy

- numpy.random.randint(low, how=None, size = Noe, dtype='l')

## Pandas practices
[http://pandas.pydata.org/pandas-docs/stable/10min.html#apply](http://pandas.pydata.org/pandas-docs/stable/10min.html#apply)

##Basic Data Processing with Pandas
- Pandas data tool kits, open source
- Help to learn Pandas: Stack Overflow; books: Python for Data Analysis( by O'Reilly ), Learning the Pandas library (by Matt Harrison); Planet Python (http://planetpython.org); data Skeptic Podcast (http://dataskeptic.com)
- The series is one of the core data structures in pandas.
- How pandas' series can be created : can be created from dictionary data, index is automatically assigned to the keys of the dictionary that you provided and not just incrementing integers

##vectorization
- Pandas and the underlying NumPy libraries support a method of computation called vectorization
- Sum method
- faster 

####Related feature in Pandas and NumPy is called broadcasting. With broadcasting, you can apply an operation to every value in the series, changing the series.

####when adding values to series, Pandas will automatically change the underlying NumPy types as appropriate. For example, numbers.Series([1,2,3]) => typy is int, number.loc['Animal'] = 'Bears', 之后，type is object

##DatFrame data structure
- heart of the Pandas library.
- It's the primary object that you'll be working with in data analysis and cleaning tasks.
- Is conceptually a **two-dimensional** series object.
	* an index and multiple columns of content, with each column having a label 
	* the indices and column names along either axis, horizontal or vertical, could be **non-unique**
	### ACCESS DATA
	* one of the powers of the Panda's DataFrame is that you can quickly select data based on multiple axis. for example: `df.loc["Store 1", "Cost"]`
	* 进入下一级（就是index里面的那一层）: 
		1. using the capital T attribute, which swaps all of the columns and rows. This essentially turns your column names into indices. for example: `df.T.loc["Cost"]`
		2. Since columns always have names, so selection is always label based. 可以直接用 `df["Cost"]` or just **chain** operations together. `df.loc["Store 1"]["Cost"]`***缺点： chaining tends to cause Pandas to return a copy of the DataFrame, instead of a view of the DataFrame (只是拿出来看看data,顶多就是慢一点。 但是如果用这个方法change data，会慢很多并且can be s source of error)*** **TRY TO AVOID IT**
		3. .loc also supports slicing (弥补上面那条的不足):  If we wanted to select all rows, we can use a column to indicate a full slice from beginning to end. And then add the column name as the second parameter as a string. In fact, if we wanted to include multiply columns, we could do so in a list. And Pandas will bring back only the columns we have asked for. for example: `df.loc[:,["Name","Cost"]]`
	* the key concepts to remember are that the rows and columns are really just for our benefit. Underneath this is just a two axis labeled array, and transposing the columns is easy
	### DROPPING DATA
	* drop function, take single parameter, which is the index or roll label to drop. `df.drop("Store 1")`
	* the drop function doesn't change the DataFrame by default. And instead, returns to you a copy of the DataFrame with the given rows removed.
	* drop has two interesting optional parameters. The first is called **in place**, and if it's set to true, the DataFrame will be updated in place, instead of a copy being returned. The second parameter is the **axis**, which should be dropped. *by default, this value is **0**, indicating the **row** axis. But you could change it to **1** if you want to drop a **column*** 
	* There is a second way to drop a column. And that's directly through the use of the indexing operator, using the del keyword. for example: `del df["Name"]` *This way of dropping data, however, takes immediate effect on the DataFrame and **does not return a view**. *
	### ADD A NEW COLUMN
	*  is as easy as assigning it to some value. For instance, if we wanted to add a new location as a column with default value of none, we could do so by using the assignment operator after the square brackets. This broadcasts the default value to the new column immediately. 
	* for example: `df["Location"] = None`
	
	
## DataFrame Indexing and Loading
- The common work flow is to read your data into a DataFrame then reduce this DataFrame to the particular columns or rows that you're interested in working with.
- If you're manipulating the data you have to be aware that any changes to the DataFrame you're working on may have an impact on the base data frame you used originally. 

##Querying a DataFrame
### Boolean masking
- is the heart of fast and efficient querying in NumPy.
- A Boolean mask is an array which can be of one dimension like a series, or two dimensions like a DataFrame, where each of the values in the array are either true or false. This array is essentially overlaid on top of the data structure that we're querying. And any cell aligned with the true value will be admitted into final result and any sign aligned with a false value will not.
- Boolean masks are created by applying operators directly to the pandas series or DataFrame objects.
- 就是盖一层T/F的mask在原本的数据上，可控制只显示true或 false
- Use **where** function to overlay that mask on the DataFrame. The where function takes a Boolean mask as a condition, applies it to the DataFrame or series, and returns a new DataFrame or series of the same shape. for example: `only_gold = df.where(df["Gold"] > 0)`
- can use & | to chain lots conditions in Boolean mask

## Indexing Dataframes
- The index is essentially a row level label, and we know that rows correspond to axis zero.
- Indices can either be inferred, or they can be set explicitly: 1. use the dictionary object to create the series; 2. loaded data from the CSV file and specified the header.3. use the **set_index** function. for example: `df.set_index("Gold")`
	* Set index is a destructive process, it doesn't keep the current index.* If you want to keep the current index, you need to manually create a new column and copy into it values from the index attribute. *
- df.reset_index()

### multi-level indexing
- This is similar to composite keys in relational database systems. To create a multi-level index, we simply call set index and give it a list of columns that we're interested in promoting to an index. Pandas will search through these in order, finding the distinct data and forming composite indices. 

##Missing Values
- couple of caveats and discussion points which we should address:
	1. the build in loading from delimited files provides control for missing values in a few ways: na_values list;na_filter option to turn off white space filtering (if you need); could treat missing values as values with information
	2. One of the handy functions that Pandas has for working with missing values is the filling function, fillna.*This function takes a number or parameters, for instance, you could pass in a single value which is called a scalar value to change all of the missing data to one value. METHOD PARAMETER: The two common fill values are ffill and bfill. ffill is for forward filling and it updates an na value for a particular cell with the value from the previous row.* 
	3. When you use statistical functions on DataFrames, **these functions typically ignore missing values**. For instance if you try and calculate the mean value of a DataFrame, the underlying NumPy function will ignore missing values. This is usually what you want but you should be aware that values are being excluded. 

## Advanced Python Pandas
### Merging Dataframes
- To add new data
	* df[**column**] = [a,b,c]
- To set default data (or overwrite all data):
	* df[**column**] = 2



