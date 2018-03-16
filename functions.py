def sumall(upto):
  sumupto = 0
  for i in range(1, upto + 1):
    sumupto = sumupto + i
  return sumupto

print("The sum of the values from 1 to 50 inclusive is: ",sumall(50))
print("The sum of the values from 1 to 5 inclusive is: ",sumall(5))
print("The sum of the values from 1 to 10 inclusive is: ",sumall(10))




sum5 = 0 
for i in range(1, 6):
  sum5 = sum5 + i
print("The sum of the values from 1 to 5 inclusive is: ",sum5)


sum10 = 0 
for i in range(1, 11):
  sum10 = sum10 + i
print("The sum of the values from 1 to 10 inclusive is: ",sum10)