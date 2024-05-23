class Bird:
    name= ""
    age = 0

bird = Bird ()
bird.name = "abc"
bird.age =20
print (bird.name, " ", bird.age)

bird2 = Bird ()
print ("Bird2", bird2.name, " ", bird2.age)

class Room():
    length = 0.0
    breadth = 0.0

    def area (self):
        return self.length
        return self.breadth

room1 = Room()
room1.length = 10
room1.breadth = 20

print (room1.area())

class Bike () :
    def __init__(self, abc= " ", xyz= " "):
        self.name = abc
        self.country = xyz

bike1 = Bike ("mountain bike", "india")
print(bike1.name , bike1.country)

class Animal():
    def eat (self):
        print ("I can eat")

class Dog (Animal):
    def bark (self):
        print ("I car Bark")

class Breed(Dog):
    def name(self):
        print("German Shephard")
breed = Breed ()
breed.eat ()
breed.bark()
breed.name()

class Animal ():
    def eat (self):
        print ("I am eating")

class Dog (Animal):
    def bark (self):
        print ("I am barking")

class Cat (Animal):
    def meow (self):
        print ("Meow")

#Polymorphinm

cat = Cat ()
dog = Dog ()

dog.bark()
cat.meow ()

















