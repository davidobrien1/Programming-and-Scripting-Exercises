# David O'Brien, 2018-03-03
# Topic 5, vidoe 4, splitting strings
# See 7.2 of Python tutorial


with open("data/iris.csv") as f:      # we are opening the file in this line. "as f" means we have called this file f from now on
  for line in f:                      # looping through the lines in the file
      print(line.split(',')[0], end='')  
      
      
# Notes for line 7:  
# there is now blank line between the previous lines. 
# the files new line character and the print commands new line character are both getting printed.  
# Adding "end=''" stops printing out the new line character from the print command. the ".split" addition to the  "line" function splits each line into a Python List
# Adding [0] prints out the first number on each line, changing this to [1] prints out the next column etc.
# look at python turorial to figure out how to remove new line character


