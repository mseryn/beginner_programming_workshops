#!/usr/bin/python3

#***
#*  Speed Exercise 3
#*  26 September 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Instructions:
#*      Make a script that takes a string from the user and prints how many 
#*      characters it contains.
#***

if __name__ == "__main__":
    input_string = input("Enter your string: ")
    print("%s has %i characters" %(input_string, len(input_string)))
