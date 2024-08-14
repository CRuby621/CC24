
"""
Created on Wed Jul 24 14:27:36 2024

@author: conno
"""

## prime number calculator
# check number from 2 --> int(num ** 0.5 + 1)
# if the remainder is zero it is not a prime


NumInput = int(input("insert a number to check: "))

def IsPrime(num):
     if (num < 2):
         return False
     
     for i in range(2, int(num ** 0.5) + 1):
         if num % i == 0:
             return print("it is not a prime")
         return True
        
if IsPrime(NumInput) == True:
    print("it's a prime")
else:
    print("not a prime")