#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:23:33 2020

@author: edu
"""
#n = input("Input number: "
def is_even(n) :
    while n:
        if n % 2 == 0 :
            return True
    else:
       return False
    
#%%

def is_odd(n) :
    while n:
        if n % 2 == 1 :
            return True
    else:
       return False
   
#%% Factorial

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

n= int(input("Input interger: "))
print(factorial(n))



#%% Multiples

def multiples(numbers, n):
    
    multi = []
    
    for i in numbers:
        if i % n ==0:
            multi.append(i)
        return multi
        
       
        
numbers= [1,2,3,4,5,6,7,8,9,10,
          11,12,13,14,15,16,17,18,19,20,
          21,22,23,24,25,26,27,28,29,30,
          31,32,33,34,35,36,37,38,39,40,
          41,42,43,44,45,46,47,48,49,50,
          51,52,53,54,55,56,57,58,59,60,
          61,62,63,64,65,66,67,68,69,70,
          71,72,73,74,75,76,77,78,79,80,
          81,82,83,84,85,86,87,88,89,90,
          91,92,93,94,95,96,97,98,99,100]        

