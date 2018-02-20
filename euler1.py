# David O'Brien, 2018-02-20
# Project Euler Prolem 1
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
i = 1

while i < 1000:
  if i % 3 == 0:
    sum = sum + i
  elif i % 5 == 0:
    sum = sum + i
  i = i + 1

print("Sum of miltiples of 3 and 5, less than 1000:", sum)
