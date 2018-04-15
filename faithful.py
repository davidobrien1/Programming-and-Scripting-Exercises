# David O'Brien 2018-04-08
# Old faithful analysis

# Calculate the mean of each column.
import numpy

# read data file into array.
data = numpy.genfromtxt('data/faithful.csv', delimiter=',')

firstcol = data[:,0]
meanfirstcol = data[:,0]
