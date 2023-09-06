                                            ##Python Functions

#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.


                                           ##Creating a Function

#In Python a function is defined using the def keyword:
'''
def my_function():
    print("hello from a function")
'''


                                            ##Calling a Function

#To call a function, use the function name followed by parenthesis:
'''
def my_function():
    print("Hello from a function")
my_function()
'''


                                            ##Arguments

#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. 
#You can add as many arguments as you want, just separate them with a comma.
#The following example has a function with one argument (fname). 
#When the function is called, we pass along a first name, which is used inside the function to print the full name:
'''
def my_function(fname):
    print(fname + "Abdullah")
my_function("Rifat ")
my_function("Maymuna ")
my_function("Khaled ")
#Arguments are often shortened to args in Python documentations.
'''


                                            ##Parameters or Arguments?

#The terms parameter and argument can be used for the same thing: information that are passed into a function.
                                          #From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.



                                            ##Number of Arguments

#By default, a function must be called with the correct number of arguments. 
#Meaning that if your function expects 2 arguments, 
#you have to call the function with 2 arguments, not more, and not less.
#This function expects 2 arguments, and gets 2 arguments:
'''
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Rifat", "Abdullah")
'''

##If you try to call the function with 1 or 3 arguments, you will get an error:
#This function expects 2 arguments, but gets only 1:
'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil") #this will be an error

'''


                                            ##Arbitrary Arguments, *args

#If you do not know how many arguments that will be passed into your function, 
#add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:
#If the number of arguments is unknown, add a * before the parameter name:
'''
def my_function(*friend):
    print("This is my friend " + friend[1])
my_function("Rifat", "Sakib", "Salam")

#Arbitrary Arguments are often shortened to *args in Python documentations.
'''


                                            ##Keyword Arguments

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
'''
def my_function(child1, child2, child3):
    print(child2 + " is our elder son")
my_function(child1 = "salam", child2 = "Rifat", child3 = "Sakib")

#The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
'''


                                            ##Arbitrary Keyword Arguments, **kwargs

#If you do not know how many keyword arguments that will be passed into your function, 
#add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
'''
def my_func(**kid):
    print("My last name is " + kid["lname"])
my_func(fname = "Rifat", lname = "Abdullah")

#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
'''


                                                ##Default Parameter Value
#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
'''
def my_function(country = "Nepal"):
    print("I am from " + country)
my_function("Bangladesh")
my_function("India")
my_function()
my_function("Bhutan")
'''


                                                ##Passing a List as an Argument
#You can send any data types of argument to a function (string, number, list, dictionary etc.), 
#and it will be treated as the same data type inside the function.
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:
'''
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "Banana", "Mango"]

my_function(fruits)
'''


                                                ##Return Values
#To let a function return a value, use the return statement:
'''
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
'''


##The pass Statement
#function definitions cannot be empty, but if you for some reason have a function definition with no content, 
# put in the pass statement to avoid getting an error.
'''
def myfunction():
  pass
  '''


##Recursion
#Python also accepts function recursion, which means a defined function can call itself.
#Recursion is a common mathematical and programming concept. It means that a function calls itself. 
#This has the benefit of meaning that you can loop through data to reach a result.
#The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, 
#or one that uses excess amounts of memory or processor power. 
#However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
#In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). 
#We use the k variable as the data, which decrements (-1) every time we recurse. 
#The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
#To a new developer it can take some time to work out how exactly this works, 
#best way to find out is by testing and modifying it.

'''
def tri_recursion(k):
    if (k > 0):
     result = k + tri_recursion(k-1)
     print(result)
    else:
     result = 0
    return result
    
print("\n\nRecursion example result")
tri_recursion(6)
'''