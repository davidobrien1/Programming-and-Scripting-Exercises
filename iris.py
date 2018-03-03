# David O'Brien, 2018-03-03
# Topic 5, Exercise 5
# Please complete the following exercise this week:
# Write a Python script that reads the Iris data set in and prints 
# the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, 
# and these values should have the decimal places aligned, with a space between the columns.


with open("data/iris.csv") as f:      # we are opening the file in this line. "as f" means we have called this file f from now on
  for line in f:                      # looping through the lines in the file
      print(line.split(',')[0:4])  

# Notes for line 12:   
# the ".split" addition to the  "line" function splits each line into a Python List
# Adding [0] prints out the first number on each line, changing this to [1] prints out the next column etc.

