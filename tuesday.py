# David O'Brie, 2018-02-09
# Is it Tuesday?
# Date Time Ref:  https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python

import datetime

if datetime.datetime.today().weekday() == 1:
  print("Yay! It is Tuesday.")
else:
  print("Unfortunately it is not Tuesday.")