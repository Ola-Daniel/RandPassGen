import random


# A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


#    Main program
uppercaseLetter1 = chr(random.randint(65, 90))   # Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65, 90))
uppercaseLetter3 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
lowercaseLetter3 = chr(random.randint(97, 122))
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))
digit3 = chr(random.randint(48, 57))
digit4 = chr(random.randint(48, 57))
punch1 = chr(46)
punch2 = chr(33)
punch3 = chr(46)
punch4 = chr(33)

# Place-holder to generate more characters here

# Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + lowercaseLetter1 + \
           lowercaseLetter2 + lowercaseLetter3 + digit1 + digit2 + punch1 + punch2 + punch3 + punch4
password = shuffle(password)

print(password)
