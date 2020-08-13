# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""

"""
1313. Decompress Run-Length Encoded List


"""

def decompressRLElist(nums):
    
    freq = nums[0::2]
    
    val = nums[1::2]
    
    new_list = []
    
    for x,y in zip(freq,val):
         
        new_list = new_list + [y]*x
        
    return new_list


    
    
nums = [1,2,3,4]
print(decompressRLElist(nums))

