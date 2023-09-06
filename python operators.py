                                                    #Python Operators



#Operators are used to perform operations on variables and values. 
                        #In the example below, we use the + operator to add together two values:
#print(10+4)
'''
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
''' 


                                                   ##Arithmetic operators
                     #Arithmetic operators are used with numeric values to perform common mathematical operations:



##(+	Addition)
'''
x = 45
y = 10	 
print(x + y)
'''

##(-	Subtraction)
'''	    
x = 60
y = -23
subtraction = x - y
print(subtraction)	
'''

##(*	Multiplication)
'''
x = 6
y = 7
c = x * y
print(c)
'''

##(/	Division)
'''
x = 90
y = 30
v = x / y
print(v)
#
m = 88
n = 25
k = m / n
print(k)
'''

##(%	Modulus)
'''
t = 40
s = 3
l = t % s
print(l)
#
x = 50
y = 10
u = x % y
print(u)
'''

##(**	Exponentiation)
'''
x = 4
y = 3  
z = x ** y	#same as 4*4*4
print(z)
#
m = 3
n = 5
k = m ** n
print(k)
'''

##(//	Floor division)
'''
x = 12
y = 5
z = x // y	##the floor division // rounds the result down to the nearest whole number
print(z)
#
a = 123.45
b = 34
c = a // b
print(c)
'''


                                                   ##Assignment Operators
                                    #Assignment operators are used to assign values to variables:



##(=	x = 5)
'''
x = 5
print(x)
'''

##(+=	x += 3   x = x + 3)
'''
x = 5
x +=3
print(x)
#
y = -10
y += 15
print(y)
'''

##(-=	x -= 3   x = x -3)
'''
x = 34
x -= 23
print(x)
#
m = -22
m -= 11
print(m)
'''

##(*=	x *= 3   x = x * 3)
'''
x = 12
x *= 3
print(x)	
'''

##(/=	x /= 3	x = x / 3)
'''
x = 23
x /= 3
print(x)
print(type(x))
'''

##(%=	x %= 3	x = x % 3)
'''
x = 31
x %= 3
print(x)	
'''

##(//=	x //= 3	x = x // 3)
'''
x = 23
x //= 3
print(x)	
'''

##(**=	x **= 3	x = x ** 3)
'''
x = 5
x **= 3
print(x)
'''
	
##(&=	x &= 3	x = x & 3)(AND)
'''         ## Program to demonstrate the Bitwise And (&) and Assign Operators in Python.   
             #a = 8 # assign value  
             #b = 13   
             #   0100  (8 in binary)  
             # & 1101  (13 in binary)  
             #  ________  
             #   0100 = 8 (In decimal)  
x = 8
x &= 13
print(x)
'''

##(|=  x |= 3	x = x | 3)(OR)
'''         ## Program to demonstrate the Bitwise OR and Assign Operators in Python.   
            # a = 6 # assign value  
            #b = 13
            #   0110  (6 in binary)  
            # | 1101  (13 in binary)  
            #  ________  
            #   1111 = 15 (In decimal)  
x = 6 
x |= 13
print(x)
'''

##(^=	x ^= 3	x = x ^ 3)(XOR)
'''          ## Program to demonstrate the Bitwise NOR and Assign Operators in Python.   
             #a = 6 # assign value  
             #b = 13   
             #   0110  (6 in binary)  
             # ^ 1101  (13 in binary)  
             #  ________  
             #   1011 = 11 (In decimal)
x = 6
x ^= 13
print(x)
'''

##(>>=	x >>= 3	 x = x >> 3)
'''           ## Program to demonstrate the Bitwise Right shift and Assign Operators in Python.   
              #https://www.youtube.com/watch?v=_RDSuXwsECc
x = 6
x >>= 13
print(x)
'''

##(<<=	x <<= 3	x = x << 3)
'''            ## Program to demonstrate the Bitwise Left shift and Assign Operators in Python.   
               #https://www.youtube.com/watch?v=uuAeBFYjPIo
x = 6
x <<= 13
print(x)
'''


                                                   ##Comparison Operators(print true/false)
                                           #Comparison operators are used to compare two values:
             

##(==	Equal	x == y)	
'''                   
x = 45
y = 30
if (x == y):
     print(True)
else:
     print(False)
#
x = 10
y = 10
print(x == y)
'''

##(!=	Not equal	x != y)
'''                       
x = 23
y = 22.99
z = ( x != y)
print(z)
'''

##(>	Greater than	x > y)
'''
x = 24
y = -24
print(x > y)
'''

##(<	Less than	x < y)
'''
x = 14 
y = 22
print(x < y)
'''

##(>=	Greater than or equal to	x >= y)
'''
x = 23
y = 35
print(x >= y)
#
x = 34
y = 20
print(x >= y)
'''

##(<=	Less than or equal to	x <= y)
'''
x = 70
y = 34
print(x <= y)
'''
                                                    ##Logical Operators
                                       #Logical operators are used to combine conditional statements:
                            
##((and)	   #Returns True if both statements are true	        x < 5 and  x < 10)
'''
x = 5
y = x > 3 and x < 10
print(y)
#
m = 10
k = m > 9 and m < 5
print(k)
'''
##((or)   	   #Returns True if one of the statements is true	x < 5 or x < 4)
'''
x = 30
y =  x > 25 or x < 43
print(y)
#
b = 45
a =  b > 25 or b < 43
print(a)
#
j = 3
h =  j > 25 or j < 2
print(h)
#
k = 12
m =  k > 25 or k < 43
print(m)
'''

##((not)	  #Reverse the result, returns False if the result is true	    not(x < 5 and x < 10))
'''
x = 30
y = not(x > 25 or x < 43)
print(y)
#
b = 45
a = not(b > 25 or b < 43)
print(a)
#
j = 3
h = not(j > 25 or j < 2)
print(h)
#
k = 12
m = not(k > 25 or k < 43)
print(m)
'''

                                            ##Identity Operators
                    #Identity operators are used to compare the objects, not if they are equal,
                    # but if they are actually the same object, with the same memory location:

## is 	    Returns     True if both variables are the same object	x is y
'''
x = ["Mango", "Banana", "Apple"]
y = ["Mango", "Banana", "Apple"]
z = x
print(x is z)       # returns True because z is the same object as x
print(x is y)       # returns False because x is not the same object as y, even if they have the same content.
print(x == y)        # to demonstrate the difference betweeen "is" and "==": 
                    #this comparison returns True because x is equal to y
'''

## is not	  Returns True      if both variables are not the same object	x is not y
'''
x = ["My Father", "My Mother", "My Sister"]
y = ["My Father", "My Mother", "My Sister"]
z = x
print(x is not z)  # returns False because z is the same object as x.
print(x is not y)  # returns True because x is not the same object as y, even if they have the same content.
print(x != y)      # to demonstrate the difference betweeen "is not" and "!=": 
                   # this comparison returns False because x is equal to y.
'''

                                            ##Membership Operators
                    #Membership operators are used to test if a sequence is presented in an object:

## in 	  Returns       True if a sequence with the specified value is present in the object	x in y
'''
x = ["This", "is", "my", "room"]
y = "room" in x         # returns True because a sequence with the value "room" is in the list.
print(y)
'''

## not in     	Returns     True if a sequence with the specified value is not present in the object	x not in y
'''
x = ["apple", "banana"]
print("pineapple" not in x)  ## returns True because a sequence with the value "pineapple" is not in the list
'''

                                            ##Bitwise Operators
                                #Bitwise operators are used to compare (binary) numbers:
     
## & 	  AND	Sets each bit to 1 if both bits are 1	     x & y
'''	
x = 6     #The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
y = 3                            #The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
print(x & y)

                                 6 = 0000000000000110
                                 3 = 0000000000000011
                                 --------------------
                                 2 = 0000000000000010
                                 ====================

                                Decimal numbers and their binary values:
                                0 = 0000000000000000
                                1 = 0000000000000001
                                2 = 0000000000000010
                                3 = 0000000000000011
                                4 = 0000000000000100
                                5 = 0000000000000101
                                6 = 0000000000000110
                                7 = 0000000000000111
'''

## |	OR	  Sets each bit to 1 if one of two bits is 1	    x | y
'''
x = 6                   # The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:
y = 8                   # 6 = 0000000000000110
print(x | y)            # 8 = 0000000000001000
                        # --------------------
                        #14 = 0000000000001110
                        # ====================
'''

## ^	XOR	   Sets each bit to 1 if only one of two bits is 1	   x ^ y
'''
x = 9                  #The ^ operator compares each bit and set it to 1 if only one is 1, 
y = 3                  #otherwise (if both are 1 or both are 0) it is set to 0:	
print(x ^ y)           # 9 = 0000000000001001
                       # 3 = 0000000000000011
                       # --------------------
                       #10 = 0000000000001010
                       # ====================
'''
 
## ~	NOT	  Inverts all the bits	  ~x	
'''
print(~5)           #The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
                    #Inverted 5 becomes -6:
                    # 5 = 0000000000000101
                    # -6 = 1111111111111010

                    #Decimal numbers and their binary values:
                    #4 = 0000000000000100
                    #3 = 0000000000000011
                    #2 = 0000000000000010
                    #1 = 0000000000000001
                    #0 = 0000000000000000
                    #-1 = 1111111111111111
                    #-2 = 1111111111111110
                    #-3 = 1111111111111101
                    #-4 = 1111111111111100
'''

## <<	 Zero fill left shift	  Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
'''
x = 12           #The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:
y = 9            #If you push 000000000 in from the left:
                 #12 = 0000000000001100
                 #becomes
                 #6144 = 0001100000000000
print(x << y)
'''

## >>	 Signed right shift	      Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	
'''
x = 8                        #The >> operator moves each bit the specified number of times to the right.
y = 3                        #Empty holes at the left are filled with 0's.
print(x >> y)                #If you move each bit 2 times to the right, 8 becomes 2:
                             #8 = 0000000000001000
                             #becomes
                             #3 = 0000000000000001
'''


###Operator Precedence
#Operator precedence describes the order in which operations are performed.
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
'''
print((6 / 3) - (4 * 2))
#
print((6 + 3) - (6 + 3))
'''

#### Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
'''
print(100 + 5 * 3)
#
print(((34* 5 -130) * 5) + 123)
'''

#Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
'''
x = 100
y = 3
print(x + ~ y)  #The calculation above reads 100 + -4 = 96
'''

#Multiplication, division, floor division, and modulus has higher precedence than addition, and needs to be evaluated first.
'''
print(100 + 5 % 3) #The calculation above reads  5 % 3 = 2
                                                # 100 + 2 =102
'''

#Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:
'''
print(5 + 4 - 7 + 3)   #The calculation above reads:
                            #5 + 4 = 9
                            #9 - 7 = 2
                            #2 + 3 = 5
'''

#Bitwise right shift   has a lower precedence than subtraction, and we need to calculate the subtraction first.
'''
print(8 >> 4 - 2)  

#The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.
'''

# & Bitwise AND     has a lower precedence than addition, and we need to calculate the addition first.
'''
print(6 & 2 + 1)    #The calculation reads 6 & 3 = 2
                    #The & operator compares each bit and set it to 1 if both are 1,
                    #otherwise it is set to 0
'''                 

# Bitwise OR        has a lower precedence than addition, and we need to calculate the addition first.
'''
print(6 | 2 + 1)    #The calculation reads 6 | 3 = 7
                    #The | operator compares each bit and set it to 1 if one or both is 1, 
                    #otherwise it is set to 0

'''

# Bitwise XOR       has a lower precedence than addition, and we need to calculate the addition first.
'''
print(6 ^ 2 + 1)     #The calculation above reads 6 ^ 3 = 5
                     #The ^ operator compares each bit and set it to 1 if only one is 1, 
                     # otherwise (if both are 1 or both are 0) it is set to 0.
'''

# Comparisons, identity, and membership operators has a lower precedence than addition, and we need to calculate the addition first.
'''
print(5 == 4 + 1)  #The calculation above reads 5 == 5 = True
'''

# not	             Logical NOT
'''                  #The logical NOT operator has a lower precedence than "like" comparison,
                     #and we need to calculate the comparison first.
print(not 5 ==5)     #The calculation reads: not True = False
'''

# and	                AND
'''                     
                        #The and operator has a higher precedence than or, and we need to calculate the and expression first.
print(1 or 2 and 3)     #The calculation reads: 1 or 3 = 1
'''

#or	                    OR
'''
                        #The or operator has a lower precedence than addition, and we need to calculate the addition first.
print(4 or 5 + 10 or 8)
                        #The calculation above reads: 4 or 15 or 8 = 4
'''