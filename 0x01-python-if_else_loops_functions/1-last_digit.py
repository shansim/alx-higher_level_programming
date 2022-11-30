#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
for i in number[-1]:
    if i[-1:] > str(5):
        print("Last digit of {} is {} and is greater than 5".format(number, i[-1:]))
    elif i[-1:] == str(0):
        print("Last digit of {} is {} and is 0".format(number, i[-1:]))
    elif i[-1:] < str(6) and i[-1:] != str(0):
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, i[-1:])) 
