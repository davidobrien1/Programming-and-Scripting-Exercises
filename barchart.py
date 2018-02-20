# David O'Brien, 2018-02-10
# Create a bar chart
# https://pythonspot.com/matplotlib-bar-chart/

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('David', 'Una', 'Padraic', 'Amy')
y_pos = np.arange(len(objects))
age = [32,33,3,1]
 
plt.bar(y_pos, age, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Age')
plt.title("O'Brien Family Ages")
 
plt.show()