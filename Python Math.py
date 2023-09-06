                                                    ##Python Math

#Python has a set of built-in math functions, including an extensive math module, 
#that allows you to perform mathematical tasks on numbers.

##Built-in Math Functions
#The min() and max() functions can be used to find the lowest or highest value in an iterable:
'''
y = (10, 14, 20)
x = (20,50,2000)

print(min(x))
print(max(y))
'''
##The abs() function returns the absolute (positive) value of the specified number:
'''
x = abs(-7.25)
print(x)
'''
##The pow(x, y) function returns the value of x to the power of y (xy).
'''
x = pow(3,3)
print(x)
'''

                                                    ##The Math Module

#Python has also a built-in module called math, which extends the list of mathematical functions.
#To use it, you must import the math module:
#When you have imported the math module, you can start using methods and constants of the module.
#The math.sqrt() method for example, returns the square root of a number:
'''
import math

x = math.sqrt(36)
print(x)
'''


## The math.ceil() method rounds a number upwards to its nearest integer,
## the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
'''
import math

x = math.ceil(20.45)
y = math.floor(25.60)

print(x) # returns 21
print(y) # returns 25
'''

#The math.pi constant, returns the value of PI (3.14...):
'''
import math

x = math.pi
print(x)
'''