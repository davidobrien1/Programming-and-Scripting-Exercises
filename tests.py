# David O'Brien, 2018-02-23
# Week 5 Exercise 4 - Project Euler Problem 5
# Reference: https://code.mikeyaworski.com/python/project_euler/problem_5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# Write a Python program using for and range to calculate the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20

# returns smallest multiple that is evenly divisible by all numbers from 1 - n
# returns -1 if multiple does not exist

    for i in range(1, 11):
        if isMultiple(i, 2):
            return i
    return -1

# checks every number between 1 and n to see if x is a multiple of every number
# returns True if x is found to be a multiple of every number, and False if x is
# found to not be a multiple of any number
def isMultiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True

# returns the n factorial, or -1 if it does not exist
def factorial(n):
    if n > 1: return n * factorial(n - 1)
    elif n >= 0: return 1
    else: return -1

print (findSmallestMultiple(10)) # 2520
print (findSmallestMultiple(20))