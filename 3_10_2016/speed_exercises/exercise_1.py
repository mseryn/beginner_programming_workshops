#!/usr/bin/python3

#***
#*  Speed Exercise 1
#*  26 September 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Instructions:
#*      Make a function that counts to 15 and prints each odd number.
#***

counter = 1

while counter <= 15:
    if counter%2 == 1:
        print(counter)
    counter += 1
