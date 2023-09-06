                                   ##Python Lists
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, 
#the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:
'''
mn = ["i", "am", "fine"]
print(mn)
'''

##List Items
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc. 

##Ordered
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.

##Changeable
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

##Allow Duplicates
#Since lists are indexed, lists can have items with the same value.
'''
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#
list = ["This", "is", "Rahim.", "Rahim", "is", "a", "good", "boy."]
print(list)
'''

##List Length
#To determine how many items a list has, use the len() function:
'''
thislist = ["apple", "banana", "cherry", "apple", "banana", "cherry", "apple", "banana", "cherry"]
print(len(thislist))
'''

##List Items - Data Types
#List items can be of any data type:
'''
list1 = ["apple", "banana", "cherry"]       #String, int and boolean data types:
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)
#
mylist = [5, "banana", True, 9, "cherry", False, 0, "apple", True] #A list can contain different data types:
print(mylist)
print(len(mylist))
'''

##List type()
#From Python's perspective, lists are defined as objects with the data type 'list':
'''
mylist = [5, "banana", True, 9, "cherry", False, 0, "apple", True]
print(type(mylist))
'''

##The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
'''
the_list = list(("I am Rifat Abdullah"))
print(the_list)
print(type(the_list))
print(len(the_list))
'''
#'''
                  ##Python Collections (Arrays)
#There are four collection data types in the Python programming language:
'''
## List is a collection which is ordered and changeable. Allows duplicate members.
x = ["apple", "banana", "cherry"]

## Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
x = ("apple", "banana", "cherry")

## Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
x ={"apple", "banana", "cherry"}

## Dictionary is a collection which is ordered** and changeable. No duplicate members.
x = { "name" : "Rifat", "age" : 36}
'''

                                    ##Access List Items
##Access Items
'''
#List items are indexed and you can access them by referring to the index number:
rifat = ["apple", "banana", "mango", "cherry", "orange"] #The first item has index 0.
print(rifat[3])
'''

##Negative Indexing
#Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
'''
rifat = ["apple", "banana", "mango", "cherry", "orange"] #The first item has index 0.
print(rifat[-3])
'''

##Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.
'''
rifat = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"] 
print(rifat[1:-1])                #The search will start at index 1 (included) and end at index -1 (not included).

#
rifat = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"] 
print(rifat[0:4])   #Remember that the first item has index 0.
#
thislist = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
print(thislist[2:])
'''

##Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the list:
'''
rifat = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"] 
print(rifat[-5:-1])
'''

##Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:
'''
rifat = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"] 
if "mango" in rifat:
    print("Yes, mango is here!")
else :
    print("No, Item is not present here")
#
rifat = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"] 
if "carrot" in rifat:
    print("Yes, mango is here!")
else :
    print("No, Item is not present here")
'''

                                    ##Change List Items
##Change Item Value
#To change the value of a specific item, refer to the index number:
'''
rifat = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
rifat[3] = "blueberry"
print(rifat)
'''

##Change a Range of Item Values
#To change the value of items within a specific range, define a list with the new values, 
#and refer to the range of index numbers where you want to insert the new values:
'''
rifat = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
rifat[2:6] = "rashberry", "blueberry", "caneberry", "blackberry"
print(rifat)
#
fruit = ["apple", "banana", "cherry"]       #If you insert more items than you replace, the new items will be inserted where you specified, 
fruit[1:2] = ["blackberry", "watermelon"]   #and the remaining items will move accordingly:
print(fruit)
'''
#If you insert more items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly:
'''
fruit = ["apple", "banana", "cherry"]
fruit[1:2] = ["blueberry", "carrot"]
print(fruit) #The length of the list will change when the number of items inserted does not match the number of items replaced.
'''

#If you insert less items than you replace, the new items will be inserted where you specified,
#  and the remaining items will move accordingly:
'''
rifat = ["apple", "banana", "cherry"]
rifat[1:3] = ["mango"]
print(rifat)
'''

                                ##Add List Items

##Append Items
#To add an item to the end of the list, use the append() method:
'''
rifat = ["apple", "banana", "cherry"]
rifat.append("mango")
print(rifat)
'''

##Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#The insert() method inserts an item at the specified index:
'''
rifat = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
rifat.insert(3, "blueberry")  #the list will now contain 4 items
print(len(rifat))
print(type(rifat))
print(rifat)
#
fruit = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
fruit.insert(7, "coconut")
print(len(fruit))
print(type(fruit))
print(fruit)
'''

##Extend List
#To append elements from another list to the current list, use the extend() method.
'''
rifat = ["mango", "orange", "lichi", "watermelon"]
hasib = ["blackberry","strawberry", "caneberry", "coconut"]
rifat.extend(hasib)
print(rifat)    #The elements will be added to the end of the list.
'''

##Add Any Iterable
#The extend() method does not have to append lists, 
# you can add any iterable object (tuples, sets, dictionaries etc.).
'''
rifat = ["mango", "orange", "lichi", "watermelon"]
hasib = {"name", "John", "age", 36}
rifat.extend(hasib)
print(rifat)
#
r = [ "book", "pen", "pencil", "paper"]
s ={"apple", "mango", "banana"}
r.extend(s)
print(r)
'''

    
                                     ##Remove List Items

##Remove Specified Item
#The remove() method removes the specified item.
'''
fruit = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]    #Remove "banana":
fruit.remove("banana")
print(fruit)
'''

##Remove Specified Index
#The pop() method removes the specified index.
'''                                               
rifat = ["apple", "banana", "cherry"]    #Remove the second item:
rifat.pop(1)
print(rifat)
'''
#If you do not specify the index, the pop() method removes the last item.
'''
fruit = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
fruit.pop()
print(fruit)
'''
#The del keyword also removes the specified index:
'''
fol = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
del fol[1]
print(fol)
'''
#The del keyword can also delete the list completely.
'''
fol = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
del fol
print(fol)
'''

##Clear the List
#The clear() method empties the list.
#The list still remains, but it has no content.
'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
'''

                                     ##Loop Lists

##Loop Through a List
#You can loop through the list items by using a for loop:
'''
fruit = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
for x in fruit:            #Print all items in the list, one by one:
   print(x)
   '''

##Loop Through the Index Numbers
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
'''
fruit = ["apple", "banana", "mango", "cherry", "orange", "kiwi", "melon"]
for i in range(len(fruit)):
   print(i, fruit[i])           #The iterable created in the example above is [0, 1, 2].
'''

## While Loop
#Use the len() function to determine the length of the list, 
#then start at 0 and loop your way through the list items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.
'''
thislist = ["apple", "banana", "cherry", "gab"]
i = 0
while i < len(thislist):
  print(i, thislist[i])
  i = i + 1
'''

##Looping Using List Comprehension
#A short hand for loop that will print all items in a list:
'''
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
'''


                                         ##List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
rifat = []

for x in fruits:
    if "a" in x:
        rifat.append(x)
print(rifat)
#With list comprehension you can do all that with only one line of code:
fol = ["apple", "banana", "cherry", "kiwi", "mango"]
notun_fol = [ x for x in fol if "a" in x ]
print(notun_fol) 
'''
#
#The Syntax ........newlist = [expression for item in iterable if condition == True]

##Condition
#The condition is like a filter that only accepts the items that valuate to True.
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]    #Only accept items that are not "apple":
print(newlist)

#The condition if x != "apple"  will return True for all elements other than "apple",
#making the new list contain all fruits except "apple".
#The condition is optional and can be omitted:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
rifat = [x for x in fruits ]
print(rifat)
'''

##Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
#You can use the range() function to create an iterable:
'''
newlist = [x for x in range(10)]
print(newlist)
#
newlist2 = [x for x in range(10) if x <5]
print(newlist2)
'''

##Expression
#The expression is the current item in the iteration, 
#but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
#Set the values in the new list to upper case:
'''
rik = ["apple", "banana", "cherry", "kiwi", "mango"]
nrik = [x.upper() for x in rik ]
print(nrik)
#
vir = ["apple", "banana", "cherry", "kiwi", "mango"]
kim = ["Rifat" for x in vir ]
print(kim)
'''

##The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#Return "orange" instead of "banana":
'''
rik = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in rik]
print(newlist) #"Return the item if it is not banana, if it is banana return orange".
'''

                                            ##Sort Lists

##Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
'''
fruit = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit.sort()
print(fruit)

#Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
'''

##Sort Descending
#To sort descending, use the keyword argument reverse = True:
'''
fruit = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit.sort(reverse = True)
print(fruit)
#
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
'''

##Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.
'''
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
'''

##Case Insensitive Sort
#By default the sort() method is case sensitive,
#resulting in all capital letters being sorted before lower case letters:
'''
fruit = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
fruit.sort()
print(fruit)

#So if you want a case-insensitive sort function, use str.lower as a key function:

fruit = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
fruit.sort(key = str.lower)
print(fruit)
'''

##Reverse Order
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements.
'''
fruit = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
fruit.reverse()
print(fruit)
'''

                                        ##Copy Lists

#Copy a List
#You cannot copy a list simply by typing list2 = list1, because: 
#list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().
'''
fruit = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
myFruit = fruit.copy()
print(myFruit)

#Another way to make a copy is to use the built-in method list().

mokam = ["Kalam", "Motin", "abul", "Kailla", "Bilas"]
rifat = list(mokam)
print(rifat)
'''

                                        ##Join Lists

#Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
'''
fruit = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
taka = [10, 20, 50, 100, 200, 500, 1000]
total = fruit + taka
print(total)
'''
#Another way to join two lists is by appending all the items from list2 into list1, one by one:
'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
#
hasib = ["cse", "swe", "eng", "nfe", "eee"]
rabbi = [1, 2, 3, 4, 5, 6, 7]
for x in rabbi:
    hasib.append(x)
print(hasib)
'''

#you can use the extend() method, where the purpose is to add elements from one list to another list:
'''
hasib = ["cse", "swe", "eng", "nfe", "eee"]
rabbi = [1, 2, 3, 4, 5, 6, 7]
hasib.extend(rabbi)
print(hasib)
'''

                                               ##List Methods
'''                              

Method	             Description
_________________________________________________________________________________________________
1.append()	             Adds an element at the end of the list

2.clear()	             Removes all the elements from the list

3.copy()	             Returns a copy of the list

4.count()	             Returns the number of elements with the specified value

5.extend()	             Add the elements of a list (or any iterable), to the end of the current list

6.index()	             Returns the index of the first element with the specified value

7.insert()	             Adds an element at the specified position

8.pop()	                 Removes the element at the specified position

9.remove()	             Removes the item with the specified value

10.reverse()	         Reverses the order of the list

11.sort()	             Sorts the list
'''

##1.append()	         Adds an element at the end of the list
'''                      #list.append(elmnt)
a = ["apple", "banana", "cherry"]  # An element of any type (string, number, object etc.)
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
'''
##2.clear()	             Removes all the elements from the list
'''                      #list.clear()
a = ["apple", "banana", "cherry"]
a.clear()
print(a)
'''
##3.copy()	             Returns a copy of the list
'''                      #list.copy()
a = ["apple", "banana", "cherry"]
x = a.copy()
print(x)
'''
##4.count()	             Returns the number of elements with the specified value
'''                      #list.count(value)
a = ["apple", "banana", "cherry"]
x =a.count("apple")
print(x)
#
n = ["apple", "banana", "cherry", "apple", "banana", "banana", "cherry"]
m = n.count("banana")
print(m)
'''
##5.extend()	         Add the elements of a list (or any iterable), to the end of the current list
'''                      #list.extend(iterable)
A =["Rahim", "karim", "Badsha"]  #Any iterable (list, set, tuple, etc.)
B = ["Faysal"]
A.extend(B)
print(A)
'''
##6.index()	             Returns the index of the first element with the specified value
'''                      #list.index(elmnt)
z = ["Rahim", "karim", "Badsha", "Faysal"]
x = z.index("Badsha")         #Any type (string, number, list, etc.)
print(x)
'''
##7.insert()	          Adds an element at the specified position
'''                       #list.insert(pos, elmnt)
                          #pos	Required. A number specifying in which position to insert the value
                          #elmnt	Required. An element of any type (string, number, object etc.)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
'''
##8.pop()	               Removes the element at the specified position
'''                        #list.pop(pos)
                           #A number specifying the position of the element you want to remove, default value is -1
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
'''
##9.remove()	           Removes the item with the specified value.
'''                        #list.remove(elmnt)
                           #Any type (string, number, list etc.)
fruits = ['apple', 'banana', 'cherry']
fruits.remove("apple")
print(fruits)
'''
##10.reverse()	           Reverses the order of the list
'''                        #list.reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
'''
##11.sort()	               Sorts the list
'''                        #list.sort(reverse=True|False, key=myFunc)
                           #reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
                           #key	Optional. A function to specify the sorting criteria(s)
fruits = ['apple', 'Banana', 'cherry']
fruits.sort()
print(fruits)
#
cars1 = ['Ford', 'BMW', 'Volvo']
cars1.sort(reverse=True)
print(cars1)
# A function that returns the length of the value:
def myfunc(x):
    return len(x)

gari = ['Ford', 'Mitsubishi', 'BMW', 'VW']
gari.sort( key = myfunc )
print(gari)
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars2 = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars2.sort(reverse=True, key=myFunc)
print(cars2)
'''