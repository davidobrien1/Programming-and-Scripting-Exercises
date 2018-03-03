# David O'Brien, 2018-03-03
# Topic 5, Exercise 5
# Please complete the following exercise this week:
# Write a Python script that reads the Iris data set in and prints 
# the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, 
# and these values should have the decimal places aligned, with a space between the columns.


# Attempt No. 1: Reulted in printing all rows as strings

with open("data/iris.csv") as f:      # we are opening the file in this line. "as f" means we have called this file f from now on
  for line in f:                      # looping through the lines in the file
      print(line.split(',')[0:4])     # the ".split" addition to the  "line" splits each line into a Python List
                                      # Adding [0] prints out the first number on each line, changing this to [1] prints out the next column etc.


# Attempt No. 2: Reulted in printing correct answer without the need to format
# Reference: https://stackoverflow.com/questions/40777108/printing-selected-columns-from-a-csv-file-in-python

with open("data/iris.csv") as f:
  for line in f:
    line = line.split(',')                      # here, i split the line before the print function
    print(line[0], line[1], line[2], line[3])   # this prints out the first number, then the second and so on
                                                # Decimal places are aligned with space bewteen columns so no need to format



# Attempt No. 3: Reulted in printing correct answer with formatting functions
# Reference: https://stackoverflow.com/questions/40777108/printing-selected-columns-from-a-csv-file-in-python

with open("data/iris.csv") as f:
  for line in f:
    line = line.split(',')
    print('{:>3} {:>3} {:>3} {:>3}'.format(line[0], line[1], line[2], line[3])) # the > symbol right aligns the text and the number specifies the width of the string.

    