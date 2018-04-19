# David O'Brien 2018-04-08
# Old faithful analysis

# Calculate the mean of each column.
import numpy

# read data file into array.
data = numpy.genfromtxt('data/faithful.csv', delimiter=',')

firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])
print("Average of first column is: ", meanfirstcol)

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()