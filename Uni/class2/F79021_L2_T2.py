import sys

firstWord = sys.argv[1]
secondWord = sys.argv[2]

firstWordList = list(firstWord.lower())
firstWordList.sort()
secondWordList = list(secondWord.lower())
secondWordList.sort()

print firstWordList == secondWordList