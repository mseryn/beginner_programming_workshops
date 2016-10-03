#!/usr/bin/python3

#***
#*  Sample File Input
#*  26 September 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#***

import matplotlib.pyplot


# Playing with formatted text file

file_descriptor = open("test_formatted_numeric_file.txt", "r")
x_data = []
y_data = []
for line in file_descriptor:
    x_data.append(float(line.strip().split()[0]))
    y_data.append(float(line.strip().split()[1]))
        
matplotlib.pyplot.plot(x_data, y_data)
matplotlib.pyplot.show()

file_descriptor.close()
