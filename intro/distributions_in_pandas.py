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