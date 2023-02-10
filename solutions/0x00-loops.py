#!/usr/bin/python3

def square_numbers(number):
    # find all non negatives less than number
    numbers = range(number)

    # loop through numbers and square each and print it
    for integer in numbers:
        print(integer ** 2)

