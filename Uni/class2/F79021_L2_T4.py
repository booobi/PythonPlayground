import sys

inputList = sys.argv[1:]
newList = []

for char in inputList:
    if char not in newList:
        newList.append(char)
        
print newList