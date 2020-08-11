# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""


def shuffle( nums , n):
     
     
     out = []
     for i in range(0,n):
         
         print(i)
         out.append(nums[i])
         
         out.append(nums[n+i])
     
         
    #     print(i)
     
     print(out)
    
        
     
     
     
nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums,n))

[2,3,1,3,4,7]