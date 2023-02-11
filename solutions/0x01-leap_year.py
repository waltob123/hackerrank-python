#!/usr/bin/python3

def is_leap(year):
    leap = False # initially set leap to false

    # Check if year is leap or not using Gregorian calendar conditions
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
