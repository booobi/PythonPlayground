import sys

inputWord = sys.argv[1].lower()

def isPalindrom(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and isPalindrom(word[1:-1])

print isPalindrom(inputWord)