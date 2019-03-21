import sys

startIndex = int(sys.argv[1])
endIndex = int(sys.argv[2])

resultSequence = []
calculatedFibNumbers = {}

def fibs(number):
    if calculatedFibNumbers.get(number) != None:
        # print "Used the stored number", calculatedFibNumbers[number], "at position", number 
        return calculatedFibNumbers[number]
    elif number == 1:
        answer = 0
    elif number == 2:
        answer = 1 + fibs(1)
    else:
        answer = fibs(number - 1) + fibs(number - 2)
    
    # print "Stored the number", answer, "at position", number
    calculatedFibNumbers[number] = answer
    return answer

for i in range(startIndex,endIndex+1):
    resultSequence.append(fibs(i))

print resultSequence