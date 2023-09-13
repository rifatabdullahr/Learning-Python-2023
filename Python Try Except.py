                                                        ##Python Try Except
                                                        

#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

                                                        ##Exception Handling

#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#These exceptions can be handled using the try statement:

'''
#The try block will generate an error, because x is not defined:
try:
    print(x)
except:
    print("An Exception Error")
    '''

#Since the try block raises an error, the except block will be executed.
#Without the try block, the program will crash and raise an error:
#This statement will raise an error, because x is not defined:
##This will raise an exception, because x is not defined:
'''
print(x)
'''


                                                            ##Many Exceptions

#You can define as many exception blocks as you want, e.g. 
#if you want to execute a special block of code for a special kind of error:
#Print one message if the try block raises a NameError and another for other errors:
'''
try:
    print(x)
except NameError:
    print("Variable not defined")
except:
    print("Something else gone error")
    '''


## Else
#You can use the else keyword to define a block of code to be executed if no errors were raised:
'''
try:
    print("Hi man")
except:
    print("There is an Error")
else:
    print("No error")
    '''


                                             ##Finally

#The finally block, if specified, will be executed regardless if the try block raises an error or not.
'''
#The finally block gets executed no matter if the try block raises any errors or not:

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try and except' has finished")
    '''
