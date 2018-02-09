# David O'Brien, 2018-02-09
# Collatz: https://en.wikipedia.org/wiki/Collatz_conjecture

n = int(input("Please enter an integer: "))

while n > 1:
  if(n % 2 == 0): 
      n = n/2     
      print(n)
  elif(n % 2 == 1):
      n = n * 3 + 1
      print(n)
