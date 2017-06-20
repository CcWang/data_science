
# coding: utf-8

# In[14]:

import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages=['Python','SQL','Java','C++',"JavaScript"]
pos = np.arange(len(languages))
popularity = [56,39,34,34,29]
#  change the bar colors to be less bright blue
bars = plt.bar(pos,popularity,align='center', linewidth = 0, color="lightslategrey")

# make one bar, the python bar, a contrasting color
bars[0].set_color('#1F77B4')

plt.xticks(pos,languages)
# TODO: remove the Y label since bars are directly labeled
# plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)


# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top='off',left='off',bottom='off',right='off',labelleft='off',labelbottom='on')
# TODO: remove the frame of the chart
# my way 
# a=plt.gca()
# a.set_frame_on(False)

# the answer from proferssor
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# TODO: direct label each bar with Y axis values
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%', 
                 ha='center', color='w', fontsize=11)
plt.show()


# In[3]:




# In[ ]:



