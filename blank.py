
#https://stackoverflow.com/questions/40777108/printing-selected-columns-from-a-csv-file-in-python

with open("data/iris.csv") as f:
  for line in f:
    line = line.split(',')
    print('{:>3} {:>3} {:>3} {:>3}'.format(line[0], line[1], line[2], line[3]))
    