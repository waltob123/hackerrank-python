#!/usr/bin/python3

def print_format(n):
    '''
    This function takes in n as argument and prints from 1 to n
    each number without ending with new line or spaces.
    '''

    i = 1 # counting number
    while i <= n:
    # loop until i is equal to n
        print(i, end='')
        i += 1

