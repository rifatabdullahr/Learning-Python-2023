'''
if 5 > 2:
    print("Five is greater than two")
if 5 > 2:
        print("Five is greater than two")
'''

"""
x = 10
y = "I am Rifat"
print(x)
print(y)

"""

#comment { " # " single line comment, '''/""" use for multiline comment }
#print("hello world")

'''

x = 34 #here x is int
x = "Rifat" #here x is str
print(x)

'''

'''
for x = str(3/name)
for x = int(3)
for x = float(3)

'''
"""
x, y, z = "Red", "Green", "Yellow"
print(x,y,x)

"""
#to assign same values to multiple variable
'''
x = y = z = "Rifat"
print(x+y+z)
# print(x,y,z) #in print() function i can output multiple variable,separated by comma
             #i can also use + instade of comma
'''
"""
x = "Rifat"
print(type(x))
print(x)
"""
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
'''
Global Variable
'''
#Create a variable outside of a function, and use it inside the function

'''
x = "awsome"

def myfunc():
   print("Python is " + x)

myfunc()

'''
#Create a variable inside a function, with the same name as the global variable
'''
x = "awsome"

def myfunc():
   x = "fantastic"
   print("Python is " + x)

myfunc()

print("Python is " + x)
'''
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
'''
x = "Fantastic"

def myfunc():
   global x
   x = "Awsome"
myfunc()


print("Python is " + x)
'''
#data type
'''
x = "hello world"
print(type(x))
print(x)
'''
'''
x = ["apple", "banana", "cherry"] #list data type
print(type(x))
print(x)
'''
'''
x = ("apple", "banana", "cherry") #tuple data type
print(type(x))
print(x)
'''
'''
x = range(7)
print(type(x))  #range data type
print(x)
'''
'''
x = { "name" : "Rifat", "age" : 36} #dict data type
print(type(x))
print(x)
'''
'''
x ={"apple", "banana", "cherry"} #set data type
print(type(x))
print(x)
'''
'''
x = frozenset({"apple", "banana", "cherry"}) #frozenset data type
print(type(x))
print(x)
'''
'''
x = True
print(type(x)) #bool data type
print(x)
'''
'''
x = b"Hello"
print(type(x)) #bytes data type
print(x)
'''
'''
x = bytearray(5)
print(type(x)) #bytearray data type
print(x)
'''
'''
x = memoryview(bytes(5)) #memoryview data type
print(x)
print(type(x))
'''
'''
x = None
print(type(x)) #noneType data type
print(x)
'''
#python numbers
'''
x = 1 #int
y = 2.8 #float
z = 1j #complex

print(type(x))
print(type(y))
print(type(z))
'''
#Float can also be scientific numbers with an "e" to indicate the power of 10
'''
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
'''
#Complex numbers are written with a "j" as the imaginary part:
'''
x = 3+5J
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
'''

# You can convert from one type to another with the int(), float(), and complex() methods:
# you can not convert complex number into another number type
'''
x = 5 #int
y = 70.50 #float
z = 49j #complex

#convert int into float
a = float(x)

#convert float into int
b = int(y)

#convert float into complex
c = complex(y)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
'''

#Random Number
#Python does not have a random() function to make a random number
#but Python has a built-in module called random that can be used to make random numbers
'''
import random
print(random.randrange(1, 10))
'''

#Python Casting
#Specify a Variable Type
#There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
'''
Casting in python is therefore done using constructor functions:
int() - constructs an integer number from an integer literal, 
        a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal,
        a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, 
        including strings, integer literals and float literals

'''
'''
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x)
print(y)
print(z)

x = float(1)   # x will be 1
y = float(2.8) # y will be 2
z = float("3") # z will be 3
w = float("39.45") # w will be 39.45

print(x)
print(y)
print(z)
print(w)

x = str("10")   # x will be 1
y = str(2) # y will be 2
z = str(50.6) # z will be 3

print(x)
print(y)
print(z)
'''

#Strings
#Strings in python are surrounded by either single quotation marks, or double quotation marks.
'''
print("Hello World")
print('Hello World')

a = "I am Rifat"
print(a)
'''
#multiline Sting
#You can assign a multiline string to a variable by using three quotes('''/""" both):
'''
a = """Amar sonar Bangla
Ami tomay bhalôbasi
Chirôdin tomar akash,
Tomar batas,
Amar prane bajay bãshi.
sonar Bangla,
ami tomay bhalôbasi! """
print(a)
'''

#Strings are Arrays
#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.
'''
a =  "hello, world!"
print(a[8])
'''
#Looping Through a String
#Since strings are arrays, we can loop through the characters in a string, with a for loop.
'''
for z in "Rifat":
    print(z)
    '''
#String Length
#To get the length of a string, use the len() function.
'''
a = "Hi! I am Rifat Abdullah."
print(len(a))
'''
#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in.
'''
a = "Hi! I am Rifat Abdullah."
print("Rifat" in a)
'''
#use it in an if statement
'''
a = "Hi! I am Rifat Abdullah."
if "Rifat" in a:
   print(a)
'''

#Check if NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
'''
a = "Hi! I am Rifat Abdullah."
print("Prinon" not in a)
'''
#use it in an if statement
'''
a = "Hi! I am Rifat Abdullah."
if "Prinon" not in a:
    print("No, 'Prinon' is not present")

    '''

#String Slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
'''
a = "Abdullah."
print(a[0:8]) #[note:The first character has index o]

'''
#Slice From the Start
#By leaving out the start index, the range will start at the first character:
'''
t = "Rifat Abdullah"
print(t[:5])  #Get the characters from the start to position 5 (not included):
'''
'''
#slice to the end
t = "Rifat Abdullah"
print(t[6:]) #Get the characters from position 6(included) and all the way to the end:
'''
#Negative Indexing
#Use negative indexes to start the slice from the end of the string:
'''
b = "I love Cricket" #From "r" in the "cricket" (position -6), but not included "e" in "cricket" (position -2)            
print(b[-6:-3])
'''
#Upper Case
#The upper() method returns the string in upper case:
'''
x = " i love my country"
print(x.upper())
'''
#Lower Case
#The lower() method returns the string in lower case:
'''
v = "Hi dear! I am Rifat.And you?"
print(v.lower())
print(len(v))
print(type(v))
'''
#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
#The strip() method removes any whitespace from the beginning or the end:
'''
d = " I am Rifat Abdullah "
print(d.strip())
'''
#Replace String
#The replace() method replaces a string with another string:
'''
h = "myself rifat"
print(h.replace("r", "S"))
'''

#split string
#The split() method splits the string into substrings if it finds instances of the separator:
'''
j = "Rahat,Rifat,Maruf,Iraz"
h= j.split(",")
print(h)
'''
#String Concatenation
#To concatenate, or combine, two strings you can use the (+) operator.
'''
a = "       Hi There!"
b =" I am rifat"
c = a + b
print(c.strip())
'''
#to add space between them
'''
a = "i am ri"
b = "fat"
c = a + " " + b
print(c.upper())
print(len(c))
print(type(c))
'''
#String Format
#As we learned in the Python Variables chapter, we cannot combine strings and n umbers like this:
"""
age = "35"
txt = "My name is Rifat, I am " + age 
print(txt)
"""
###ut we can combine strings and numbers by using the format() method!
###The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
'''
age = 50
txt = "My name is Rifat and i am {}"
print(txt.format(age))
'''
##The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
'''
quantity = 12
name = "Mango"
price = 600
order = "I want {} pieces of {} for {} taka." #/order = "I want {0} pieces of {1} for {2} taka."
print(order.format(quantity, name, price)) #You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

'''
#Escape Character
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash (\) followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
#
'''
txt = "We are called \"PABNAIYA\" in our country"
print(txt)

'''

# \'  (Single Quote)
'''
txt = "I\'m Fine"
print(txt)
'''
# \\  (Backslash)
'''
txt = "Will you go to school today \\ Or I will go"
print(txt)
'''
# \n  (New Line)
'''
txt = "Hi there!\nI am Rifat.\nHow are you?"
print(txt)
'''
# \r  (Carriage Return)
'''
txt = "Python is included in CodeSpeedy\r123456"
print(txt)
'''
# \t  (Tab)
'''
txt = "I am Rifat \tAnd he is Asif."
print(txt)
'''
# \b  (Backspace)
'''
txt = "I am Rifat \bAbdullah"
print(txt)
'''
# \f  (Form Feed)
'''
txt = "Hello\fRifat"#strang Problem in output,Vs code
print(txt)
'''
# \ooo (Octal value)
'''
txt = "\122\151\146\141\164"
print(txt)
'''
# \xhh (Hex value)
'''
txt = "\x49\x20\x61\x6d\x20\x52\x69\x66\x61\x74"
print(txt)
''' 
