
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib notebook')
import matplotlib.pyplot as plt
import numpy as np
# plt.subplot?


# In[2]:

plt.figure()
plt.subplot(2,3,1)

linear_data = np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data, '-o')


# In[3]:

exponential_data = linear_data**2
plt.subplot(2,3,4)
plt.plot(exponential_data, '-x')


# In[4]:

plt.subplot(2,3,1)
plt.plot(exponential_data,'-x')


# In[5]:

plt.figure()
ax1 = plt.subplot(1,2,1)
plt.plot(linear_data, '-o')
# make ax1 and ax2 to have the same y axis to keep the consistency
ax2 = plt.subplot(1,2,2,sharey=ax1)
plt.plot(exponential_data, '-x')


# In[6]:

plt.figure()
# second syntax
# save the space and commas in between
plt.subplot(1,2,1) == plt.subplot(121)


# In[7]:

fig, ((ax1,ax2,ax3), (ax4,ax5,ax6),(ax7,ax8,ax9)) = plt.subplots(3,3,sharex = True, sharey = True)

ax5.plot(linear_data,'-')
ax9.plot(exponential_data, '-o')


# In[8]:

for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
#         print(label)
        label.set_visible(True)


# In[9]:

plt.gcf().canvas.draw()


# In[11]:

# histograms
# create 2*2 grid of axis  subplots
fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, sharex = True)
axs = [ax1,ax2,ax3,ax4]

# draw n = 10, 100, 1000, 10000 samples from the normal distribution and plot corresponding histograms
for n in range(len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc = 0.0, scale = 1.0, size = sample_size)
    axs[n].hist(sample)
    axs[n].set_title('n={}'.format(sample_size))



# In[12]:

# repeat with number of bins set to 100
fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, sharex = True)
axs = [ax1,ax2,ax3,ax4]

# draw n = 10, 100, 1000, 10000 samples from the normal distribution and plot corresponding histograms
for n in range(len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc = 0.0, scale = 1.0, size = sample_size)
    axs[n].hist(sample, bins = 100)
    axs[n].set_title('n={}'.format(sample_size))


# In[13]:

plt.figure()
Y  = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
X = np.random.random(size = 10000)
plt.scatter(X,Y)


# In[18]:

# use gridspec to partition the figure into subplots
import matplotlib.gridspec as gridspec
plt.figure()
gspec = gridspec.GridSpec(3,3)

top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:,0])
lower_right = plt.subplot(gspec[1:,1:])


# In[19]:

Y = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
X = np.random.random(size = 10000)
lower_right.scatter(X,Y)
top_histogram.hist(X, bins = 100)
s = side_histogram.hist(Y, bins = 100, orientation='horizontal')


# In[21]:

# clear the histograms and plot normed histograms
top_histogram.clear()
top_histogram.hist(X, bins = 100, normed = True)
side_histogram.clear()
side_histogram.hist(Y, bins = 100, orientation = 'horizontal', normed = True)
# flip the side histogram's x axis
side_histogram.invert_xaxis()


# In[22]:

# change axes limits
for ax in [top_histogram, lower_right]:
    ax.set_xlim(0,1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5,5)


# In[24]:

# Box and Whisker plots
import pandas as pd
normal_sample = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
random_sample = np.random.random(size = 10000)
gamma_sample = np.random.gamma(2,size = 10000)

df = pd.DataFrame({'normal':normal_sample, 'random':random_sample, 'gamma':gamma_sample})


# In[25]:

df.describe()


# In[26]:

plt.figure()
#  create a boxplot of the normal data, assign the output to a variable to supress output
_ = plt.boxplot(df['normal'], whis = 'range')


# In[27]:

# clear the current figure
plt.clf()
# plot boxplots for all three of df's columns
_ = plt.boxplot([df['normal'], df['random'], df['gamma']], whis = 'range')


# In[28]:

plt.figure()
_ = plt.hist(df['normal'],bins = 100)


# In[30]:

import mpl_toolkits.axes_grid1.inset_locator as mpl_il

plt.figure()
plt.boxplot([df['normal'],df['random'],df['gamma']], whis = 'range')
# overlay axis on top of another
ax2 = mpl_il.inset_axes(plt.gca(),width = '60%',height='40%',loc = 2)
ax2.hist(df['gamma'], bins = 100)
ax2.margins(x = 0.5)


# In[31]:

# switch the y axis ticks for ax2 to the right side
ax2.yaxis.tick_right()


# In[32]:

# if 'whis' argument isn't passed, boxplot defaults to showing 1.5 * interquartile(IQR) whiskers with outliers
plt.figure()
_ = plt.boxplot([df['normal'], df['random'], df['gamma']])


# In[34]:

# heatmaps
plt.figure()
Y = np.random.normal(loc = 0.0, scale =1.0, size = 10000)
X = np.random.random(size = 10000)
_ = plt.hist2d(X, Y, bins = 25)


# In[35]:

plt.figure()
_ = plt.hist2d(X,Y, bins = 100)


# In[36]:

# add a color bar legend
plt.colorbar()


# In[46]:

# Animations
import matplotlib.animation as animation

n = 100
x = np.random.randn(n)
# print (x)


# In[47]:

# do the plotting
# FuncAnimation will call this update function very xxx milliseconds
# pass in the frame number, starting with frame zero
def update(curr):
#     check if the current frame is at the end of our list
    if curr == n:
#         see below, a is defined as the FuncAnimation
        a.event_source.stop()
#     clear the current axis with cla
    plt.cla()
# want all of our bins set and evenly spaced, because we're redrawing the animation in each clock tick, 
# we can use the NumPy arange function. This will ensure that the bins don't change. We use the balance of minus 4 to plus 4, in half-step increments. 
    bins = np.arange(-4,4,0.5)
    plt.hist(x[:curr], bins = bins)
#     x and y axis values
    plt.axis([-4,4,0,30])
    plt.gca().set_title('Sampling the Normal Distribution')
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n={}'.format(curr), [3,27])
    


# In[48]:

fig = plt.figure()
# call the FuncAnimation construtor and assign it to a
# if not assign a name to FuncAnimation, then we cannot make the event stop
a = animation.FuncAnimation(fig, update, interval = 100)


# In[60]:

w = np.random.normal(loc = 0.0, scale = 10.0, size = 100)
# print (np.amax(w))
def update_2(curr):
    if curr == n:
        b.event_source.stop()
    plt.cla()
    plt.scatter(w[curr],w[curr]+w[curr])
    plt.axis([np.amin(w),np.amax(w),np.amin(w),np.amax(w)])
    plt.annotate('n={}'.format(curr),[3,27])
fig = plt.figure()
b = animation.FuncAnimation(fig,update_2, interval = 100)


# In[63]:

# Interactivity
plt.figure()
data = np.random.rand(10)
plt.plot(data)
def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('Event at pixels {},{}\nand data{},{}'.format(event.x,event.y, event.xdata,event.ydata))

# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event',onclick)


# In[67]:

from random import shuffle
origins = ['China','Brazil','India','USA','Canada','UK','Germany','Iraq','Chile','Mexico']

shuffle(origins)
# print (origins)
df = pd.DataFrame({'height':np.random.rand(10),'weight':np.random.rand(10),'origin':origins})
df


# In[70]:

plt.figure()
# picker = 5 informs the Matplotlib backend that the mouse doesn't have to click directly on a rendered object 
# that can be up to 5 pixels away and it should find the closest object.
plt.scatter(df['height'],df['weight'],picker = 5)
plt.gca().set_ylabel('Weight')
plt.gca().set_xlabel('Height')


# In[73]:

def onpick(event):
    origin = df.iloc[event.ind[0]]['origin']
    print (df.iloc[event.ind[0]])
    plt.gca().set_title('Selected item came from{}'.format(origin))
# connect pick_event
plt.gcf().canvas.mpl_connect('pick_event',onpick)


# In[ ]:



