                                                            ##Python RegEx

#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.


                                            ##RegEx Module

#Python has a built-in package called re, which can be used to work with Regular Expressions.
#Import the re module:
'''
import re
'''


                                            ##RegEx in Python

#When you have imported the re module, you can start using regular expressions:
#Search the string to see if it starts with "The" and ends with "Spain":
'''
import re

txt = "The Rain in Spain"
x = re.search("^The.*Spain$", txt)

if x :
    print("Yes,We found a match")
else :
    print("No match")

    '''


                                                ##RegEx Functions
'''
The re module offers a set of functions that allows us to search a string for a match:

Function	                        Description
____________________________________________________________________________________________
findall	                Returns a list containing all matches
search	                Returns a Match object if there is a match anywhere in the string
split	                Returns a list where the string has been split at each match
sub	                    Replaces one or many matches with a string

'''


                                                ##Metacharacters

#Metacharacters are characters with a special meaning:

## []	   A set of characters	     "[a-m]"
'''
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)

'''


## \	Signals a special sequence (can also be used to escape special characters)	"\d"
'''
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

'''


## .	Any character (except newline character)	"he..o"
'''
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)
'''


## ^	Starts with	     "^hello"
'''
import re

txt = "Hello, This is Rifat"

#Check if the string starts with 'hello':
x = re.findall("^Hello", txt)

if x :
    print("Here it matched")
else :
    print("no matched")
'''


## $	Ends with	"planet$"
'''
import re

txt = "Hi everyone.Welcome to Planet"

x = re.findall("Planet$", txt)

#Check if the string ends with 'planet':

if x :
    print("Yes,ends with Planet")
else :
    print("No Match")
'''


## *	Zero or more occurrences	"he.*o"
'''
import re

txt  = "Hello, I am Rifat"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("He.*o", txt)

print(x)
'''


## +	One or more occurrences	"he.+o"
'''
import re

txt ="I am Rifat"
#Search for a sequence that starts with "Ri", followed by 1 or more  (any) characters, and an "t":

x = re.findall("Ri.+t", txt)

print(x)
'''


## ?	Zero or one occurrences	"he.?o"
'''
import re

txt = "I am Rifat"

#Search for a sequence that starts with "Ri", followed by 0 or 1  (any) character, and an "t":

x = re.findall("Ri.?t", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "Ri" and the "t"
'''


## {}	Exactly the specified number of occurrences	"he.{2}o"
'''
import re

txt = txt = "He is Rifat"

#Search for a sequence that starts with "Ri", followed excactly 2 (any) characters, and an "t":

x = re.findall("Ri.{2}t", txt)

print(x)
'''


##  |	Either or	"falls|stays"
'''
import re

txt = "I am Rifat and he is Hasib"

#Check if the string contains either "am" or "are":

x = re.findall("am|are", txt)
print(x)
if x :
    print("Yes,At least we found one match")
else :
    print("No match")
'''


## ()	Capture and group
'''

'''


                                                    ##Special Sequences

# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

## \A	Returns a match if the specified characters are at the beginning of the string	 "\AThe"
'''
import re 

txt = "Rahim loves his country"

#Check if the string starts with "The":

x = re.findall("\ARahim", txt)

print (x)

if x :
    print("Yes,The sentence starts with Rahim")

else :
    print("No it isn't")

    '''


## \b	Returns a match where the specified characters are at the beginning or at the end of a word    r"\bain"
'''
import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)
if x :
    print("Yes,This matched")

else :
    print("No it doesn't match")

#
#
#
    
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")     r"ain\b"

import re

txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  '''
