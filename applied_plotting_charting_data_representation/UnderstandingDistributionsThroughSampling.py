
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[100]:

import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib notebook')

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(figsize=(9,3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5);
plt.axis([-7,21,0,0.6])

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')


# In[36]:

# Creates a number of subplots using the pyplot subplots
data1 = np.array([1,2,4,6,8,10,12])
data2 = np.array([0,1,3,5,7,9,11])
data3 = data1**2
data4 = data2**2
data5 = data2*10

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, sharey = True)
ax1.plot(data1,'-o',c='red')
ax2.plot(data2,'-x')
ax2.plot(data5,'r+')
ax3.plot(data3,'-o',c='red')
ax4.plot(data4)


# In[92]:

# Creates a number of subplots using the matplotlib gridspec functionality.
import matplotlib.gridspec as gridspec
plt.figure()
gspec = gridspec.GridSpec(3,4)
top_front = plt.subplot(gspec[0,0])
top_middle = plt.subplot(gspec[0,1:3])
top_end = plt.subplot(gspec[0:,3])
bottom_front = plt.subplot(gspec[1:,0:2])
bottom_middle = plt.subplot(gspec[1:,2:3])


# In[138]:

# plt.clf()
Y = np.random.normal(-2.5, 1, 500)
X = np.random.random(500)
bottom_front.clear()
bottom_front.scatter(X,Y)
top_middle.clear()
top_middle.hist(X,bins = 30, normed = True)
top_end.clear()
top_end.hist(Y, bins = 30, orientation = 'horizontal',normed = True)
top_front.clear()
top_front.plot(data1)
bottom_middle.clear()
bottom_middle.plot(data5,'-o')


# In[153]:

import matplotlib.animation as animation
n = 100
x= [x1,x2,x3,x4]
axis1 = [-7.5,2.5,0,0.6]
axis2 = [0,10,0,0.6]
axis3 = [7,17,0,0.6]
axis4 = [12,22,0,0.6]
axis = [axis1,axis2,axis3,axis4]

bin1 = np.arange(-7.5,2.5,0.2)
bin2 = np.arange(0,10,0.2)
bin3 = np.arange(7,17,0.2)
bin4 = np.arange(12,22,0.2)
bins = [bin1,bin2,bin3,bin4]

anno_x = [-1,6.5,13.5, 18.5]
colors =['green','red','blue','orange']
titles = ['x1 Normal', 'x2 Gamma', 'x3 Exponential', 'x4 Uniform']
def update(curr):
#     check if the current frame is at the end of our list
    if curr == n:
    # see below, a is defined as the FuncAnimation
        a.event_source.stop()
    for i in range(len(ax)):
        ax[i].cla() 
        ax[i].hist(x[i][:100*curr], normed = True, bins = bins[i],color = colors[i])
#     x and y axis values
        ax[i].axis(axis[i])
        ax[i].set_title(titles[i])
        ax[i].set_ylabel('Normed Frequency')
        ax[i].set_xlabel('Value')
        ax[i].annotate('n={}'.format(curr*100), [anno_x[i],0.5])
    plt.tight_layout()



# In[154]:

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
ax = [ax1,ax2,ax3,ax4]
a = animation.FuncAnimation(fig,update, interval = 100)


# In[ ]:



