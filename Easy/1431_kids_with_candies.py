# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""


def kidsWithCandies(candies, extraCandies):
     
     max_candies = max(candies)
     
     out_table = []
     for i in candies:
         if i + extraCandies >= max_candies :
             
             out_table.append(True)
             
         else:
             out_table.append(False)
             
             
             
             

     print(out_table)
     
     
     
candies  = [2,3,5,1,3] 
extraCandies = 3

print(kidsWithCandies(candies,extraCandies))