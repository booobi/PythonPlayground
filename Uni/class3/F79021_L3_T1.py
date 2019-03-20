import sys

textToCypher = sys.argv[1]
offset = int(sys.argv[2])

cypheredText = ""

for letter in textToCypher:
    cypheredText += chr(65 + ((ord(letter) - 65) + offset) % 26)

print cypheredText
