##python Booleans
#
#Booleans represent one of two values: True or False.
#In programming you often need to know if an expression is True or False.
#You can evaluate any expression in Python, and get one of two answers, True or False.
#When you compare two values, the expression is evaluated and Python returns the Boolean answer:
'''
print(10 > 9)
print(10 == 9)
print(10 < 9)
'''
'''     #When you run a condition in an if statement, Python returns True or False:
         #Print a message based on whether the condition is True or False:

a = 2000
b = 300

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
'''
'''      #The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))
#         #Evaluate two variables:
x = "jack"
y = 123

print(bool(x))
print(bool(y))
'''
'''
                      ##Almost any value is evaluated to True if it has some sort of content.
                      #Any string is True, except empty strings.
                      #Any number is True, except 0.
                      #Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("abc"))
print(bool("123"))
print(bool(["mango", "apple", "banana"]))
print(bool([]))
#
                    #In fact, there are not many values that evaluate to False.
                    #except empty values, such as (), [], {}, "", the number 0, and the value None.              
                    # And of course the value False evaluates to False.

print(bool(False))

print(bool(None))

print(bool(0))

print(bool(""))

print(bool(()))

print(bool([]))

print(bool({}))

'''
#
'''                #One more value, or object in this case, evaluates to False, 
                    # and that is if you have an object that is made from a class with a __len__ function that returns 0 or False.
class myclass():
  def __len__(self):
    return 0
  
myobj = myclass()
print(bool(myobj))
'''
#Functions can Return a Boolean
'''
def myfunction():
    return True
print(bool(myfunction))
#
def myfunction():
    return 99
print(bool(myfunction))
'''
#Print "YES!" if the function returns True, otherwise print "NO
'''
def myfunc():
    return True
if myfunc():
   print("Yes!")
else: 
   print("No!")
'''
#the isinstance() function, which can be used to determine if an object is of a certain data type:
'''
x = 5000
print(isinstance(x, int))
x = 5000
print(isinstance(x, float))
x = 5000
print(isinstance(x, str))
'''