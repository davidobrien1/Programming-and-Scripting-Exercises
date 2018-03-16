# David O'Brien, 2018-03-02
# Video 3 - formatting
# examples from 7.1 of python tutorial

for i in range(1,11): # the for statement loops through each of the numbers from 1 to 10
  print('{:2d} {:3d} {:4d} {:5d}'.format(i, i**2, i**3, i**4)) # this format notation allows
 
a = 5
print(f'The value of a is {a} and a+1 is {a+1}') #f means treat the following string differently than usual - it it allows you to put variables from your code into the f string

for i in range(1, 11):
  print(f'{i} {i**2} {i**3} {i**4}')