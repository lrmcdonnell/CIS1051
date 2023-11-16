
#BLAME POPE GREGORY IN CLASS EXERCISE - 02/21/2023

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


date = input("Please enter a date in MM/DD/YYYY format: ")

#0123456789
#MM/DD/YYYY

month = int(date[0:2])

day = int(date[3:5])

year = int(date[6:])



if month in [4,6,9,11]: #30 day month
    if 0 < day < 31:
        print("Valid date")
    else:
        print("Invalid date")
        print("You have entered a month that has 30 days.")
        
        
elif month in [1,3,5,7,8,10,12]: #31 day month
    if 0 < day < 32:
        print("Valid date")
    else:
        print("Invalid date")
        print("You have entered a month that has 31 days.")
        
        
elif (month == 2): #February 
    if 0 < day < 29:
        print("Valid date")
    elif day == 29 and isLeapYear(year):
        print("Valid date")
    else:
        print("Invalid date.")
        
        
else:
    print("This is not a valid date in the Gregorian calendar.")
        

    
