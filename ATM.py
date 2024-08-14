# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

UsercardAuth = 404
User404Pin = 2222
User404 = [1000, 555, 333]

def CardRead():
    print("reading card.")
    return 404



def PinCheck():
    attempts = 0
        
    ReadINSCard = CardRead()    #reads auth number off card
    
    if ReadINSCard == UsercardAuth:  # if it is correct continue
        while attempts < 3:   #while the user hasn't exceeded their attempts
            INPin = 0000   #reset pin to 0000 with each attempt
            if attempts == 0:  # if it is the first attempt
                attempts += 1 # iterate attempts +1 
                INPin = int(input("What is your pin? "))   #ask for pin
                if INPin == User404Pin: # if pin is correct
                    return True # return Main() = true
                if INPin != User404Pin: # if the pin is incorrect
                    continue # next loop
                    
            else:
                attempts += 1 # iterate attempts +1 
                INPin = int(input("Incorrect pin. Please try again. ")) #read new pin
                if INPin == User404Pin: # if pin is correct
                    return True # return main() = true
                else: # if pin is incorrect
                    continue # next loop
                
                
                

input("Please insert card: ")
correct = PinCheck()   # the correct variable stores the true/false returned from pincheck()
if correct == True: #if the pin is correct
     AccType = input("What account do you want to withdraw from? (credit/cheque/savings): ")
     if str.lower(AccType) == "credit": # if the specified acc type is credit
        MoneyValue = User404[0] # access the value in the first index on their account
        AccIndex = 0
        
     elif str.lower(AccType) == "cheque": # if the specified acc type is cheque
        MoneyValue = User404[1] # access the value in the second index on their account
        AccIndex = 1
        
     elif str.lower(AccType) == "savings": # if the specified acc type is savings
        MoneyValue = User404[2] # access the value in the third index on their account
        AccIndex = 2
        
     OutAmount = int(input("How much would you like to withdraw? ")) # assign the outamount to how much the user wants to withdraw
     if MoneyValue >= OutAmount: # if the amount they want to withdraw is less than what's in the account
         User404[AccIndex] = (MoneyValue - OutAmount)
         print("The new balance of your", AccType, "account is", (User404[AccIndex])) # update and print new balance
     else: # if the amount they want to withdraw is greater than that of the account
         while True: #infinite loop until broken
           OutAmount = int(input("Invalid amount. Please enter amount to withdraw: "))  # pester for new value
           if OutAmount <= MoneyValue: #if they get it right
               break # exit the while loop
         User404[AccIndex] = (MoneyValue - OutAmount)
         print("The new balance of your", AccType, "account is", (User404[AccIndex]))
           

else:
    print("Destroying card")
    
    
    
    
                
                
                
                
    
    
    
    
    
    
    

