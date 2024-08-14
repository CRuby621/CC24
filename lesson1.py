# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:47:41 2024

@author: connor
"""

from datetime import date

name = input("what is your Name?")
today = date.today()
num = int(input("What is your favourite number?"))
Bday = input("Enter Day: ")
Bmonth = input("Enter Month: ")
Byear = input("Enter Year: ")

def calculateAge(Bday, Bmonth, Byear):
    today = date.today() #get todays date
    birthdate = date(Byear, Bmonth, Bday) # concat the input into the date format
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

AgeResult = calculateAge(int(Bday), int(Bmonth), int(Byear))

print("you are", AgeResult, "years old!")    
    



#print("your name is", name, "and your favourite number is", num)
print("the next number up is", (num + 1))


