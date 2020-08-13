# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""


#1108. Defanging an IP Address
def defangIPaddr(address):
        
        
        new_add = address.replace(".","[.]")
        
        return new_add
        
        

        
address = "255.100.50.0"


print(defangIPaddr(address))