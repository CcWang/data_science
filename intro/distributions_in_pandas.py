import pandas as pd
import numpy as np

# first argument: times to run, second: the chance we got zero
# np.random.binomial (a,b)
# run a times, return how many times we got b 
print np.random.binomial (4,0.5)

def greater_than_15():
	#  to check if filp coins for 20 times, and do that 10000 times(simulations).
	# what proportion of tht simulations are 15 or greater
	x = np.random.binomial(20, 0.5, 10000)
	answer = (x>15).mean()
	return answer

print greater_than_15()
# unevenly distributions
change_of_tornado = 0.1/100
# in 4000 times, the chance of tornado happened
print np.random.binomial(4000, change_of_tornado)

# to know the chance of tornado happened two days in a row
change_of_tornado = 0.01
days = 1000000
tornado_events = np.random.binomial(1,change_of_tornado,days)
two_days_in_a_row = 0
for j in range(1,len(tornado_events)-1):
	if tornado_events[j] == 1 and tornado_events[j-1] == 1:
		two_days_in_a_row +=1;

print ('{} tornadoes back to back in {} years'.format(two_days_in_a_row,days/365))

#numpy.random.uniform(low = 0.0, high=1.0, size = None)
# Draw samples from a uniform distribution.

# Samples are uniformly distributed over the half-open interval [low, high) (includes low, but excludes high). 
# In other words, any value within the given interval is equally likely to be drawn by uniform. 

print np.random.uniform(0,1)