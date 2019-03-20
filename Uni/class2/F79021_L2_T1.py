import sys

try:
        inputList = [int(possibleNum) for possibleNum in sys.argv[1:]]
except ValueError:
        inputList = sys.argv[1:]

isSorted = True
for i in range(len(inputList)-1):
        if(inputList[i]>inputList[i+1]):
                isSorted = False
                break

print 'sorted' if isSorted else 'unsorted'