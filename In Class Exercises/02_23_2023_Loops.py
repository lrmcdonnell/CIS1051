#IN CLASS EXERCISE - 02/23/2023


#1 - NUMBER OF VOWELS
def numVowels(word):
    count = 0
    vowels = ['a','e','i','o','u']
    word = word.lower()
    for letter in word:
        if letter in vowels:
            count+= 1
    return count

print(numVowels('hello'))




#2 - NUMBER OF EVEN DIGITS
def numEvenDigits(num):
    count = 0
    for digit in str(num):
        if int(digit)%2 == 0:
            count += 1
    return count

    #other way to do it:
def numEvenDigits2(num):
    count = 0
    while num > 0:
        lastDigit = num%10
        if lastDigit % 2 == 0:
            count +=1
        num = num//10
    return count

print(numEvenDigits(24567))




#3 - THREE DIGIT ARMSTRONG NUMBERS
def isArmstrong(num):
    total = 0
    orig = num
    while num > 0:
        lastDigit = num % 10
        total = total + lastDigit ** 3
        num = num // 10
    if total == orig:
        return True
    else:
        return False

print(isArmstrong(371))


#4 - RIDDLER
def riddler():
    for num in range(1001,10000,2):
        thou = num // 1000
        hund = num%1000 // 100
        tens = (num%100) // 10
        ones = num % 10
        if thou != hund and thou != tens and thou != ones and hund != tens and hund != ones and tens != ones:
            if 3 * tens == thou:
                if thou + hund + tens + ones == 27:
                    print(num)
riddler()
            

