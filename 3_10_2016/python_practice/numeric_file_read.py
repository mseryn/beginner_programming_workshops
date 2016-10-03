#!/usr/bin/python3

#***
#*  Sample File Input
#*  26 September 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#***

import matplotlib.pyplot


# Playing with numeric text file

file_descriptor = open("test_numeric_file.txt", "r")
data = []
for line in file_descriptor:
    data.append(float(line.strip()))

matplotlib.pyplot.plot(data)
matplotlib.pyplot.show()

file_descriptor.close()
