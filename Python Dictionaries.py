                                                ##Python Dictionaries
##Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
'''

##Dictionary Items
#Dictionary items are ordered, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
'''
#Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
'''

##Ordered or Unordered?
#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

##Changeable
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

##Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
'''

##Dictionary Length
#To determine how many items a dictionary has, use the len() function:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
'''

##Dictionary Items - Data Types
#The values in dictionary items can be of any data type:
#String, int, boolean, and list data types:
'''
car = {
 "brand": "Ford",
 "model": "mustang",
 "electric": "False",
 "year": "1964",
 "color": ["red", "green", "blue", "yellow"]
}
print(car)
'''

##type()
#From Python's perspective, dictionaries are defined as objects with the data type 'dict':
#Print the data type of a dictionary:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
'''

##The dict() Constructor
#It is also possible to use the dict() constructor to make a dictionary.
'''
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
'''
'''
###Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List           is a collection which is ordered and changeable. Allows duplicate members.
#Tuple          is a collection which is ordered and unchangeable. Allows duplicate members.
#Set            is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary     is a collection which is ordered** and changeable. No duplicate members.
'''


                                            ##Access Dictionary Items

##Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:
'''
mydict = {
    "name" : "ford",         #Get the value of the "model" key:
    "model" : "mustang",
    "year" : 1964,
    "color" : "red"
}
x = mydict["model"]
print(x)
#There is also a method called get() that will give you the same result:
mydict1 = {
    "name" : "ford",       
    "model" : "mustang",
    "year" : 1964,
    "color" : "red"
}
x1 = mydict1.get("model")
print(x1)
'''

##Get Keys
#The keys() method will return a list of all the keys in the dictionary.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
'''
#Add a new item to the original dictionary, and see that the keys list gets updated as well:
'''
car = {
    "brand": "Ford",
    "model": "Mustang",
     "year": 1964
}
x = car.keys()
print(x)
car["color"] = "white"
print(x)
'''

##Get Values
#The values() method will return a list of all the values in the dictionary.
'''
car = {
    "brand": "Ford",
    "model": "Mustang",
     "year": 1964
}
x = car.values()
print(x)
car["color"] = "white"
print(x)
'''

##Get Items
#The items() method will return each item in a dictionary, as tuples in a list.
'''
car = {
    "brand": "Ford",
    "model": "Mustang",
     "year": 1964
}
x = car.items()
print(x)
car["year"] = "2023"
print(x)
'''

##Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:
'''
car = {
    "brand": "Ford",
    "model": "Mustang",
     "year": 1964
}
if "model" in car :   
    print("yes, model is present in car")
'''


                                         ##Change Dictionary Items

##Change Values
#You can change the value of a specific item by referring to its key name:
'''
#Change the "year" to 2023:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2023
print(thisdict)
'''

##Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
'''
#Update the "year" of the car by using the update() method:
thisdict = {
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2023})
print(thisdict)
'''


                                                ##Add Dictionary Items

##Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
'''

##Update Dictionary
#The update() method will update the dictionary with the items from a given argument. 
#If the item does not exist, the item will be added.
#The argument must be a dictionary, or an iterable object with key:value pairs.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
'''

                                        ##Remove Dictionary Items

##Removing Items
#There are several methods to remove items from a dictionary:
#The pop() method removes the item with the specified key name:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#
#####The popitem() method removes the last inserted item:
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.popitem()
print(thisdict1)
#
#####The del keyword removes the item with the specified key name:
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict2["brand"]
print(thisdict2)
#
#####The clear() method empties the dictionary:
thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict3.clear()
print(thisdict3)
#
#####The del keyword can also delete the dictionary completely:
thisdict4 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict4
print(thisdict4) #this will cause an error because "thisdict" no longer exists.
'''


                                                ##Loop Dictionaries

##Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, 
#but there are methods to return the values as well.
'''
#Print all key names in the dictionary, one by one:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)
    '''
###
#Print all values in the dictionary, one by one:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
   print(thisdict[x])
#
##You can also use the values() method to return values of a dictionary:

thisdict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict1.values():
    print(x)
'''

##You can use the keys() method to return the keys of a dictionary:
'''
thisdict2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict2.keys():
    print(x)
    '''

##Loop through both keys and values, by using the items() method:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x,y in thisdict.items():
    print(x,y)
    '''


                                             ##Copy Dictionaries

##Copy a Dictionary
#You cannot copy a dictionary simply by typing dict2 = dict1, 
# because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
'''
rifat = {
    "iqbal" :"mango",
    "rasel" : "banana",
    "torikul" : "apple",
    "masud" : "coconut",
    "anik" : "lemon"
}
rahim = rifat.copy()
print(rahim)

#
##Make a copy of a dictionary with the dict() function:
rifas = {
    "iqbal" :"mango",
    "rasel" : "banana",
    "torikul" : "apple",
    "masud" : "coconut",
    "anik" : "lemon"
}
rakib = dict(rifas)
print(rakib)
'''


                                            ##Nested Dictionaries

##Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.
'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  },
  "child4" : {
    "name" : "ashraf",
    "year" : 2018
  }
}
print(myfamily)
'''

##Or, if you want to add three dictionaries into a new dictionary:
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
'''
rifat = {
    "iqbal" :"mango",
    "rasel" : "banana",
    "torikul" : "apple",
    "masud" : "coconut",
    "anik" : "lemon"
}
rakib = {
    "iqbal" :"1990",
    "rasel" : "1998",
    "torikul" : "1995",
    "masud" : "1997",
    "anik" : "2000"
}
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
all = {
    "rifat" : rifat,
    "rakib" : rakib,
    "car" : car
}
print(all)
'''

##Access Items in Nested Dictionaries
#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
#Print the name/year of child 2:
'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  },
  "child4" : {
    "name" : "ashraf",
    "year" : 2018
  }
}
print(myfamily["child2"]["name"])#["year"])
'''


                                            ##Dictionary Methods

#Python has a set of built-in methods that you can use on dictionaries.


##clear()	        Removes all the elements from the dictionary
                  #dictionary.clear()
'''
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2022
}
car.clear()
print(car)
'''

##copy()	        Returns a copy of the dictionary
                  #The copy() method returns a copy of the specified dictionary.
                  #dictionary.copy()
'''
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2022
}
x = car.copy()
print(x)
'''

##fromkeys()	    Returns a dictionary with the specified keys and value
                  #The fromkeys() method returns a dictionary with the specified keys and the specified value.
                  #dict.fromkeys(keys, value)
                  #keys	Required. An iterable specifying the keys of the new dictionary
                  #value	Optional. The value for all keys. Default value is None
'''
x = ("key1", "key2", "key3")
y = ("lock")
keylock = dict.fromkeys(x,y)
print(keylock)
'''

##get()	          Returns the value of the specified key
                  #The get() method returns the value of the item with the specified key.
                  #dictionary.get(keyname, value)
                  #keyname	Required. The keyname of the item you want to return the value from
                  #value	Optional. A value to return if the specified key does not exist.default value None
'''
car ={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2020
}
x = car.get("model")
print(x)
'''

##items()	        Returns a list containing a tuple for each key value pair
                  #The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
                  #The view object will reflect any changes done to the dictionary, see example below.
                  #dictionary.items()
'''
car ={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2020
}
x = car.items()
print(x)
'''

##keys()	          Returns a list containing the dictionary's keys
                    #The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
                    #The view object will reflect any changes done to the dictionary, see example below.
                    #dictionary.keys()
'''
car ={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2020
}
x = car.keys()
print(x)
'''

##pop()	            Removes the element with the specified key
                    #The pop() method removes the specified item from the dictionary.
                    #The value of the removed item is the return value of the pop() method,
                    #dictionary.pop(keyname, defaultvalue)
                    #keyname	Required. The keyname of the item you want to remove.
                    #defaultvalue	Optional. A value to return if the specified key do not exist.
'''
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2022
}
car.pop("model")
print(car)
'''

##popitem()	        Removes the last inserted key-value pair
                    #The popitem() method removes the item that was last inserted into the dictionary.
                    #dictionary.popitem()
'''
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2022
}
car.popitem()
print(car)
'''

##setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key,with the specified value
                    #The setdefault() method returns the value of the item with the specified key.
                    #dictionary.setdefault(keyname, value)
                    #keyname	Required. The keyname of the item you want to return the value from
'''
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2022
}
x = car.setdefault()
print(x)
'''

##update()	        Updates the dictionary with the specified key-value pairs
                    #The update() method inserts the specified items to the dictionary.
                    #The specified items can be a dictionary, or an iterable object with key value pairs.
                    #dictionary.update(iterable)
                    #iterable	A dictionary or an iterable object with key value pairs, that will be inserted to the dictionary
'''
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2022
}
car.update({"color" : "white"})
print(car)
'''

##values()	        Returns a list of all the values in the dictionary
                    #The values() method returns a view object. The view object contains the values of the dictionary, as a list.
                    #dictionary.values()
#'''
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2022
}
x = car.values()
print(x)
