# Pets class containing dogs

# Dogs stuff
# Parent class
class Dog:
    # Class attribute
    species = 'mammal'
    is_hungry = True
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    def walk(self):
        return "{} is walking!".format(self.name)
    def eat(self):
        self.is_hungry = False
# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Pets class
class Pets:
    def __init__(self, dogs):
        self.dogs = dogs
    def walk(self):
        for aDog in self.dogs:
            print(aDog.walk())
# Create pets
myDogs = [Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]
myPets = Pets(myDogs)
# Walk the Dogs
myPets.walk()
