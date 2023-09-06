                                                ##Python Iterators

#An iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#Technically, in Python, an iterator is an object which implements the iterator protocol, 
#which consist of the methods __iter__() and __next__().


                                                ##Iterator vs Iterable

#Lists, tuples, dictionaries, and sets are all iterable objects. 
#They are iterable containers which you can get an iterator from.

#All these objects have a iter() method which is used to get an iterator:
#Return an iterator from a tuple, and print each value:
'''
thistuple = ("Rifat", "Hasib", "Mahin")
myit = iter(thistuple)

print(next(myit))
print(next(myit))
print(next(myit))
#
#Even strings are iterable objects, and can return an iterator:
#Strings are also iterable objects, containing a sequence of characters:

myname = "Rifat Abdullah"
it = iter(myname)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

'''


                                                ##Looping Through an Iterator

#We can also use a for loop to iterate through an iterable object:
#Iterate the values of a tuple:
'''

fruit_names = ("Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi", "Lemon", "Mango", "Orange")

for x in fruit_names:
    print(x)
#
#Iterate the characters of a string:

myname = "Rifat Abdullah"

for x in myname:
    print(x)
#The for loop actually creates an iterator object and executes the next() method for each loop.
'''


                                                ##Create an Iterator

#To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

#all classes have a function called __init__(), 
#which allows you to do some initializing when the object is being created.

#The __iter__() method acts similar, you can do operations (initializing etc.), 
#but must always return the iterator object itself.

#The __next__() method also allows you to do operations, and must return the next item in the sequence.
'''
class mynumbers:

    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''


                                                        ##Stop Iteration

#The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
#To prevent the iteration from going on forever, we can use the StopIteration statement.
#In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
'''
class mynumbrs:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a +=1
            return x
        else:
              raise StopIteration
        
myclass = mynumbrs()
myiter = iter(myclass)

for x in myiter:
    print(x)
'''