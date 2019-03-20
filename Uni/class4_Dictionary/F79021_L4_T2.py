import sys

inputText = sys.argv[1]

resultDict = dict.fromkeys(list(inputText), 0)

for ch in inputText:
    resultDict[ch] += 1

print resultDict