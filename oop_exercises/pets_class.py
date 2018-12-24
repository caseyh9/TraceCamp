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

# Create and describe pets
myDogs = [Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]
myPets = Pets(myDogs)
print("I have {} dogs.".format(len(myDogs)))
for aDog in myPets.dogs:
    print("{} is {}.".format(aDog.name, aDog.age))
    aDog.eat()
print("And they're all {}s, of course.".format(aDog.species))
hunger = False
for dog in myPets.dogs:
    if dog.is_hungry == True:
        hunger = True
if hunger:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")
