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

import math
import time
 

def is_square(number):
    perfect_square = math.sqrt(number)    #takes the square root of the users number to see if its a perfect square
    square_check = number % perfect_square    #checks to see if the users number is a perfect square
    
    if square_check == 0:
        return True
    else:
        return False

def factor(number):   
    """Takes in one int, returns a list of factors"""
    
    factors = []
    
    if number <= 0:
        return ('Invalid number')
    else:
        number_count = int(1)    #sets the number count = to 1
        factor_a = (2)    #defines the initial factor a which will be redefined in the first loop
    
        
        if is_square(number):    #this is the factoring loop for perfect squares, it displays the number*itself at the end
            while number_count <= factor_a:
                 if number % number_count == 0:
                    factor_a = (number /int(number_count))    #devides number by number_count to get both factors
                    factors.append(number_count)
                    factors.append(factor_a)
                 number_count += 1    #advances the count by 1
        else:    #this is the loop for non-perfect squares
            while number_count < factor_a:    #this is the only line that changes, as it doesnt diplay the number*itself at the end
                 if number % number_count == 0:
                    factor_a = (number / number_count)
                    factors.append(number_count)
                    factors.append(factor_a)
                 number_count += 1
        return factors

def print_factors(number):
    """Takes a one int, factors it, then
     prints the list of factors to the console in a user readable format"""
    
    factors = factor(number)
    
    if factors == 'Invalid number':
        print("Invalid number, please try again")
    else:
        for i in range(0, int((len(factors))), 2):
            print (factors[i], factors[i+1])

def is_prime(number):
    """Takes in one int, returns True if prime or False if not"""
    
    factors = factor(number)
    if len(factors) == 2:
        return True
    else:
        return False

def main():
    master = True
    while master:
    
        number = int(input('Please enter number to recieve factors: '))  #this is the users number to be factored 
        print_factors(number)
        
        end = True    #establishes the end loop counter
        while end:
            u_input = str(input('Would you like another number factored? \n Yes or No:'))    #prompts user, gives options, and takes user input
        
            if u_input.lower() == 'no' or u_input.lower() == 'n':    #defines the end command 
                master = False
                end = False
        
            elif u_input.lower() == 'yes' or u_input.lower() == 'y':   #defines the continue command
                end = False
        
            else:    #loops the program back if the input isnt expected
                print ('Sorry, try again')
    
    print ('Thanks for using')    #displays an ending message
    time.sleep(1)



if __name__=='__main__':
    main()
