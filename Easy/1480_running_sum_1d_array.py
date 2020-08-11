# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""


def runningSum(nums):
        
        sums = 0

        ans = []                
        for i in nums:
            
            sums += i
            
            ans.append(sums)
            
        print(ans)
        

nums = [1,2,3,4]

print(runningSum(nums))


#%%
def runningSum(nums):
        
        sums = 0

        for i in range(1,len(nums)):
            print(i)
            nums[i] = nums[i] + nums[i-1]             
            
        return nums

nums = [1,2,3,4]

print(runningSum(nums))

