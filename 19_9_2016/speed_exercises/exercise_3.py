#!/usr/bin/python3

#***
#*  Speed Exercise 3 -- Example Exercise
#*  19 September 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Instructions:
#*      Make a class called coin. Give it a property “value” and a function called 
#*      flip(). Have flip() return “Heads” 50% of the time and “Tails” 50% of the time.
#*      (Hint: random numbers might help.)
#***

import random

class Coin():
    def __init__(self, input_value):
        self.value = input_value

    def flip(self):
        if random.random() < 0.5:
            return "Heads"
        else:
            return "Tails"

def test_coin_init():
    test_coin = Coin("Test Value")
    if (test_coin.value != "Test Value"):
        print("test_coin_init failed to initialize value correctly")
        return 1
    return 0

def test_coin_flip():
    test_coin = Coin("Test Value")
    flip_value = test_coin.flip()
    if (flip_value != "Heads") and (flip_value != "Tails"):
        print("test_coin_flip failed to give an appropriate value")
        return 1
    return 0


if __name__ == "__main__":
    print("Running example unit tests for Coin class")
    if (test_coin_init() == 0) and (test_coin_flip() == 0):
        print("All tests ran correctly!")
