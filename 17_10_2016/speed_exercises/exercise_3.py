#!/usr/bin/python3

#***
#*  Exercise 2 
#*  17 October 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Instructions:
#*      Read the file dictionary_inputs.txt. Each line is a key, value pair 
#*      separated by a space. Store the values under their key in a dictionary. 
#*      Print the dictionary.
#*      Take an input from the user. If it’s a key, print that key’s value.
#***


if __name__ == "__main__":
    input_dictionary = {}
    input_key = None
    input_value = None
    input_pair = []

    inputs = open("dictionary_inputs.txt", "r")

    for line in inputs:
        input_pair = line.strip().split()
        input_key = input_pair[0]
        input_value = input_pair[1]
        input_dictionary[input_key] = input_value

#    print(input_dictionary)        

    user_input = input("English Key: ")
    if user_input in input_dictionary:
        print("French Value: %s" %(input_dictionary[user_input]))
    else:
        print("Key %s not in dictionary, sorry." %(user_input))
