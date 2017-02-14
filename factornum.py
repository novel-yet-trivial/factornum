#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Factoring a whole number and other functions
Chris Whitling
LE: 2/9/17
v2.2

MIT License

Copyright (c) 2017 Chris Whitling

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import print_function
try:
    input = raw_input # python2
except NameError:
    pass # python 3

import math
import time

def is_square(number):
    """checks if a number is a perfect square"""
    square_root = math.sqrt(number)    #takes the square root of the users number to see if its a perfect square
    return int(square_root) == number #checks to see if the users number is a perfect square

def factor(number):
    """Takes in one int, returns a generator of factors"""

    if number < 1:
        raise ValueError("Number must be greater than zero")

    number_count = 1    #sets the number count = to 1
    factor_a = 2    #defines the initial factor a which will be redefined in the first loop
    while number_count < factor_a:    #this is the only line that changes, as it doesnt diplay the number*itself at the end
        if number % number_count == 0:
            factor_a = (number // number_count)
            yield number_count
            yield factor_a
        number_count += 1

def print_factors(number):
    """Takes a one int, factors it, then
     prints the list of factors to the console in a user readable format"""
    factors = factor(number)
    for i in factors:
        print("{:<4}{}".format(i, next(factors)))

def is_prime(number):
    """Takes in one int, returns True if prime or False if not"""
    next(factors) # throw out the first 2 factors
    next(factors)
    for _ in factors:
        return False # as soon as a 3rd factor is found, return False
    return True

def cli():
    try:
        number = int(input('Please enter number to recieve factors: '))  #this is the users number to be factored
        print_factors(number)
    except ValueError as e:
        #~ print("Please enter a positive integer")
        print("ERROR:", e)

def repeat():
    while True:
        u_input = input('Would you like another number factored? \n Yes or No:')    #prompts user, gives options, and takes user input
        if u_input.lower().startswith('n'):    #defines the end command
            return False
        elif u_input.lower().startswith('y'):   #defines the continue command
            return True
        else:    #loops the program back if the input isnt expected
            print ('Sorry, try again')

def main():
    while True:
        cli()
        if not repeat():
            break
    print ('Thanks for using')    #displays an ending message

if __name__=='__main__':
    main()
