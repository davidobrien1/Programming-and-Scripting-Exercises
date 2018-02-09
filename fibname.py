# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "OBrien"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Comments posted in discussion forum week 1 for Fibonacci Exercise Response as follows:
# My name is David, so the first and last letter of my name (D + D = 4 + 4) give the number 8. The 8th Fibonacci number is 21.

# Comments posted in discussion forum week 2 task as follows:
# My surname is OBrien
# The first letter O is number 79
# The last letter n is number 110
# Fibonacci number 189 is 1409869790947669143312035591975596518914
# What does ord() do? - it converts a string of one character only to ASCII value.  Returns Type Error if there is more than one character.  chr() is the opposide of ord() i.e. it gives the corresponding character for a given ASCII code
# example:
# ord('H) returns 72
# chr(72) returns H
