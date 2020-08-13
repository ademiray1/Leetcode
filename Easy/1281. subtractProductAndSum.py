# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""

import math

def subtractProductAndSum(n):
    
    multip = 1
    new_multip = []
    
    for i in str(n):
        
        new_multip.append(int(i))
        
    for x in new_multip:
        multip = multip*x
    
    sum_list = sum(new_multip)
    
    difference = multip - sum_list
    
    print(difference)
        
   
    
    
    
n = 234
print(subtractProductAndSum(n))    


#%%

def subtractProductAndSum(n):

    prod = 1
    sum = 0
    
    for i in str(n):
        prod = prod*int(i)
        sum = sum + int(i)
        
    return prod - sum

n = 234
print(subtractProductAndSum(n))    

        