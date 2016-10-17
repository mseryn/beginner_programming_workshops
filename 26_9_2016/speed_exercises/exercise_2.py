#!/usr/bin/python3

#***
#*  Speed Exercise 2
#*  26 September 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Instructions:
#*      Make a function that prints all prime numbers between 1 and 100
#***

def print_prime_numbers_in_range(start, finish):
    for number in range(start, finish + 1):
        if number > 1:
            for temp in range(2, number):
                if (number % temp) == 0:
                    break;      # a break here triggers the else clause below
            else:
                # else statements following for loops trigger if for loop
                # terminated due to a break
                print("%i is prime" %number)             

if __name__ == "__main__":
    print_prime_numbers_in_range(0, 100)
