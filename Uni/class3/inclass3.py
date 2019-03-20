# Caesar
# textToCypher = "ATACKATDOWN"
# offset = 3
# CaesarCypheredText = ""

# for letter in textToCypher:
#     CaesarCypheredText += chr(65 + ((ord(letter) - 65) + offset) % 26)

# print CaesarCypheredText


# Vegenere
textToCypher = "ATACKATDOWN"
key = "LEMON"

cypheredText = ""
for index, letter in enumerate(textToCypher):

    letterPos = ord(letter) - 65
    letterOffset = ord(key[index % len(key)])

    # cypheredText += (ord(letter) - 65)
