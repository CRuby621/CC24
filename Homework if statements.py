

from datetime import date

Bday = input("Enter Day: ")
Bmonth = input("Enter Month: ")
Byear = input("Enter Year: ")

def calculateAge(Bday, Bmonth, Byear):
    today = date.today() #get todays date
    birthdate = date(Byear, Bmonth, Bday) # concat the input into the date format
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

AgeResult = calculateAge(int(Bday), int(Bmonth), int(Byear))

if (AgeResult >= 18):
    print("you can go to the races")
elif (AgeResult < 18) and (AgeResult >= 13):
    print("you must get permission from a parent")
elif (AgeResult < 13):
    print("You must be with a responsible adult")    
    5