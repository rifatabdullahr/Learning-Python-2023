####python string method
###capitalize()     Converts the first character to upper case
'''
x = "i love my COUNTRY"
m = (x.capitalize())      #The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
print(m)
'''

#casefold()         Converts string into lower case
'''
x = "i love my COUNTRY"
m = (x.casefold())        #The casefold() method returns a string where all the characters are lower case.
print(m)
'''

#center()           Returns a centered string
'''                    #The center() method will center align the string, using a specified character (space is default) as the fill character.
x = "I love my COUNTRY"  ####string.center(length, character)
m = x.center(50)     
print(m)
#
txt = "I am Rifat"
x = txt.center(20, "O")
print(x)
'''

#count()            Returns the number of times a specified value occurs in a string
'''                    #The count() method returns the number of times a specified value appears in the string.
txt = "Banana is a fruit.I love Banana" ####string.count(value, start, end)
#x = txt.count("Banana")
x = txt.count("Banana", 0, 40)
print(x)
'''

#encode()           Returns an encoded version of the string
'''                   #The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt = "I am Rifät"       ####string.encode(encoding=encoding, errors=errors)
#x = txt.encode()
#print(x)
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
'''

#endswith()         Returns true if the string ends with the specified value
'''                    #The endswith() method returns True if the string ends with the specified value, otherwise False.
txt = "Banana is a fruit.I love Banana"  ####string.endswith(value, start, end)
x = txt.endswith("Banana")
print(x)
'''

#expandtabs()       Sets the tab size of the string
'''                    #The expandtabs() method sets the tab size to the specified number of whitespaces.
txt = "I\t a\tm\t R\ti\tf\ta\tt"      ####string.expandtabs(tabsize)
x = txt.expandtabs(10)
print(x)
'''

#find()             Searches the string for a specified value and returns the position of where it was found
'''                       #The find() method finds the first occurrence of the specified value.
                       #The find() method returns -1 if the value is not found.
                       #The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
txt = "Hello, welcome to my world."       #string.find(value, start, end)
#x = txt.find("welcome")
x = txt.find("o", 5, 15)
print(x)
'''


#format()           Formats specified values in a string
'''                   #The format() method formats the specified value(s) and insert them inside the string's placeholder.
                       #The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
                       #The format() method returns the formatted string.
#txt = "For only {price:} dollars!"   ####string.format(value1, value2...)
#print(txt.format(price = 49))           
txt1 = "My name is {name} and i am {years} old.".format(name = "Rifat", years = "25")  #The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
txt2 = "I am {0} and i like to write {1}.".format("Rifat", "Code")
txt3 = "This is {} and he is a good {}.".format("Rifat", "boy")
print(txt1)
print(txt2)
print(txt3) 
'''

#format_map()       Formats specified values in a string


#index()            Searches the string for a specified value and returns the position of where it was found
# find() and index() are same.If the value is not found, the find() method returns -1, but the index() method will raise an exception:

#isalnum()          Returns True if all characters in the string are alphanumeric
'''                    #The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
vb = "Rifat2730"        ####string.isalnum()
x = vb.isalnum()
print(x)
'''

#isalpha()          Returns True if all characters in the string are in the alphabet
'''                    #The isalpha() method returns True if all the characters are alphabet letters (a-z).
#x = "Myself"           ####string.isalpha()
x = "Myself Rifat @7"
b = x.isalpha()
print(b)
'''

#isascii()          Returns True if all characters in the string are ascii characters
'''                   #The isascii() method returns True if all the characters are ascii characters  (a-z).
x = "Rifat1234"        ####string.isascii()
b = x.isascii()
print(b)
'''

#isdecimal()        Returns True if all characters in the string are decimals
'''                   #The isdecimal() method returns True if all the characters are decimals (0-9).
                       #This method can also be used on unicode objects.
#Rifat = "2730"        ####string.isdecimal()
Rifat = "Name"
x = Rifat.isdecimal()
print(x)
'''

#isdigit()          Returns True if all characters in the string are digits
'''                   #The isdigit() method returns True if all the characters are digits, otherwise False.
                       #Exponents, like ², are also considered to be a digit.
#Rifat = "Name"        ####string.isdigit()
Rifat = "2730"
x = Rifat.isdecimal()
print(x)        
'''

#isidentifier()     Returns True if the string is an identifier
'''                   #The isidentifier() method returns True if the string is a valid identifier, otherwise False.      
                       #A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
                       #A valid identifier cannot start with a number, or contain any spaces.
e = "Myself"           ####string.isidentifier()
f = "Rifat2730"
g = "3men"
h = "hi! i am rifat"

print(e.isidentifier())
print(f.isidentifier())
print(g.isidentifier())
print(h.isidentifier())
'''

#islower()          Returns True if all characters in the string are lower case
'''                  #The islower() method returns True if all the characters are in lower case, otherwise False.
                      #Numbers, symbols and spaces are not checked, only alphabet characters.
a = "Hello world!"    ####string.islower()
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower()) 
'''

#isnumeric()        Returns True if all characters in the string are numeric
'''                   #The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
                      #Exponents, like ² and ¾ are also considered to be numeric values.
                      # "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
a = "rifat2456"       ####string.isnumeric()
b = "234598" 
c = "2984 939"
d = "-1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
'''

#isprintable()      Returns True if all characters in the string are printable
'''                    #The isprintable() method returns True if all the characters are printable, otherwise False.
a = "hello dear!How are you ? #1"     ####string.isprintable()
print(a.isprintable())
b = "i am rifat\n and you?"
print(b.isprintable())
'''

#isspace()          Returns True if all characters in the string are whitespaces
'''                   #The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
s = " "                ####string.isspace()
print(s.isspace())
t = "i am Rifat"
print(t.isspace())
'''

#istitle()          Returns True if the string follows the rules of a title
'''                   #The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
                       #Symbols and numbers are ignored.
d = "I Am Rifat Abdullah.My id is 2730"     ####string.istitle()                     
print(d.istitle()) 
u = "I Am Rifat Abdullah"
print(u.istitle())     
'''                 

#isupper()          Returns True if all characters in the string are upper case
'''                   #The isupper() method returns True if all the characters are in upper case, otherwise False.
                      #Numbers, symbols and spaces are not checked, only alphabet characters.
a = "Hello World!"    ####string.isupper()
b = "hello 123"
c = "MY NAME IS RIFAT"

print(a.isupper())
print(b.isupper())
print(c.isupper())     
'''

#join()             Joins the elements of an iterable to the end of the string
'''                  #The join() method takes all items in an iterable and joins them into one string.
                      #A string must be specified as the separator.
RifatTuple = ("Book", "Pen", "Pencil")     ####string.join(iterable)
msep = " @! "
print(msep.join(RifatTuple))

myDict = {"name": "John", "country": "Norway"}   
mySeparator = "TEST"          ####When using a dictionary as an iterable, the returned values are the keys, not the values.
x = mySeparator.join(myDict)
print(x)
'''

#ljust()            Returns a left justified version of the string
'''                   #The ljust() method will left align the string, using a specified character (space is default) as the fill character.
t = "Mango"            ####string.ljust(length, character)
x = t.ljust(20)        #In the result, there are actually 15 whitespaces to the right of the word Mango.
m = "Cricket"            
j = m.ljust(20, "@")
print(x, "is my favourite fruit")    
print(j, "is my favourite game")
'''

#lower()            Converts a string into lower case
'''                 #The lower() method returns a string where all characters are lower case.
                     #Symbols and Numbers are ignored.
v = "HI THERE!How are you?" ####string.lower()
print(v.lower())
'''

#lstrip()           Returns a left trim version of the string
'''                   #The lstrip() method removes any leading characters (space is the default leading character to remove)
g = "         pen        "    ####string.lstrip(characters)
h = g.lstrip()
print("Does this", h, "belong to you")

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)
'''

###maketrans()        Returns a translation table to be used in translations
'''                   #The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
                                 ####str.maketrans(x, y, z)
                                 #x	Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
                                 #y	Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
                                 #z	Optional. A string describing which characters to remove from the original string.
r = "I am Rifat"
table = str.maketrans("R", "S") 
l = r.translate((table))
print(l)
#
txt  = "I love my Family"
x = "voel"
y = "kiel"
table = str.maketrans(x, y)
z = txt.translate((table))
print(z)
#
txt = "Good Night Sam"
x = "aSm"
y = "oJe"
z = "odghtN"
table = str.maketrans(x, y, z)
s = txt.translate((table))
print(s)
'''

#partition()        Returns a tuple where the string is parted into three parts
'''                    #The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
                       #The first element contains the part before the specified string.
                       #The second element contains the specified string.
                       #The third element contains the part after the string.
x = "He is a Bus lover"  ####string.partition(value)
k = x.partition("Bus")
print(k)  
#This method searches for the first occurrence of the specified string.
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)
'''

#replace()          Returns a string where a specified value is replaced with a specified value
'''                   #The replace() method replaces a specified phrase with another specified phrase.
#x = "I love Mango"     ####string.replace(oldvalue, newvalue, count)
#t = x.replace("Mango", "Banana")
#print(t)
#All occurrences of the specified phrase will be replaced, if nothing else is specified.
txt = "Three Two Three, Go"
x = txt.replace("Three", "One", 1)
print(x)
'''

#rfind()            Searches the string for a specified value and returns the last position of where it was found
'''                   #The rfind() method finds the last occurrence of the specified value.
                       #The rfind() method returns -1 if the value is not found.
                       #The rfind() method is almost the same as the rindex() method. 
txt = "Hi Refat, I am Rifat."  ####string.rfind(value, start, end)
x = txt.rfind("Rifat")
print(x)             
#
txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)          
#
txt = "Where do you live?"
x = txt.rfind("e", 0, 10)
print(x)
#
txt = "Where do you live?"
x = txt.rfind("Work", 0, 10)
print(x)
'''

#rindex()           Searches the string for a specified value and returns the last position of where it was found
'''                   #The rindex() method is almost the same as the rfind() method.
                       #The difference is rindex() method raises an exception if the value is not found.
                       ####string.rindex(value, start, end)
'''

#rjust()            Returns a right justified version of the string
'''                   #The rjust() method will right align the string, using a specified character (space is default) as the fill character.
                       #ljust() and rjust() work function are almost same.
                       #l for the left justified.
                       #r for the right justified.
txt = "banana"         #####string.rjust(length, character)
x = txt.rjust(20, "O")
print(x)  
'''                     

#rpartition()       Returns a tuple where the string is parted into three parts
'''                   #The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
                       #The first element contains the part before the specified string.
                       #The second element contains the specified string. 
                       #The third element contains the part after the string
txt = "I could eat bananas all day, bananas are my favorite fruit"    ####string.rpartition(value)
x = txt.rpartition("bananas")
print(x)           
#
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)         
'''   
#rsplit()           Splits the string at the specified separator, and returns a list
'''                   #The rsplit() method splits a string into a list, starting from the right.
                       #If no "max" is specified, this method will return the same as the split() method.
r = "book, pen, prncil"  ####string.rsplit(separator, maxsplit)  
txt = r.rsplit(", ") 
print(txt)  
#
r = "book, pen, prncil"  
txt = r.rsplit(", ", 1) 
print(txt)     
'''           

#rstrip()           Returns a right trim version of the string
'''                   #The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
v = "           Book            "  ####string.rstrip(characters)
c = v.rstrip()
print(c)
#
t = "This is a book..,,,,sqw"
m = t.rstrip(",.sqw")
print(m)
'''
#split()            Splits the string at the specified separator, and returns a list
'''                   #The split() method splits a string into a list.
                       #You can specify the separator, default separator is any whitespace.
                       #When maxsplit is specified, the list will contain the specified number of elements plus one.
b = "this is a book and i love books"   ####string.split(separator, maxsplit)
c = b.split()
print(c)                      
#
v = "I#love#my#country"
w = v.split("#", 2)
print(w)
#
b = "this is, a book, and i love, books"   
c = b.split(",",3)
print(c)
'''

#splitlines()       Splits the string at line breaks and returns a list
'''                   #The splitlines() method splits a string into a list. The splitting is done at line breaks.
r = "I am rifat.\nWho are you?"  ####string.splitlines(keeplinebreaks)
t = r.splitlines()
print(t)
#
txt = "There is a library.\nWe can read many books in there"
x = txt.splitlines()    #Specifies if the line breaks should be included (True), or not (False). Default value is False
print(x)
'''
#startswith()       Returns true if the string starts with the specified value
'''                   #The startswith() method returns True if the string starts with the specified value, otherwise False.
h = "May i come in?"   ####string.startswith(value, start, end)
v = h.startswith("May")##value Required. The value to check if the string starts with
print(v)
#
k ="Hi how are you?"
b =k.startswith("are", 7, 12)
print(b)
'''

#strip()            Returns a trimmed version of the string
'''                   #The strip() method removes any leading, and trailing whitespaces.
                       #Leading means at the beginning of the string, trailing means at the end.
                       #You can specify which character(s) to remove, if not, any whitespaces will be removed.
txt = "     banana     "  ####string.strip(characters)
x = txt.strip()
print("of all fruits", x, "is my favorite")  
#
# txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)  
'''

#swapcase()         Swaps cases, lower case becomes upper case and vice versa
'''                   #The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello,My Name Is RIFAT"  ####string.swapcase()
x = txt.swapcase()
print(x)
#
txt = "ASDFlkjhg"  ####string.swapcase()
x = txt.swapcase()
print(x)
'''

#title()            Converts the first character of each word to upper case
'''                   #The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
                       #If the word contains a number or a symbol, the first letter after that will be converted to upper case.
y = "hello how Are YOu?" ####string.title()
x = y.title()
print(x)     
#
txt = "Welcome to my 2nd world"
z = txt.title()
print(z)
#
n = "hello b2b2b2 and 3g3g3g"
m = n.title()
print(m)
'''
                
#translate()        Returns a translated string
'''                   #The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
                       #Use the maketrans() method to create a mapping table.
                       #If a character is not specified in the dictionary/table, the character will not be replaced.
                       #If you use a dictionary, you must use ascii codes instead of characters.
                       ####string.translate(table)
                       #table	Required. Either a dictionary, or a mapping table describing how to perform the replace
f = {83 : 80}  ##use a dictionary with ascii codes to replace 83 (S) with 80 (P):
s = "Hello Sam"
v = s.translate(f)
print(v)
#
txt  = "I love my Family"
x = "voel"
y = "kiel"
table = str.maketrans(x, y)
z = txt.translate((table))
print(z)
#
txt = "Good Night Sam"
x = "aSm"
y = "oJe"
z = "odghtN"
table = str.maketrans(x, y, z)
s = txt.translate((table))
print(s)
#
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))
'''

#upper()            Converts a string into upper case
'''                   #The upper() method returns a string where all characters are in upper case.
                       #Symbols and Numbers are ignored.
txt = "Hello my friends" ####string.upper()
x = txt.upper()
print(x)   
'''

#zfill()            Fills the string with a specified number of 0 values at the beginning
'''                   #The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
                       #If the value of the len parameter is less than the length of the string, no filling is done.
txt = "50"             ####string.zfill(len)
x = txt.zfill(100)     ##len Required. A number specifying the desired length of the string
print(x)
#
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(100))
print(c.zfill(10))
'''