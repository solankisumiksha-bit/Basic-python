# python basic 


# literals
# literals are the data that is given in a variable or constant.
# example: a=10, b=20.5, c="hello", d=True

#keywords
# keywords are the reserved words in python that have a special meaning. 
# example: if, else, for, while, def, class, return, import, 
# and, or, not, is, in, break, continue, pass, try, except,
#  finally, raise, with, as, lambda, yield, global, nonlocal,
#  assert, del

# identifiers
# identifiers are the names given to variables, functions, classes, etc.

#primitive data types
# primitive data types are the basic data types in python.
# example: int, float, str, bool, complex 


# How to join strings together in Python?
# In Python, you can join strings together using the + operator or
#  the join() method.for example:
# using + operator   
"""
a = "Hello"
b = "World"
c = a + " " + b 
# print(c)
 # Output: Hello World
print(type(c))
 # Output: <class 'str'>
d = 10
print(type(d))
 # Output: <class 'int'>
f = 20.5
print(type(f))
 # Output: <class 'float'>
g = True
print(type(g))
 # Output: <class 'bool'>
j = 1 + 2j
print(type(j))
 # Output: <class 'complex'>
k = [1, 2, 3, 4, 5]
print(type(k))
 # Output: <class 'list'>
u = (1, 2, 3, 4, 5)
print(type(u)) 
# Output: <class 'tuple'>
v = {1, 2, 3, 4, 5}
print(type(v)) 
# Output: <class 'set'>
w = {"name": "John", "age": 30}
print(type(w))
 # Output: <class 'dict'>
y = None
print(type(y)) 
# Output: <class 'NoneType'>
t = b"Hello"
print(type(t))
 # Output: <class 'bytes'>
h = bytearray(b"Hello")
print(type(h))
 # Output: <class 'bytearray'>
"""
#arithmetic operators
# arithmetic operators are used to perform mathematical operations.
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
square = a ** 2
modulus = a % b
print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
"""

#comparison operators
# comparison operators are used to compare two values.
# example: ==, !=, >, <, >=, <=
"""
c = 10
d = 20
b = 20
print(c == d) # False
print(c != d) # True
print(c > d) # False
print(c < d) # True
print(c >= d) # False
print(c <= d) # True
print(d == b) # True
print(d != b) # False etc"""

# logical operators
# logical operators are used to combine conditional statements.
# example: and, or, not
"""
true and True # True
true and False # False
false and True # False
false and False # False
true or True # True
true or False # True
false or True # True
false or False # False 
true and not True # False
true and not False # True
false and not True # False
false and not False # False
"""

# assignment operators
# assignment operators are used to assign values to variables.
# example: =, +=, -=, *=, /=, %=, **=, //=

# bitwise operators
# bitwise operators are used to perform bitwise
#  operations on binary numbers.

# precedence of operators
# precedence of operators is the order in
#  which the operators are evaluated.
#example: (), **, +x, -x, ~x, *, /, //,
#  %, +, -, <<, >>, &, ^, |, ==, !=, >,
#  <, >=, <=, is, is not, in, not in, and, or



s = 34
result = s + 5 * 2 - 3 / 1 ** 2
# print(result) 
#result used to be 43.0 but now it is 44.0 because
#  of the precedence of operators.

#functions write the function name print , input, len, type,
#  str, int, float, bool, list, tuple, set, dict, etc.
#   Numric functions: abs(), round(), pow(), divmod(), max(), min(), sum()
#example: 
"""
abs(-5) # 5,
round(3.14159, 2) # 3.14,
pow(2, 3) # 8,
divmod(7, 3) # (2, 1),
max(1, 2, 3) # 3,
min(1, 2, 3) # 1,
sum([1, 2, 3]) # 6
print(abs(-5)) # 5
print(round(3.14159, 2)) # 3.14
"""

# coding practices
""" 
when all the length of the sides of the triangle is - a,b,c 
area = square root of s(s-a)(s-b)(s-c) where
 s = (a+b+c)/2 

example:of sum of the area of triangle using python code is given below:

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("The area of the triangle is:", area)

"""
# percent = (sub + sub1 + sub2 ) / 3





###STRING SLICING
# name = "hello world"
# print(name[0:3]) # answer: hel

#f or example, if we want to slice the string from index 0 to index 3, 
# we can use the slicing operator [0:3]. This will give us the substring 
# "hel" from the original string "hello world".

sub1 = 120
sub2 = 30
sub3 = 50 
name = "jatin"
presentage = (sub1 + sub2 + sub3) / 300 * 100


# print(f"my name is {name} and my marks are {sub1 + sub2 + sub3}") # answer: my name is jatin and my marks are 200
#

##\n are used to print the output in a new line. For example,
#  if we want to print the name and marks in a new line, we can use the \n operator.
#  This will give us the output in a new line. example:
# print(f"my name is {name} i get {presentage}%\n") # answer: my name is jatin and my marks are 200



#escape sequences 
#\n it ues for new line 
# \t it ues for tab space
# \\ it ues for backslash
# \'. it ues for single quote




# opration on string 
# membeship use for checking the membership of a string in another string.
#  example: 'a' in 'hello' # False 
# strip used to remove the whitespace from the beginning and end of a string.
#  example: ' hello '.strip() # 'hello'
# replace used to replace a substring with another substring in a string.
#  example: 'hello world'.replace('world', 'python') # 'hello python'
s1 = "hello world"
#print(s1 in("o")) # False
#print(s1 not in("p"))# False
#print(s1.strip()) # hello world
#print(s1.replace("world", "python")) # hello python

# comparison operators
# comparison operators are used to compare two strings.
# print(s1 == "hello world") # True
# print(20 == "hi") # False

# remove the whitespace from the beginning and end of a string.
# print(s1.strip("he")) 
# print(s1.replace("world", "python")) # hello python
"""
# count used to count the number of occurrences of a substring in a string.
print(s1.count("o")) # 2
# cases use to check the case of a string. example: s1.islower() # False, s1.isupper() # False
print(s1.islower()) # False
print(s1.isupper()) # False
# endswith and startswith
print(s1.endswith("world")) # True
print(s1.startswith("hello")) # True
"""


## lists in python 
# lists are used to store multiple items in a single variable.
# example:
my_list = [1, 2, 3, 4, 5]
 # slicing in list
# slicing is used to get a subset of a list.example:
# print(my_list[0:3]) # [1, 2, 3]

#concat used to join two or more lists together. example:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3) # [1, 2, 3, 4, 5, 6]

# repeat used to repeat a list multiple times. example:
list4 = [1, 2, 3]
list5 = list4 * 3
print(list5) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

 # append used to add an item to the end of a list. example:
list6 = [1, 2, 3]
list6.append(4)
print(list6) # [1, 2, 3, 4]

# insert used to add an item at a specific index in a list. example:
list7 = [1, 2, 3]
list7.insert(1, 4)
print(list7) # [1, 4, 2, 3]


