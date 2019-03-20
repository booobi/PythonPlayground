# 1

# myList = [1,2,2,3,4,5,6,6,6,7]

# isSorted=True
# for i in range(len(myList)-1):
#     if(myList[i]>myList[i+1]):
#         isSorted = False
#         break

# print isSorted

# 2

wordList1 = list("rocket boys".lower())
wordList2 = list("october sky".lower())

areSimilar = True
for i in range(len(wordList1)):
    if wordList1[i] in wordList2:
        print "Found occurance of ", wordList1[i]
        wordList2.remove(wordList1[i])
    else:
        areSimilar = False
        break

print areSimilar

# 3
# myList = [5, 3, 1, 5, 9, 2, 8, 6, 7]
# testList = []
# containsMoreThanOne = False

# for i in range(len(myList)):
#     if (myList[i] in testList):
#         containsMoreThanOne = True
#         break
#     else:
#         testList.append(myList[i])

# print containsMoreThanOne

# 4
# myList = [6, 3, 7, 4, 7, 4, 7, 4, 8, 4, 3, 8, 4, 3, 8, 3, 9, 4, 3]
# resultList = []

# for i in range(len(myList)):
#     if(myList[i] not in resultList):
#         resultList.append(myList[i])

# print resultList