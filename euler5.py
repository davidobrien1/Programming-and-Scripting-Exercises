# David O'Brien, 2018-02-20
# Topic 4 - Exercise 4 - Problem 5 from Project Euler
# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

a = 0
b = 1

for i in range(1, 11):
  while a % i == 0:
    a = a + b

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:", a)



# Lets try again