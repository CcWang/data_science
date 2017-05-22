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
- when created DataFrame, can set index to whatever you want
	* `df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
					{'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
					{'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
					index = ['Store 1', 'Store 1', 'Store 2'])`
- reset_index() will make index to regular index number (0 - n)
- 如果有些row你没有给value, pandas会自动放NaN value 进去
#### merge two DataFrames/join them together
- Full outer join(union)*want all the information*
- Inner join (intersection) *only want the intersection information（就是只取交集）*
- 语法：
	* use index to join: pd.merge(left_DataFrame_name, right_DataFrame_name, how = 'outer/inner/left/right', left_index = True, right_index = True)
	* use column name to join: pd.merge(left_DataFrame_name, right_DataFrame_name, how = 'outer/inner/left/right', left_on = column_name/['xxx','bbb'], right_on = column_name/['xxx','bbb']) *多个条件(multi-index/multi-column)，把条件放list里*
－ 假如有conflicts between the DataFrames: The merge function preserves this information, but appends an _x or _y to help differentiate between which index went with which column of data. The _x is always the left DataFrame information, and the _ y is always the right DataFrame information. And you could control the names of _x and _y with additional parameters if you want to.

### Pandas Idioms
#### method chaining
- Chain Indexing:
	* df.loc['Washtenaw']['Total Population']
	* Generally **bad**, Pandas could return a copy of a view depending upon numpy
- Code smell
	* If you see a ][ you should think carefully about what you are doing 
－ Method chaining
	* The general idea behind method chaining is that every method on an object returns a **reference** to that object.

## apply (用的比较多)
- most use: find max/min value, and returns a new row of data
- 写一个def，然后apply. Apply takes the function and the axis on which to operate as parameters.  example: `df.apply(def_name, axis = 1)` 
- axis parameter is really the parameter of the index to use. So, to apply across all rows, you pass axis equal to one.

## Group by
- group by function: This function takes some column name or names and splits the DataFrame up into chunks based on those names, it returns a DataFrame groupby object. Which can be iterated upon, and then returns a tuple where the first item is the group condition, and the second item is the data frame reduced by that grouping.

## Scales
### Ratio scale:
- units are equally spaced
- mathematical operations of +-/* are all valid. *e.g. height and weight*

### Interval scale:
- units are equally spaced, but theres no clear absence of value (no true zero)
- operation such as multiplication and division are not valid. *e.g. the temperatures measured in Celsius or Fahrenheit*

### Ordinal scale (common in machine learning):
- the order of the units is important, but the differences between the value are not evenly spaced.
- letter grades such as A+, A are a good example   

### Nominal scale (called categorical data):
- categories of data, but the categories have no order with respect to one another.
- E.g. Teams of a sport

Variables with a Boolean value are typically called dummy variables. And pandas has a built-in function called get_dummies, which will convert the values of a single column into multiple columns of 0's and 1's, indicating the presence of a dummy variable. 

## one more function 

reducing a value which is on the interval or ratio scale, like a number grade, into one that is categorical like a letter grade. 
- Now, this might seem a bit counter intuitive to you since you're losing information about the value. But it's useful on a couple of places. 

	1. First, if you're visualizing the frequencies of categories, and this can be an extremely useful approach and histograms are regularly used with converted interval or ratio data 
	2. Second, if you're using a machine learning classification approach on data, then you need to be using categorical data. So reducing dimensionality is useful there too.
	3. Pandas has a function called cut, which takes an argument which is some array like structure of a column or a DataFrame or a series.
	4. It also takes a number of bins to be used and all bins are kept at equal spacing. 
	
##Pivot Tables
A pivot table is a way of summarizing data in a data frame for a particular purpose. It makes heavy use of the aggregation function. 

- A pivot table is itself a data frame, where the rows represent one variable that you're interested in, the columns another, and the cell's some aggregate value. 
- A pivot table also tends to includes marginal values as well, which are the sums for each column and row. **This allows you to be able to see the relationship between two variables at just a glance. **

## Date Functionality
### Timestamp
`pd.Timestamp('9/1/2016)`
 Timestamp is interchangeable with Python's datetime in most cases.
 
### Periods
- Suppose we weren't interested in a specific point in time, and instead wanted a span of time. This is where Period comes into play.
- Period represents a single time span, such as a specific day or month. 

### DatetimeIndex
- `t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
` each timestamp is the index and has a value associated with it, in this case, a, b and c. 

### PeriodIndex
`t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
`
type is PeriodIndex

### converting to Datetime
pandas.to_datetime

###Timedeltas
time differences

###working with Dates in a Dataframe


