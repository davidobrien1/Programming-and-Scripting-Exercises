# David O'Brien, 2018-02-09
# Collatz: https://en.wikipedia.org/wiki/Collatz_conjecture 
# Exercise Description: In the video lectures we discussed the Collatz conjecture. 
# Complete the exercise discussed in the Collatz conjecture video by writing a 
# single Python script that starts with an integer and repeatedly applies the 
# Collatz function (divide by 2 if even, multiply by three and add 1 if odd) using a 
# while loop and if statement. At each iteration, the current value of the integer
#  should be printed to the screen. You can specify in your code the starting 
# value of 17. If you wish to enhance your program, have the program ask the 
# user for the integer instead of specifying a value at the start of your code. 
# Add the script to your GitHub repository, as per the instruction in the 
# Assessments section.

n = int(input("Please enter an integer: ")) # this line defines "n" and asks the user to input an integer.  The int function converts the input to an integer

while n > 1:        # the while statement keeps looping through the code while n > 1 
  if(n % 2 == 0):   # this if statement states that if the remainder of n divided by 2 is equal to 0 i.e an even number
      n = n/2       # n now becomes (n divided by 2) and
      print(n)      # print the value of n
  elif(n % 2 == 1): # the elif statement says that, or else if the remainder of n divided by 2 is equal to 1 i.e an odd number
      n = n * 3 + 1 # n now becomes (n multiplied by 3 plus 1) and
      print(n)      # print the value of n
