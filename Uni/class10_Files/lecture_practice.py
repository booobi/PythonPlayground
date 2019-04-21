import sys

# text = sys.stdin.readlines()
# for line in text:
#     print line


f = open("./FStestOne", "w")
try:
    f.write("Hellow, ")
    f.write("world!")
finally:
    f.close()


f = open("./FStestOne", "r")
print f.read(5) # Hello
print f.read(1) # w
print f.read()  #, world!
f.close()

f = open("./FStestOne", "r")
print f.readlines() # all lines read and buffered
print f.readline() # nothing
print f.readlines() # empty list
f.close()

#read char
f = open("./FStestOne", "r")
ch = f.read(1)
while ch:         # for ch in f.read()
    print ch
    ch = f.read(1)
f.close()

# writelines
f = open("./FStestTwo.txt", "w")
lines = ['me\n', 'myself\n', "i"]
f.writelines(lines)
f.close()

# files are iterable in python > 2.2
for line in open('FStestTwo.txt', "r"):
    print line