# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:58:56 2024

@author: conno
"""

CelsiusInput = int(input("What is your current Temperature? "))
Direction = input("What unit would you like to convert to? ")

def DegConvert(Temp, ToUnit):
    if str.lower(ToUnit) == "celsius":
        ValOut = ((Temp -32) * 9/5) 
    elif str.lower(ToUnit) == "fahrenheit":
        ValOut = ((Temp * (9/5) + 32))
    else:
        return None
    print(ValOut, "in", ToUnit)
    
DegConvert(CelsiusInput, Direction)

    
    
    
