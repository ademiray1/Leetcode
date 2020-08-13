# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""

"""

Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

"""


def numberOfSteps (num):
    
    num_step= 0
 
    while num != 0 :
        if num % 2 == 0:
            num = num/2
            num_step +=1
        else:
            num = num-1
            num_step+=1
    return num_step
            
        

print(numberOfSteps(14))


#%%


def numberOfSteps (num):
    
    c =0
    while num != 0:
               
        num, c = num-1 if num % 2 else num//2, c+1
    return c
            
       
print(numberOfSteps(14))

