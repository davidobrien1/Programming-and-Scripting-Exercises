# David O'Brien, 02018-03-02
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# Examples taken from 7.1

s = 'Hello, world.'
str(s)
'Hello, world.'
repr(s)
"'Hello, world.'"
str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

for x in range(1, 11):
  print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
# Note use of 'end' on previous line
print(repr(x*x*x).rjust(4))