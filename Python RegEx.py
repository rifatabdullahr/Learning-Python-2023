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


## \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word    r"\Bain"
'''
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
 '''


## \B (the "r" in the beginning is making sure that the string is being treated as a "raw string")    r"ain\B"
'''
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)

if x :
 print("Yes, Matched")
else:
 print("no match")

 '''


## \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
'''
import re

txt = "There are 4 cars"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x :
    print("Yes,we found a digit")
else:
    print("No match")
    '''


## \D	Returns a match where the string DOES NOT contain digits	"\D"
'''
import re

txt = "There are 4 cars"

#Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x :
    print("Yes,we found a digit")
else:
    print("No match")
    '''


## \s	Returns a match where the string contains a white space character	"\s"
'''
import re

txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

  '''


## \S	Returns a match where the string DOES NOT contain a white space character	"\S"
'''
import re

txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
'''


## \w	Returns a match where the string contains any word characters (characters from a to Z, 
# digits from 0-9, and the underscore _ character)	"\w"
'''
import re

txt = "I am Hasib.I read in class 3.Last month my attendence was 100%"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  '''


## \W	Returns a match where the string DOES NOT contain any word characters	"\W"
'''
import re

txt = "I am Hasib.I read in class 3.Last month my attendence was 100%"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
'''


## \Z	Returns a match if the specified characters are at the end of the string	"Bangladesh\Z"
'''
import re

txt = "The rain in Bangladesh"

#Check if the string ends with "Bangladesh":

x = re.findall("Bangladesh\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
'''


                                                        ##Sets

#A set is a set of characters inside a pair of square brackets [] with a special meaning:

## [arn]	Returns a match where one of the specified characters (a, r, or n) is present
'''
import re

txt = "Rain in BD"
#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)
print(x)

if x:
    print("Yes, We found at least one match")
else :
    print("No match")
'''


## [a-n]	Returns a match for any lower case character, alphabetically between a and n
'''
import re

txt = "i am hasib.I read in class 3.Last month my attendence was 100%"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
    '''


## [^arn]	Returns a match for any character EXCEPT a, r, and n
'''
import re

txt = "I am hasib.I read in class 3.Last month my attendence was 100%"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)
print(x)

if x :
    print("Yes, there is at least one match!")
else:
    print("No match")
'''


## [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
'''
import re

txt = "I am hasib.I read in class 3.Last month my attendence was 100%"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
    '''


## [0-9]	Returns a match for any digit between 0 and 9
'''
import re

txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
    '''


## [0-8][0-9]	Returns a match for any two-digit numbers from 00 and 59
'''
import re

txt = "He came here at 11:20.8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-8][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
'''


## [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
'''
import re

txt = "I am hasib.I read in class 3.Last month my attendence was 100%"

#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  '''


## [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
'''
import re

txt = "I am hasib.I read in class 3.Last month my attendence was 100%"

#Check if the string has any + characters:

x = re.findall("[+]", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
  print("No match")
  '''


                                                      ## The findall() Function

# The findall() function returns a list containing all matches.
#Print a list of all matches:
'''
import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
'''
#The list contains the matches in the order they are found.
#If no matches are found, an empty list is returned:
#Return an empty list if no match was found:
'''
import re

#Return a list containing every occurrence of "Portugal":

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
  print("No match")
'''


                                                      ## The search() Function

#The search() function searches the string for a match, and returns a Match object if there is a match.
#If there is more than one match, only the first occurrence of the match will be returned:
#Search for the first white-space character in the string:
'''
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
'''
#
#If no matches are found, the value None is returned:
#Make a search that returns no match:
'''
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
'''


                                                ##The split() Function

# The split() function returns a list where the string has been split at each match:
#Split at each white-space character:
'''
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
'''
#
##You can control the number of occurrences by specifying the maxsplit parameter:
#Split the string only at the first occurrence:
'''
import re

#Split the string at the first white-space character:

txt = "When will you come?"

x = re.split("\s", txt, 1)

print(x)
'''


                                                          ##The sub() Function

#The sub() function replaces the matches with the text of your choice:
#Replace every white-space character with the number 9:
'''
import re

#Replace all white-space characters with the digit "9":
txt = "I am Rifat.Who are you?"

x = re.sub("\s", "9", txt)
print(x)
'''
##You can control the number of replacements by specifying the count parameter:
#Replace the first 2 occurrences:
'''
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
'''