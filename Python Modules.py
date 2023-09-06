                                                ##Python Modules

##What is a Module?
#Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application.


                                                ##Create a Module

#To create a module just save the code you want in a file with the file extension .py:
'''
def greeting(name):
  print("Hello, " + name)
  '''

#Use a Module
#Now we can use the module we just created, by using the import statement:
#Import the module named Rough_Module, and call the greeting function:
#Note: When using a function from a module, use the syntax: module_name.function_name.

'''
import Rough_Module

Rough_Module.greeting("Rifat")

'''


                                                        ##Variables in Module

#The module can contain functions, as already described, 
#but also variables of all types (arrays, dictionaries, objects etc):

#import the module named Rough_Module, and access the person1 dictionary:
'''
import Rough_Module

a = Rough_Module.person1["age"]

print(a)
'''

                                                        ##Naming a Module

#You can name the module file whatever you like, but it must have the file extension .py


                                                        ##Re-naming a Module

#You can create an alias when you import a module, by using the as keyword:
'''
import Rough_Module as RM

s = RM.person1["age"]

print(s)
'''


                                                        ##Built-in Modules

#There are several built-in modules in Python, which you can import whenever you like.
#Import and use the platform module:
'''
import platform

x = platform.system()
print(x)
'''


                                                        ##Using the dir() Function

#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
#List all the defined names belonging to the platform module:
#Note: The dir() function can be used on all modules, also the ones you create yourself.

'''
import platform

x = dir(platform)
print(x)
'''

                                                        ##Import From Module

#You can choose to import only parts from a module, by using the from keyword.
#The module named Rough_Module has one function and one dictionary:
#Import only the person1 dictionary from the module:
'''
from Rough_Module import Human

x = Human["Address"]
print(x)
'''
#Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: Human["Address"], not Rough_Module.Human["Address"]
