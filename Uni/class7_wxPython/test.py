class Dog():
    bark = 55

oneDog = Dog()
print oneDog.bark

Dog.bark = 40
print oneDog.bark

oneDog.bark = 55
print oneDog.bark

print Dog.bark

anotherDog = Dog()
print anotherDog.bark

print oneDog.bark

Dog.bark = 30

print oneDog.bark
print anotherDog.bark

Dog.shit = 100
print oneDog.shit
oneDog.shit  = 55
print oneDog.shit

Dog.shit = 90
print oneDog.shit

anotherDog.shit = 55
print anotherDog.shit

Dog.shit = 85
print anotherDog.shit