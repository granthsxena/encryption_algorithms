# this algorithm just comverts aplhabets into numbers based on their ord value and randomisation 

import random

def isOdd(length):
    if length % 2 == 0:
        return False
    else:
        return True


def encryption_1(text, key):
    #this algorithm flips the string first
    # replaces the second word

    innitial = text[::-1]
    lyst = []


    for i in innitial:
        lyst.append(i)

    lyst_second_last = lyst[-2]
    lyst_second = lyst[1]

    text_length = len(text)


    if isOdd(text_length):
        #change variable placement
        lyst[1] = lyst_second_last
        lyst[-2] = lyst_second
    else:
        #use randomness here
        divider = random.randint(1,10)
        internal_divider = random.randint(1,10)
        if divider >= 5:
            for i in range(len(lyst)):
                if not isOdd(i):
                    #change the logic here where a becomes
                    lyst[i] = lyst[i].upper()
                    if internal_divider >= 5:
                        lyst[i] = str((ord(lyst[i]) - 3) // 12)
                else:
                    lyst[i] = str((ord(lyst[i])-3)//12)

    final = ''.join(lyst)


    return final

#testing print statements
print(encryption_1("kobe", "cod123"))
