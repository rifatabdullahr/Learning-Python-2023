                                            ##Python Scope

#A variable is only available from inside the region it is created. This is called scope.


                                            ##Local Scope

#A variable created inside a function belongs to the local scope of that function, 
#and can only be used inside that function.
#A variable created inside a function is available inside that function:
'''
def myfunction():
    x = 30
    print(x)

myfunction()
'''

##Function Inside Function
#As explained in the example above, the variable x is not available outside the function,
#but it is available for any function inside the function:
'''
def myfunction():
    x = 300

    def mynewfunction():
        print(x)

    mynewfunction()

myfunction()

'''


                                                ##Global Scope

#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.

#A variable created outside of a function is global and can be used by anyone:
'''
x = "My name is Rifat"

def myfunction():
    print(x)

myfunction()

print(x)

'''


##Naming Variables
#If you operate with the same variable name inside and outside of a function, 
#Python will treat them as two separate variables, 
#one available in the global scope (outside the function) and one available in the local scope (inside the function):
'''
x = "Abdullah"

def myname():
    y = "Rifat"
    print(y)
myname()

print(x)
'''


                                                ##Global Keyword

#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#The global keyword makes the variable global.
#If you use the global keyword, the variable belongs to the global scope:
'''
def myfunc():
    global x
    x = 123

myfunc()

print(x)
'''

#Also, use the global keyword if you want to make a change to a global variable inside a function.
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
'''
x = "Rifat"

def myfunc():
    global x
    x = "Prinon"

myfunc()

print(x)
'''