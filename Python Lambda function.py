                                                ##Python Lambda

#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
###lambda arguments : expression
#The expression is executed and the result is returned:
'''
#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))
#
#Multiply argument m with argument n and return the result:

b = lambda m, n : m * n
print(b(10, 5))
#
#Summarize argument a, b, and c and return the result:
p = lambda q, r, s : q + r + s
print(p(20,30,50))
'''

##Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, 
#and that argument will be multiplied with an unknown number:
'''
def myfunc(n):
  return lambda a : a * n
  '''
#Use that function definition to make a function that always doubles the number you send in:
'''
def myfunc(n):
    return lambda a : a * n
doubler = myfunc(2)
print(doubler(11))
#
#Or, use the same function definition to make a function that always triples the number you send in:
def func(l):
    return lambda m : m * l
trippler = func(3)
print(trippler(11))
#
#Or, use the same function definition to make both functions, in the same program:
def function(y):
    return lambda x : x * y
double = function(2)
tripple = function(3)
print(double(25))
print(tripple(20))
'''
#Use lambda functions when an anonymous function is required for a short period of time.

