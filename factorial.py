# David O'Brien, 2018-03-16
# Write a Python script containing a function called 
# factorial() that takes a single input/argument which 
# is a positive integer and returns its factorial. 
# The factorial of a number is that number multiplied 
# by all of the positive numbers less than it. 
# For example, the factorial of 5 is 5x4x3x2x1 which 
# equals 120. You should, in your script, test the function
#  by calling it with the values 5, 7, and 10.


def factorial(x):   # this line defines the function 'factorial' where x is the input value
  factorialx = 1
  for i in range(2, x+1):   # loop through the range 1 to the inputted value
    factorialx = factorialx * i   # update the value of factorialx by multiplying be the next value in the for loop
  return factorialx     # returns the final value of factoralx after going through all values in the for loop
print("The factorial of 5 is: ",factorial(5))   # prints the statement in double quotes and returns the factorial value of the input 5
print("The factorial of 7 is: ",factorial(7))   # prints the statement in double quotes and returns the factorial value of the input 7
print("The factorial of 10 is: ",factorial(10))   # prints the statement in double quotes and returns the factorial value of the input 10