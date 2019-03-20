import sys

inputList = sys.argv[1:]
foundCharList = []
contains = False

for char in inputList:
    if char in foundCharList:
        contains = True
        break
    else:
        foundCharList.append(char)

print contains