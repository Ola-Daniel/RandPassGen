import random


# A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


#    Main program
uppercaseLetter1 = chr(random.randint(65, 90))   # Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65, 90))
# Place-holder to generate more characters here

# Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2    # + ......
password = shuffle(password)

print(password)