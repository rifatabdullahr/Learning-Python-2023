                                                ##Python Inheritance

#Python Inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.


                                                ##Create a Parent Class

#Any class can be a parent class, so the syntax is the same as creating any other class:
#Create a class named Person, with firstname and lastname properties, and a printname method:
'''
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

##Use the Person class to create an object, and then execute the printname method:
x = Person("Rifat", "Abdullah")

x.printname()
'''

                                                    ##Create a Child Class

#To create a class that inherits the functionality from another class, 
# send the parent class as a parameter when creating the child class:
#Create a class named Student, which will inherit the properties and methods from the Person class:
'''
class Student(Person):
  pass
  
#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
'''
#Example
#Use the Student class to create an object, and then execute the printname method:
'''
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    pass

x = Student("Rifat", "Abdullah")
x.printname()

'''


                                            ##Add the __init__() Function

#So far we have created a child class that inherits the properties and methods from its parent.
#We want to add the __init__() function to the child class (instead of the pass keyword).

#Note: The __init__() function is called automatically every time the class is being used to create a new object.
#Example
#Add the __init__() function to the Student class:
'''
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    '''
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
'''
class People:
    def __init__(self, fname, age):
        self.fname = fname
        self.age = age
    def printinfo(self):
        print("Hi!I am " + self.fname +" and i am " + str(self.age) + " years old.")
class Student(People):
    def __init__(self, fname, age):
        People.__init__(self, fname, age)
x = Student("Rifat", 25)

x.printinfo()

#Now we have successfully added the __init__() function, 
#and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

'''


                                                    ##Use the super() Function

#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Rifat", "Abdullah")

x.printname()

#By using the super() function, you do not have to use the name of the parent element, 
#it will automatically inherit the methods and properties from its parent.

'''


                                                ##Add Properties
#Example
#Add a property called graduationyear to the Student class:
'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

'''
##In the example below, the year 2019 should be a variable, 
#and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

#Add a date parameter, and pass the correct year when creating objects:
'''
class Info:
    def __init__(self, name, place):
        self.name = name
        self.place = place
    
class Student(Info):
    
    def __init__(self, name, place, date):
        super().__init__(name, place)
        self.date = date
    
    def SWE_student(self):
        print("I am " + self.name + ".I am from " + self.place + ".My birth year is " + str(self.date) + ".Thank you.")
    
x = Student("Rifat Abdullah", "Sirajgonj", 1998)
x.SWE_student()

'''


                                                ##Add Methods
#Example
#Add a method called welcome to the Car class:
'''
class Car:
    def __init__(self, object, name):
        self.object = object
        self.name = name
    
    def printmyobject(self):
        print(self.object, self.name)

class Vehicle(Car):
    def __init__(self, object, name, year):
        super().__init__(object, name)
        self.year = year

    def welcome(self):
        print("This is my ", self.object, ".It is a ", self.name, ".I bought this at ", str(self.year), ".")

x = Vehicle("Car", "BMW", 2022)
x.welcome()

'''