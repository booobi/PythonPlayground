genericDict = {'genericKey' : 'genericValue', 1 : 'one'}
print genericDict['genericKey']
print genericDict[1]

constants = [("pi", 3.14), ("me", 10)]
myDict = dict(constants)

print myDict["pi"]

anotherDict = dict(anotherPi=3.14,anotherMe=10)

print anotherDict["anotherPi"]

x = {}
x[42] = 'fourty-two'
print x

x = {}
y = x
x[1] = 'one'
print y
x.clear()
print y

#copy makes a shallow copy
complicatedDict = {'firstVar':'randomString', 'secondVariable':[1,2,3]}
copyOfComplicatedDict = complicatedDict.copy()
complicatedDict['firstVar'] = 'somethingElse'
print complicatedDict
print copyOfComplicatedDict
complicatedDict['secondVariable'][2] = 20
print complicatedDict
print copyOfComplicatedDict

#fromkeys
keysOnlyDict = dict.fromkeys(['one','two'])
print keysOnlyDict
#change default value of fromkeys
keysOnlyDict = dict.fromkeys(['one','two'], '(unknown)')
print keysOnlyDict

#hasKey
hasKeyDict = {}
print hasKeyDict.has_key('name')
hasKeyDict['name'] = 'MyName'
print hasKeyDict.has_key('name')

#items - returns a list in the form [(key,value), (key,value)]
myDict = {'url':'google.com', 'hits':'10000'}
print myDict.items()

#keys
print myDict.keys()

#pop
print myDict.pop('url')
print myDict

#popitem - like pop, but random, efficient
myDict = {'url':'google.com', 'hits':'10000'}
print myDict.popitem()
print myDict

#setDefault
emails = {'mine':'thisone@ha.com', 'theirs':'theirs@ha.com'}
emails.setdefault('ours')
print emails
emails.pop('ours')
emails.setdefault('ours','ours@ha.com')
print emails

#update
dictToUpdate = {1:'one', 2:'two', 3:'three'}
dictToUpdateWith = {3:'actualThree', 4:'four', 5:'five'}
dictToUpdate.update(dictToUpdateWith)
print dictToUpdate

#iteration
dictToIterate = dictToUpdate.copy()
for k in dictToIterate:
    print k, dictToIterate[k]