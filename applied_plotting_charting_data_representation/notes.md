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
3. 
