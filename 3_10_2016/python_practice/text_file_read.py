#!/usr/bin/python3

#***
#*  Sample File Input
#*  26 September 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#***

import matplotlib.pyplot


# Playing with text file

file_descriptor = open("test_file.txt", "r")

for line in file_descriptor:
    if line.strip():
        print(line)

file_descriptor.close()
