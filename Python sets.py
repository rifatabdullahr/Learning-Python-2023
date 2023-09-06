                                           ##Python Sets

##set
#Sets are used to store multiple items in a single variable.
#sets are unordered,unchangeable* and unindexed.
#
#
#Note: Set items are unchangeable, but you can remove items and add new items.
#Sets are written with curly brackets.
#Note: Sets are unordered, so you cannot be sure in which order the items will appear.
'''
myset = {"apple", "banana", "cherry"}
print(myset)
'''

##Set Items
#Set items are unordered, unchangeable, and do not allow duplicate values.

##Unordered
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

##Unchangeable
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can remove items and add new items.

##Duplicates Not Allowed
#Sets cannot have two items with the same value.
'''
myset = {"apple", "banana", "cherry", "apple", "cherry"}
print(myset)  #Duplicate values will be ignored:

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #True and 1 is considered the same value:
'''

##Get the Length of a Set
#To determine how many items a set has, use the len() function.
'''
myset = {"apple", "banana", "cherry"}
print(len(myset))
#
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(len(thisset))
'''

##Set Items - Data Types
#Set items can be of any data type:
'''
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

#

set1 = {"abc", 34, True, 40, "male"}
print(set1)
'''

##type()
#From Python's perspective, sets are defined as objects with the data type 'set':
'''
myset = {"apple", "banana", "cherry"}
print(type(myset))
#
set1 = {"abc", 34, True, 40, "male"}
print(type(set1))
'''

##The set() Constructor
#It is also possible to use the set() constructor to make a set.
'''
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
'''

##Python Collections (Arrays)
'''
There are four collection data types in the Python programming language:

List ----is a collection which is ordered and changeable. Allows duplicate members.
Tuple ----is a collection which is ordered and unchangeable. Allows duplicate members.
Set ----is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary ----is a collection which is ordered** and changeable. No duplicate members.

#Set items are unchangeable, but you can remove items and add new items.
'''


                                            ##Access Set ite

##Access Items
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, 
#or ask if a specified value is present in a set, by using the in keyword.
'''
#Loop through the set, and print the values:
myset = ("book", "pen", "pencil", "sharpner")
for x in myset:
    print(x)

#Check if "banana" is present in the set:

myset12 = ("book", "pen", "pencil", "sharpner")
print("pen" in myset12)
'''

##Change Items
#Once a set is created, you cannot change its items, but you can add new items.


                                        ##Python - Add Set Items

##add items 
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.
'''
thisset = {"apple", "banana", "cherry"}
thisset.add("book")
print(thisset)
'''

##Add Sets
#To add items from another set into the current set, use the update() method.
'''
rifat = {"bus", "truck", "cng", "rickshaw", "pickup", "tanker"}
fruit = {"apple", "banana", "cherry", "dragon", "elderbery"}
rifat.update(fruit)
print(rifat)
'''

##Add Any Iterable
#The object in the update() method does not have to be a set, 
#it can be any iterable object (tuples, lists, dictionaries etc.).
'''
rifat = {"bangla", "english", "mathematics", "chemistry", "physics", "biology"}
duplicate = ["bus", "truck", "cng"]
rifat.update(duplicate)
print(rifat)
'''


                                            ##Remove Set Items

##Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
'''
#remove()
rifat = {"bangla", "english", "mathematics", "chemistry", "physics", "biology"}
rifat.remove("english")
print(rifat) #Note: If the item to remove does not exist, remove() will raise an error.Note: If the item to remove does not exist, remove() will raise an error.

#discard()
rifat1 = {"bangla1st", "english1st", "mathematics1st", "chemistry1st", "physics1st", "biology1st"}
rifat1.discard("chemistry1st")
print(rifat1)#Note: If the item to remove does not exist, discard() will NOT raise an error.

#pop()
#You can also use the pop() method to remove an item, but this method will remove a random item, 
#so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
vehicle = {"bus", "truck", "cng", "rickshaw", "pickup", "tanker"}
vehicle.pop()
print(vehicle)#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#clear()
#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#del()
#The del keyword will delete the set completely:
fruit = {"apple", "banana", "cherry"}
del fruit
print(fruit) #this will raise an error because the set no longer exists
'''


                                                ##Loop Sets

##Loop Items
#You can loop through the set items by using a for loop:
'''
vehicle = {"bus", "truck", "cng", "rickshaw", "pickup", "tanker"}
for x in vehicle:
    print(x)
#
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
'''


                                                ##Join Set

##Join Two Sets
#There are several ways to join two or more sets in Python.
#You can use the union() method that returns a new set containing all items from both sets, 
#or the update() method that inserts all the items from one set into another:

#The union() method returns a new set with all items from both sets:
'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:

myset = {"a", "b" , "c"}
orset = {1, 2, 3, 4}

myset.update(orset)
print(myset)
#Note: Both union() and update() will exclude any duplicate items.
'''

##Keep ONLY the Duplicates
###The intersection_update() method will keep only the items that are present in both sets.
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple", "tesla"}
x.intersection_update(y)
print(x)
#
#The intersection() method will return a new set, that only contains the items that are present in both sets.
m = {"microsoft", "google", "apple", "samsung"}
n = {"apple", "banana", "google"}
k = m.intersection(n)
print(k)
'''

##Keep All, But NOT the Duplicates
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
'''
#Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#
#The symmetric_difference() method will return a new set, 
#that contains only the elements that are NOT present in both sets.
m = {"apple", "banana", "cherry"}
n = {"google", "microsoft", "apple"}
k = m.symmetric_difference(n)
print(k)

'''

##Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
##True and 1 is considered the same value:
'''
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)
'''

                                            ##Python - Set Methods

##Set Methods
##python has a set of built-in methods that you can use on sets.

##add()	    Adds an element to the set
            #The add() method adds an element to the set.
            #If the element already exists, the add() method does not add the element.
            #set.add(elmnt)
'''
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
'''

##clear()	Removes all the elements from the set
            #The clear() method removes all elements in a set.
            #set.clear()
'''
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
'''

##copy()	Returns a copy of the set
            #The copy() method copies the set.
            #set.copy()
'''
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
'''

##difference()	Returns a set containing the difference between two or more sets
                #The difference() method returns a set that contains the difference between two sets.
                #Meaning: The returned set contains items that exist only in the first set, and not in both sets.
                #set.difference(set)
                #set	Required. The set to check for differences in
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
#
n = {"apple", "banana", "cherry"}
m = {"google", "microsoft", "apple"}
k = m.difference(n)
print(k)
'''

##difference_update()	Removes the items in this set that are also included in another, specified set
                        #The difference_update() method removes the items that exist in both sets.
                        #The difference_update() method is different from the difference() method, 
                        # because the difference() method returns a new set, without the unwanted items, 
                        # and the difference_update() method removes the unwanted items from the original set.
                        #set.difference_update(set)
                        #set	Required. The set to check for differences in
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
'''

##discard()	            Remove the specified item
                        #The discard() method removes the specified item from the set.
                        #This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist,
                        #and the discard() method will not.
                        #set.discard(value)
                        #value	Required. The item to search for, and remove
'''
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
#
x = {"apple", "banana", "cherry"}
x.discard("coconut")
print(x)
'''

##intersection()	    Returns a set, that is the intersection of two other sets
                        #The intersection() method returns a set that contains the similarity between two or more sets.
                        #Meaning: The returned set contains only items that exist in both sets, 
                        # or in all sets if the comparison is done with more than two sets.
                        #set.intersection(set1, set2 ... etc)
                        #set1	Required. The set to search for equal items in
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
#
m = {"a", "b", "c"}
n = {"c", "d", "e"}
l = {"f", "g", "c"}
result = m.intersection(n, l)
print(result)
'''

##intersection_update()	         Removes the items in this set that are not present in other, specified set(s)
                           #The intersection_update() method is different from the intersection() method,
                           #because the intersection() method returns a new set,
                           #without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.
                           #set.intersection_update(set1, set2 ... etc)
'''
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)
#
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
'''

##isdisjoint()	     Returns whether two sets have a intersection or not
                     #The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
                     #set.isdisjoint(set)
                     #set	 Required. The set to search for equal items in
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
#
m = {"a", "b", "c"}
n = {"c", "d", "e"}
k = m.isdisjoint(n)
print(k)
'''

##issubset()	      Returns whether another set contains this set or not
                      #The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
                      #set.issubset(set)
                      #set	Required. The set to search for equal items in
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook", "apple", "banana", "cherry"}
z = x.issubset(y)
print(z)
#
m = {"a", "b", "c"}
n = {"f", "e", "d", "c", "b"}
l = m.issubset(n)
print(l)
'''

##issuperset()	      Returns whether this set contains another set or not
                      #The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False.
                      #set.issuperset(set)
                      #set	Required. The set to search for equal items in
'''
x = {"google", "microsoft", "facebook", "apple", "banana", "cherry"}
y = {"apple", "banana", "cherry"}
z = x.issuperset(y)
print(z)
#
m = {"f", "e", "d", "c", "b"}
n = {"a", "b", "c"}
l = m.issubset(n)
print(l)
'''

##pop()	                           Removes an element from the set
                                   #The pop() method removes a random item from the set.
                                   #set.pop()
'''
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)
#Return the removed element:
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()  #Note: The pop() method returns removed value.
print(x)
'''

##remove()	                       Removes the specified element
                                   #The remove() method removes the specified element from the set.
                                   #This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, 
                                   #and the discard() method will not.
                                   #set.remove(item)
                                   #item	Required. The item to search for, and remove
'''
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
'''

##symmetric_difference()	       Returns a set with the symmetric differences of two sets
                                   #The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
                                   #Meaning: The returned set contains a mix of items that are not present in both sets.
                                   #set.symmetric_difference(set)
                                   #set	Required. The set to check for matches in
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
'''

##symmetric_difference_update()	   inserts the symmetric differences from this set and another
                                   #The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
                                   #set.symmetric_difference_update(set)
                                   #set	Required. The set to check for matches in
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
'''

##union()	                       Return a set containing the union of sets
                                   #The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
                                   #You can specify as many sets you want, separated by commas.
                                   #It does not have to be a set, it can be any iterable object.
                                   #If an item is present in more than one set, the result will contain only one appearance of this item.
                                   #set.union(set1, set2...)
                                   #set1	Required. The iterable to unify with
'''
m = {"apple", "banana", "cherry"}
n = {"google", "microsoft", "apple"}
l = m.union(n)
print(l)
#
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)
'''

##update()	      Update the set with the union of this set and others
                  #The update() method updates the current set, by adding items from another set (or any other iterable).
                  #If an item is present in both sets, only one appearance of this item will be present in the updated set.
                  #set.update(set)
                  #set	Required. The iterable insert into the current set
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
'''
