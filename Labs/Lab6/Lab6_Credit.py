
#LAB 6 - MARIO, CASH, CREDIT



#CREDIT - more comfortable

# I. CHECKSUM-----------------------------------------------
def checkSum(num):

    #####   first sum   #####
    l1 = num[-2::-2]    #takes every other digit starting at second to last
    digits = []         
    s1 = 0              #accumulator for first sum
    for number in l1:   #multiply each num by 2 and make a list of resulting digits
        number = str(int(number) * 2)
        digits += [int(i) for i in number]

    for digit in digits:
        s1 += digit     #calculate sum of digits

    #####   second sum  ######   
    l2 = num[-1::-2]    #takes every other digit starting from last digit
    s2 = 0              # accumulator for second sum

    for digit2 in l2:
        digit2 = int(digit2)
        s2 += digit2    #calculate sum of digits

    #####    total     #####

    checksum = s1 + s2

    if checksum % 10 == 0:
        print("valid")
    else:
        print("invalid")
        return False
        

# II. CARD TYPE AND LENGTH----------------------------------
def cardFormat(num):
    length = len(num)   #get length of card number
    firstdigit = int(cardNum[0])    #get first digit of card number
    first2digits = int(cardNum[0:2:1])  #get first 2 digits of card number

    if (length == 15 and first2digits in [34, 37]): 
        print("AMEX")
    elif ((length == 13 or length == 16) and firstdigit == 4):
        print("VISA")
    elif (length == 16 and first2digits in [51, 52, 53, 54, 55]):
        print("Mastercard")
    else:
        print("invalid")


def checkCard(num):
    if checkSum(num) != False:
        cardFormat(num)
    


#RUN
cardNum = 'banana'
while cardNum.isdigit() == False:
    cardNum = input("Please enter a credit card number: ")  #user input
checkCard(cardNum)
        
    

