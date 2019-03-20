import sys

valueToSearch = sys.argv[1]

d={1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'}

resultList = []
for k in d:
    if d[k] == valueToSearch:
        resultList.append(k)

print resultList