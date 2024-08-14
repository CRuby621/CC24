# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:52:42 2024

@author: conno
"""

import random

diceSide = int(input("What sided dice are you using?"))
DiceAmt = int(input("How many die are you using?"))


def Diceroll(Side, Amt):
    value = 0
    for i in range(0, Amt):
        value += random.randint(1, (Side))
        
    print(str(value))    
        
        
Diceroll(diceSide, DiceAmt)    
    