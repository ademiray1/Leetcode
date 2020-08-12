# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""

"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

"""

def numIdenticalPairs(nums):
    
    count = 0
    for i in range(len(nums)):
        
        for j in range(i+1,len(nums)):
            
              #print (nums[j])  
              if nums[i] == nums[j]:
                
                count +=1
     #     print (i)             
    return count
    
    
    
    
nums = [1, 2, 3, 1,1,3]

print(numIdenticalPairs(nums))


#%%
def numIdenticalPairs(nums):
    nums.sort()
    print(nums)
    i = 0
    count = 0
    
    for j in range(1,len(nums)):
#        print(j)
        
        if nums[i]==nums[j]:
            count += j-i
        else:
            i=j
           
    return count
    

nums = [1, 2, 3, 1,1,3,1,2,3,2]
nums.sort()
print(nums)


print(numIdenticalPairs(nums))

        