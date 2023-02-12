#!/usr/bin/python3

def square_numbers(number):
    # check if argument is integer
    assert type(number) == int, 'Argument should be type int'

    if number < 1:
        raise Exception('Number should be greater than zero')

    # find all non negatives less than number
    numbers = range(number)

    # loop through numbers and square each and print it
    for integer in numbers:
        print(integer ** 2)

