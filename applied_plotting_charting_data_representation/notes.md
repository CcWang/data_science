#Applied Plotting, Charting & Data Representation in Python

## Principles of Information Visualization

### Visualization Wheel Dimensions (five dimensions)

	1. Abstraction - Figuration
	A highly figurative visual describes the phenomenon using physical representations of the phenomena, such as photographs or drawings. As the representations become less real and more conceptual, the emphasis shifts from figuration to abstraction. 
		* Boxes and charts(abstraction) or real-world physical objects (figuration)
		
	2. Functionality - Decoration
	 A completely functional graphic has no embellishments and is closer to a direct representation of the data. 
		* No embellishments (functionality) or artistic embellishments(decoration)
		
	3. Density - Lightness
	they related to the amounts of data shown
		* Must be studied in depth (density) or understandable at a glance (lightness)
		
	4. Multidimensional - Unidimensional
		* Different aspects of phenomena (multidimensional) or single or few items of phenomena(unidimensional)
		
	5. Originality  - Familiarity
	
### Graphical heuristics: Data-ink ratio (Edward Tufte)
A heuristic is a process or rule that is meant to guide you in decision making.

Data-ink is the non-erasable core of a graphic.  The non-redundant ink arranged in response to variation in the numbers represented. In other words, the data-ink is essential to the sense-making process for a given variable. 

减少不必要的信息(only leave information that help user to analyze the data)

### Qualities of a good visualization
	1. truthful
		* We have two obligations when it comes to protecting the truth: a.  be honest with ourselves when we clean and summarize data (do not misleading yourself); b. to our audience: (do not misleading your audience)
	
	2. Functionality
	
	3. Beauty
	
	4. Insightful
	
	5. Enlightening
		* A combination of the previous four, but with a social ethical responsibility
		
		


##Matplotlib
matplotlib is a Python-based plotting library with **full support for 2D** and **limited support for 3D graphics
**
###Matplotlib Architecture

	1. Backend Layer:
		* Deals with the rendering of plots to screen or files.
		* In Jupiter notebooks we use the inline backend.
	2. Artist Layer:
		* Contains containers such as Figure, Subplot, and Axes.
		* Contains primitives,such as a Line2D and Rectangle, and collections, such as a PathCollection
	3. Scripting Layer:
		* Simplifies access to the Artist and Backend layers (Used in this course is called pyplot)
		* Fundamentally way of creating and representing graphical interfaces -  procedural (while HTML is declarative information visualization method, same as D3.JS) 

### Overview of matplotlib architecture
from article: [link](http://www.aosabook.org/en/matplotlib.html)
	1. **Figure:** The top-level matplotlib object that contains and manages all of the elements in a given graphic.

#### The architecture to accomplish this is logically separated into three layers, which can be viewed as a stack. Each layer that sits above another layer knows how to talk to the layer below it, but the lower layer is not aware of the layers above it. The three layers from bottom to top are: *backend, artist, and scripting.
*

1. Backend Layer: provides concrete implementations of the abstract interface classes:
	* FigureCanvas (encapsulates the concept of a surface to draw onto e.g. "the paper") 
	* Renderer (does the drawing e.g. "the paintbrush")
	* Event (handles user inputs such as keyboard and mouse events)

2. Artist Layer: the middle layer of the matplotlib stack, and is the place where much of the heavy lifting happens:
	*  the Artist is the object that knows how to take the Renderer (the paintbrush) and put ink on the canvas. 
	* Everything you see in a matplotlib Figure is an Artist instance; the title, the lines, the tick labels, the images, and so on all correspond to individual Artist instances.
	* There are** two types** of Artists in the hierarchy. **Primitive artists** represent the kinds of objects you see in a plot: Line2D, Rectangle, Circle, and Text. **Composite artists** are collections of Artists such as the Axis, Tick, Axes, and Figure. Each composite artist may contain other composite artists as well as primitive artists. For example, the Figure contains one or more composite Axes and the background of the Figure is a primitive Rectangle.

3. Scripting Layer(pyplot)

#### Transforms
1. data: the original raw data values;
2. axes: the space defined by a particular axes rectangle
3. figure: the space containing the entire figure
4. display: the physical coordinates used in the output (e.g. points in PostScript, pixels in PNG)

#### The polyline Pipeline
1. Transformation: The coordinates are transformed from data coordinates to figure coordinates. 
2. Handle missing data: pipeline must skip over the missing data segments using MOVETO commands, which tell the renderer to pick up the pen and begin drawing again at a new point.
3. Clipping:prevent problems on points outside of the boundaries; overflow errors
4. Snapping
5. Simplification

####mathtext
#### regression testing

## Ten simple rules for better Figures [link](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833)

1. Know your Audience
2. Identify Your Message
3. Adapt the Figure to the Support Medium： A figure can be displayed on a variety of media, such as a poster, a computer monitor, a projection screen (as in an oral presentation), or a simple sheet of paper (as in a printed article). Each of these media represents different physical sizes for the figure, but more importantly, each of them also implies different ways of viewing and interacting with the figure.
4. Captions Are Not Optional: The caption explains how to read the figure and provides additional precision for what cannot be graphically represented. 
5. Do Not Trust the Defaults
6. Use Color Effectively
7. Do Not Mislead the Reader
8. Avoid "Chartjunk" : Chartjunk refers to all the unnecessary or confusing visual elements found in a figure that do not improve the message (in the best case) or add confusion (in the worst case).
9. Message Trumps Beauty
10. Get the Right Tool: Matplotlib; R(is a language and environment for statistical computing and graphics. ); Inkscape(is a professional vector graphics editor. );TikZ and PGF (are TeX packages for creating graphics programmatically. ); GIMP (is the GNU Image Manipulation Program.); ImageMagick (is a software suite to create, edit, compose, or convert bitmap images from the command line. ) ; D3.js; Cytoscape (is a software platform for visualizing complex networks and integrating these with any type of attribute data.)Circus ( was originally designed for visualizing genomic data but can create figures from data in any field. Circos is useful if you have data that describes relationships or multilayered annotations of one or more scales.)


##Basic Plotting with Matplolib
1. Started by making a graph using the **plot** function;
2. A plot has two axis: an x-axis, along the horizon, and a y-axis, which runs vertically
3. pyplot.plot(*args, **kwargs) [*args means any number of unnamed arguments; **kwargs means any number of named arguments. give plot function lots of flexible]
4. pyplot.plot(x, y, "str") [x,y 是坐标， “str”是string, 代表how we want the dot to be rendered.]
5.  The scripting layer, though, isn't magic, it's just doing some of the behind the scenes work for us. For instance, when we make a call to pyplot's plot.plot, the scripting layer actually looks to see if there's a figure that currently exists and if not, it creates a new one. It then returns the axis for this figure.
6.  GCF function - get access to the figure using the , which stands for get current figure, of Pi Plot;
7.  GCA function - get access to current axes. 
8.  

*create a new figure*
`plt.figure()
`

*plot the point (3,2) using the circle marker
*`plt.plot(3, 2, 'o')`

*get the current axes*
`ax = plt.gca()`

*Set axis properties [xmin, xmax, ymin, ymax](x轴y轴的左右上下点的值)*
`ax.axis([0,6,0,10])`

9. *get all the child objects the axes contains*
`ax.get_children()`


##Scatterplots
1. Matplotlib actually has a number of useful plotting methods in the scripting layer which correspond to different kinds of plots.Scatterplots is one of the major ones.
2. 记住重要的几点： * pyplot is going to retrieve the current figure with the function gcf and then get the current axis with the function gca. * Pyplot is keeping track of the axis objects for you. But don't forget that they're there and we can get them when we want to get them. * pyplot just mirrors the API of the axis objects. So you can call the plot function against the pyplot module. But this is calling the axis plot functions underneath, so be aware.  *  the function declaration from most of the functions in matplotlib end with an open set of keyword arguments. There are a lot of different properties you can control through these keyword arguments.

### 题外话： zip method
zip method takes a number of iterables and creates tuples out of them, matching elements based on index
for example:
`zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])`
`print(list(zip_generator))`
will return : [(1,6),(2,7),(3,8), (4,9),(5,10)]

*The single star * unpacks a collection into positional arguments*
`print (*zip_generator)`
will return (1,6)(2,7)(3,8)(4,9)(5,10)


If we want to turn the data back into two lists, one with the x component and one with the y component, we can use parameter unpacking with zip. 

`x,y=zip(*zip_generator)`
那么x会变成［1，2，3，4，5］，y就会变成［6，7，8，9，10］

## Line Plots
a line plot is created with the plot function. And plots a number of different series of data points. Connecting each series in a point with a line.

1.  First, we only gave y-axes values to our plot call, no x axes values. Instead, the plot function was smart enough to figure out that what we wanted was to **use the index of the series as the x value.** pyplot.plot([list], **)
2.  the plot identifies different series of data and that the colors of the data from the series are different including the data points and the lines between the data points. 
3.  We can use the regular axes functions creating labels for the axes and for the figure as a whole.  and we can create a legend.  e.g. 
4.  plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
plt.legend(['Baseline', 'Competition', 'Us'])



## fill between function
`plt.gca().fill_between(range(len(linear_data)),linear_data,exponential_data,facecolor='red',alpha=0.15)`

## Bar Charts

#Charting Fundamentals
talk about multiple plots with the same figure, interaction, animation and a few more kinds of plots which you might find useful in your data science journey. 

##Subplots
左右各一个可进行对比
matplotlib.pyplot.subplot(*args, **kwargs)

-	Typical call signature: `subplot(number_of_rows, number_of_columns, plot_number)`
-	number_of_rows, number_of_columns,指把这个figure 分成几个row, 几个columns,然后最后一个数字代表此刻这个subplot处在什么位置
-	subplot index starts at 1 not 0
-	同一个subplot的位置 可以有几个line
-	For instance, if we want to to create two plots side by side, we would call subplot with the parameters 1, 2, and 1. This would allow us to use 1 row, with 2 columns, and set the first axis to be the current axis. `plt.figure() plot.subplot(1,2,1)`
-	to keep the consistency for different subplot, could use sharey = which_subplot to use the same proportion 
-	成批建立subplot 
-	建一个3*3的plot， ax1, ax2,ax3 为第一row的三个，以此类推
-	`fig,((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9), sharex = True, sharey = True)`


## Histograms
is a bar chart which shows the frequency of a given phenomena. 

- A great example are probability distributions

- A great example are probability distributions. 
- **Probability function** can be visualized as a curve, where the y-axis holds the probability a given value would occur, and the x-axis is the value itself. This is called a **probability density function**. The y-axis values are limited to between zero and one, where zero means there's no chance of a given value occurring and one means that the value will always occur. The x-axis values are labeled in terms of the distribution function. In the case of the normal distribution, this is usually in terms of standard deviations. 

### introduce a more flexible GridSpec layout for subplot
- The GridSpec allows us to map axes over multiple cells in a grid
-  The GridSpec is indexed as rows and columns using the indexing operator, or square brackets
-  gridspec([row_postion, column_postion])
-  For probability density histograms, we care only about the relative values. 
-  to make axes values aligned, the Matplotlib cannot post the hoc sharing. The only thing we can do is to set the range of the axis to clear things up a little bit more.

##Box Plots
- sometimes called a box-and-whisker plot is a method of showing aggregate statistics of various samples in a concise matter.
- The box plot simultaneously shows, for each sample, the median of each value, the minimum and maximum of the samples, and the interquartile range
- we can use the **pandas described function **to see some summary statistics about our data frame.`df.describe()`

## Heatmaps
- Heatmaps are a way to visualize three-dimensional data and to take advantage of spatial proximity of those dimensions. 
- plt.colorbar()

## Animation
- Maplotlib.animation module contains important helpers for building animations
- the important object here is to call FunAnimation. It builds an animation by iteratively calling a function which you define. Essentially, your function will either clear the axis object and redraw the next frame, which you want users to see or will return a list of objects which need to be redrawn. 
- numpy.arange([start, ]stop, [step, ]dtype=None)
Return evenly spaced values within a given interval.
- varable = matplotlib.animation.FuncAnimation(figure, function_name, interval_time)

## Interactivity
- very similar in Matplotlib.Animation
- have to reference the canvas object of the current figure
- the most event would be  pick event

### pyplot
import matplotlib.pyplot as plt
- plt.figure()
- plt.cla() clears an axis, i.e. the currently active axis in the current figure. It leaves the other axes untouched.
- plt.clf() clears the entire current figure with all its axes, but leaves the window opened, such that it may be reused for other plots.
- plt.close() closes a window, which will be the current window, if not specified otherwise.
- plt.gca() returns the current axes (a matplotlib.axes.Axes instance).
-  plt.gcf() returns the current figure 


## Pandas Visualization

#### find out the pre-defined styles provided

	- matplotlib.pyplot.style.available
	- use the  '...' style :`pt.style.use('style_name')`
	

### Seaborn
- A python visualization library based on matplotlib
- wraparound matplotlib. It adds styles to make default data visualizations much more visually appealing and makes creation of specific types of complicated plots much simper


#### jointplot

