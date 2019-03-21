# Recursive Binary Search
import sys

inputList = [30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256, 263, 272, 288, 289, 290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444, 486, 493, 497, 499, 510, 513, 514, 519, 521, 521, 535, 546, 552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692, 711, 713, 731, 739, 740, 842, 858, 885, 887, 888, 893, 898, 900, 903, 908, 909, 959, 988]

# testList = [1,2,3,4,5]
inputNumber = int(sys.argv[1])

def recursiveBinarySearch(listToSearch, numberToSearch):
    if listToSearch[len(listToSearch)/2] == numberToSearch:
        print "found at", len(listToSearch)/2
    elif numberToSearch < listToSearch[len(listToSearch)/2]:
        recursiveBinarySearch(listToSearch[:len(listToSearch)/2], numberToSearch)
    elif numberToSearch > listToSearch[len(listToSearch)/2]:
        recursiveBinarySearch(listToSearch[len(listToSearch)/2:], numberToSearch)
    
recursiveBinarySearch(inputList,inputNumber)


# [1,2,3,4] - looking for 3
# found at 2

# [1,2,3,4,5] - looking for 1
# [1,2,3]
# [1,2]
# 

# [1,2,3,4,5,6] - looking for 6
# [4,5,6]
# [5,6] - found at 1 

# [1,2,3,4,5,6] - looking for 4
# [4,5,6]
# [5,6] - found at 1 

# [1,2,3,4,5] - looking for 4
# [3,4,5] - found at 1