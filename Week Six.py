# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:35:52 2024

@author: conno
"""



def numcheck():
    try:
        value = float(input("give me a number"))
    except ValueError:
        print("bad")
    else:
        print("Good")
        
i = 1       
while i == 1:      
    numcheck()
    again = input("try again? (y/n)")
    if str.lower(again) == ("y"):
        i = 1
    else:
        i = 0
        
