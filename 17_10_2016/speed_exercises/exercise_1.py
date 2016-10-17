#!/usr/bin/python3

#***
#*  Speed Exercise 1 
#*  17 October 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Instructions:
#*      Read from the file exercise_1_inputs.txt. Each line is an integer. 
#*      Average these integers, and print the average.
#***

import statistics

if __name__ == "__main__":
    input_values = []
    inputs = open("exercise_1_inputs.txt", "r")
    for line in inputs:
        input_values.append(float(line.strip()))
    average = statistics.mean(input_values)
    print("The average is %f" %(average))
