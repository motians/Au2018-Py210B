#!/usr/bin/env python3
#Week2 Excercise #2
#Student: Brandon Nguyen - Au2018
def fibonacci(n):
    """
    The function have one parameter n which represents the index.
    The function returns the nth's value of the index n in fibonacci series (starting with zero indiex).
    0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    if (n==0 or n==1): 
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def lucas(n):
    """
    The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. 
    The resulting series looks like this:2, 1, 3, 4, 7, 11, 18, 29, ... similiar to f(n)=f(n-1)+f(n-2)
    The function lucas returns the nth value in the lucas numbers series (starting with zero index).
    """
    if (n==0 or n == 1):
        return abs(n-2)
    else:
        return lucas(n-1) + lucas(n-2)
        

