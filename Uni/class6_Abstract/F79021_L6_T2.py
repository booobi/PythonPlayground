import sys

inputNumber = int(sys.argv[1])
inputPower = int(sys.argv[2])

def pwr(number, power):
    if power == 1:
        return number
    else:
        return number * pwr(number, power-1)

print pwr(inputNumber, inputPower)