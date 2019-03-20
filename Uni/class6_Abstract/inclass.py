# # stepen
# def pow(number, power):
#     if (power == 1):
#         return number
#     else:
#         return number * pow(number, power - 1)

# print pow(2,10)

#fibonachi
fibSeqience = []

def fibs(amountOfNumbers):

    if amountOfNumbers == 1:
        otgovor = 0
    elif amountOfNumbers == 2:
        otgovor = 1 + fibs(1)
    else:
        return fibs(amountOfNumbers - 1) + fibs(amountOfNumbers - 2)

    fibSeqience.append(otgovor)
    return otgovor
 
fibs(3)
print fibSeqience

#palindrom
