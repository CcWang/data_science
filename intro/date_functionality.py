import pandas as pd
import numpy as np

print "Timestamp"
print pd.Timestamp('5/21/2017')

print "Period"
print pd.Period('3/5/2016')

print "DatetimeIndex"
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
print t1
print type(t1.index)