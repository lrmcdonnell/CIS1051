
#LAB 7 - HAWAIIAN PRONUNCIATION

vowels = {'a': 'ah',
          'e': 'eh',
          'i': 'ee',
          'o': 'oh',
          'u': 'oo'}

double_vowels = {'ai': 'eye',
                 'ae': 'eye',
                 'ao': 'ow',
                 'au':'ow',
                 'ei':'ay',
                 'eu': 'eh-oo',
                 'iu': 'ew',
                 'oi': 'oyo',
                 'ou': 'ow',
                 'ui': 'ooey',}

w = {'iw': 'v',
     'ew': 'v'}

valid_chars = ['a', 'e', 'i', 'o', 'u', 'p', 'k', 'h', 'l', 'm', 'n', 'w', "'", ' ']

consonants = ['p', 'k', 'h', 'l', 'm', 'n', 'w', "'"]



#I. CHECK IF WORD IS VALID
def is_valid(word):
    word = word.lower()
    for letter in word:
        if letter not in valid_chars:
            print(letter, "is not a valid Hawaiian character.")
            return False
    return True


#II. PRONOUNCE WORD
def pronounce(word):
    word = word.lower()
    output = ""
    i = 0 #i = index
    while i < (len(word)):
        if word[i:i+2]in double_vowels:
            output = output + double_vowels[word[i:i+2]] + '-'
            i = i+1
        elif word[i] in vowels and word[i:i+2] not in double_vowels and word[i-1:i+1] not in double_vowels:
            output = output + vowels[word[i]] + '-'
        elif word[i] in vowels and word[i-1:i+1] in double_vowels:
            output = output + vowels[word[i]] + '-'
        elif word[i] in consonants and word[i-1:i+1] not in double_vowels:
            output = output + word[i]
        elif word[i:i+2] in w and word[i-1:i+1] not in double_vowels:
            output = output + w[word[i:i+2]] + '-'
        i = i + 1
    output = output[:-1].replace("-'","'")
    print(word.upper(), 'is pronounced as: ', output)
    return output


def Hawaiian(word):
    ask = 'y'
    if is_valid(word) == True:
        pronounce(word)

text = input("Please enter a Hawaiian word to pronounce: ")
Hawaiian(text)

ask = 'y'
while ask != 'n':
    ask = input('Would you like to enter another word? Type "y" for YES and "n" for NO: ') 
    if ask != 'n':
        text = input("Please enter a Hawaiian word to pronounce: ")
        Hawaiian(text)
    else:
        break
   

