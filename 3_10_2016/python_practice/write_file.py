#!/usr/bin/python3

#***
#*  Sample File Output
#*  26 September 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#***

import random
import math
import matplotlib.pyplot

clean_data = []
noisy_data = []

file_descriptor = open("noisy_sin_data.txt", "w")

x_points = [x*0.01 for x in range(0, 700)]
for point in x_points:
    clean_data_point = math.sin(point)    
    if random.random() > 0.5:
        noisy_data_point = math.sin(point) + 0.25 * random.random()    
    else:
        noisy_data_point = math.sin(point) - 0.25 * random.random()    
    clean_data.append(clean_data_point)
    noisy_data.append(noisy_data_point)

matplotlib.pyplot.plot(x_points, clean_data)
matplotlib.pyplot.plot(x_points, noisy_data)
matplotlib.pyplot.show()

file_descriptor.write("CLEAN DATA:\n")
for point in clean_data:
    file_descriptor.write("%s\n" %(str(point)))
file_descriptor.write("NOISY DATA:\n")
for point in noisy_data:
    file_descriptor.write("%s\n" %(str(point)))

file_descriptor.close()
