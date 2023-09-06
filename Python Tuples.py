##Tuple
#Tuples are used to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, 
#the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
'''
fruit = ("apple", "banana", "cherry")t change, add or remove items after the tuple has been created.
'''
##Allow Duplicates
##Since tuples are indexed, they can have items with the same value:
'''
tuple = ("apple", "banana", "cherry", "dragon", "elderberry", "apple", "cherry")
print(tuple)
'''

##Tuple Length
#To determine how many items a tuple has, use the len() function:
'''
rifat = ("apple", "banana", "cherry", "dragon", "elderberry", "apple", "cherry")
print(len(rifat))
'''

##Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item, 
#otherwise Python will not recognize it as a tuple.
'''
tpl = ("apple",)
print(type(tpl))

#NOT a tuple
ntpl = ("apple")
print(type(ntpl))
'''
##Tuple Items - Data Types
#Tuple items can be of any data type:
'''
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
'''
#A tuple can contain different data types:
'''
rifat =  ( "ami", 1, 2, True, False, "lam")
print(rifat)
'''
##type()
#From Python's perspective, tuples are defined as objects with the data type 'tuple':
# <class 'tuple'>
'''
rifat =  ( "ami", 1, 2, True, False, "lam")
print(type(rifat))
'''
##The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
#Using the tuple() method to make a tuple:
'''
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#
rifat = tuple  ( ("apple", "banana", "cherry", "dragon", "elderberry", "apple", "cherry"))
print(rifat)
'''
####
'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

                                ##Access Tuple Items

##Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
'''
thistuple = ("apple", "banana", "cherry")  #Print the second item in the tuple:
print(thistuple[1])
#
rifat = ("apple", "banana", "cherry", "dragon", "elderberry", "apple", "cherry")
print(rifat[4])
'''

##Negative Indexing
#Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.
'''
rifat = ("apple", "banana", "cherry", "dragon", "elderberry", "apple", "cherry")
print(rifat[-3])
'''

##Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new tuple with the specified items.
'''
rifat = ("apple", "banana", "cherry", "dragon", "elderberry", "apple", "cherry")
print(rifat[2:5]) #The search will start at index 2 (included) and end at index 5 (not included).

#This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#This example returns the items from "cherry" and to the end:

thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple2[2:])
'''

##Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the tuple:
'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-3:-1])   #This example returns the items from index -3 (included) to index -1 (excluded)
'''

##Check if Item Exists
#To determine if a specified item is present in a tuple use the in keyword
'''
Hasib = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "cherry" in Hasib:
     print("Yes,'cherry' is present")
     '''
                                ##Unpack Tuples
##Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

##But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
'''
fruit = ("apple", "banana", "cherry", "dragon", "elderberry")
(apple, banana, cherry, dragon, elderberry) = fruit
print(apple)
print(banana)
print(cherry)
print(dragon)
print(elderberry)  #The number of variables must match the number of values in the tuple, 
                   #if not, you must use an asterisk to collect the remaining values as a list.
'''

##Using Asterisk*
#If the number of variables is less than the number of values,
#you can add an * to the variable name and the values will be assigned to the variable as a list:
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
'''


                                 ##Update Tuples
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#But there are some workarounds.

##Change Tuple Values'
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, 
#and convert the list back into a tuple.
'''
Hasib = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
x = list(Hasib)
x[2] = "berry"
Hasib = tuple(x)
print(Hasib)
'''

#Add Items
#Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
#1. Convert into a list: Just like the workaround for changing a tuple,
#  you can convert it into a list, add your item(s), and convert it back into a tuple.
'''
Hasib = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y = list(Hasib)
y.append("strawberry")
Hasib = tuple(y)
print(Hasib)
#
#2. Add tuple to a tuple. You are allowed to add tuples to tuples,
#so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
Rifat = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
x = ("Kola",)
Rifat += x   #When creating a tuple with only one item, 
print(Rifat) #remember to include a comma after the item, otherwise it will not be identified as a tuple.
'''

##Remove Items
#You cannot remove items in a tuple.
#Tuples are unchangeable, 
#so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
print(thistuple)
#Or you can delete the tuple completely:
thistuple1 = ("apple", "banana", "cherry")
del thistuple1   #del keyword can delete the tuple completely
print(thistuple1) #this will raise an error because the tuple no longer exists.
'''
                                 ##Unpack Tuples
##Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

##But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
'''
fruit = ("apple", "banana", "cherry", "dragon", "elderberry")
(apple, banana, cherry, dragon, elderberry) = fruit
print(apple)
print(banana)
print(cherry)
print(dragon)
print(elderberry)  #The number of variables must match the number of values in the tuple, 
                   #if not, you must use an asterisk to collect the remaining values as a list.
'''

##Using Asterisk*
#If the number of variables is less than the number of values,
#you can add an * to the variable name and the values will be assigned to the variable as a list:
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#
#If the asterisk is added to another variable name than the last, 
#Python will assign values to the variable until the number of values left matches the number of variables left.
fruit10 = ("apple", "banana", "cherry", "dragon", "elderberry")
(green1, *tropic, red1) = fruit10
print(green1)
print(tropic)
print(red1)

'''


                                    ##Loop Tuples

#Loop Through a Tuple
#You can loop through the tuple items by using a for loop.
'''
fruit = ("apple", "banana", "cherry", "dragon", "elderberry")
for x in fruit:
    print(x)
'''

##Loop Through the Index Numbers
#You can also loop through the tuple items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
'''
#Print all items by referring to their index number:
fruit = ("apple", "banana", "cherry", "dragon", "elderberry")
for i in range(len(fruit)):
    print(i, fruit[i])
'''

##Using a While Loop
#You can loop through the tuple items by using a while loop.
#Use the len() function to determine the length of the tuple, 
#then start at 0 and loop your way through the tuple items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.
'''
fruit = ("apple", "banana", "cherry", "dragon", "elderberry")
i = 0
while i < len(fruit):
      print(fruit[i])
      i = i + 1 
'''

                                    ##Join Tuples

##Join Two Tuples
#To join two or more tuples you can use the + operator:
'''
fruit = ("apple", "banana", "cherry", "dragon", "elderberry")
num = (1, 3, 5, 7, 9)
sum = fruit + num
print(sum)
'''

##Multiply Tuples
#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
'''
fruit = ("apple", "banana", "cherry", "dragon", "elderberry")
multiply = fruit * 10
print(multiply)
'''

                                        ##Tuple method

##Tuple Methods
#Python has two built-in methods that you can use on tuples.
'''
 Method	                            Description
 count()	     Returns the number of times a specified value occurs in a tuple
 index()	     Searches the tuple for a specified value and returns the position of where it was found
 '''
##Python Tuple count() Method
####The count() method returns the number of times a specified value appears in the tuple.
'''
fruit = ("apple", "banana", "cherry", "dragon", "elderberry", "apple", "banana", "cherry", "dragon", "elderberry", "apple", "banana", "cherry", "dragon", "elderberry")
r = fruit.count("banana")  #tuple.count(value)
print(r)                   #value	Required. The item to search for.
#
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
'''

##Python Tuple index() Method
#The index() method finds the first occurrence of the specified value.
#The index() method raises an exception if the value is not found.
'''
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)   #tuple.index(value)
print(x)                 #value	Required. The item to search for
#
fruit = ("apple", "banana", "cherry", "dragon", "elderberry", "apple", "banana", "cherry", "dragon", "elderberry", "apple", "banana", "cherry", "dragon", "elderberry")
r = fruit.index("banana")  
print(r)
'''
