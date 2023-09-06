                                        ##Python Polymorphism

#The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators
#with the same name that can be executed on many objects or classes.

                                       ##Function Polymorphism

#An example of a Python function that can be used on different objects is the len() function.
'''
##String
#For strings len() returns the number of characters:
x = "Rifat"
print(len(x))
#
##Tuple
#For tuples len() returns the number of items in the tuple:
g = ("apple", "banana", "cherry", "dragon")
print(len(g))
#
##Dictionary
#For dictionaries len() returns the number of key/value pairs in the dictionary:
m = {
    "fname" : "Rifat",
    "lname" : "Abdullah",
    "age" : 25
}
print(len(m))

'''


                                                    ##Class Polymorphism

#Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
#For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
'''
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def move(self):
        print("Drive")

class Boat:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def move(self):
        print("Sail")

class Plane:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def move(self):
        print("Fly")
    
car = Car("BMW", "7 series")
boat =Boat("Titanic", "Black")
plane = Plane("Boeing", 747)

for x in (car, boat, plane):
    #print(x.name)
    #print(x.model)
    x.move()
'''


                                                    ##Inheritance Class Polymorphism

#What about classes with child classes with the same name? Can we use polymorphism there?
#Yes.If we use the example above and make a parent class called Vehicle, and make Car, Boat, 
#Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

##Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
'''
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def Move(self):
    print("Move")

class Car(Vehicle):
  pass

class Ship(Vehicle):
  def Move(self):
    print("Sail")

class Plane(Vehicle):
  def Move(self):
    print("Fly")

car = Car("Ford", "Mustang")
ship = Ship("Titanic", "RMS")
plane = Plane("Boeing", 787)

for x in (car, ship, plane):
 print(x.brand)
 print(x.model)
 x.Move()
 '''
 
#Child classes inherits the properties and methods from the parent class.
#In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.
#The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.
#Because of polymorphism we can execute the same method for all classes.