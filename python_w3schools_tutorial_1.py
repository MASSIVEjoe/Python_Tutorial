# print(__version__)

# Python Indentation
if 5>2:
    print("Five is greater than two!")

# Python variables

'''
Multiline Comments
'''

print(5)


# No need to declare any variables
# int x --- C
# x = 5 python

# TO specify data type
x =str(3)
y = int(4)

print(type(x))
print(type(y))

# String variables can be declared in '' or " "

x = "Test"
x = 'test'

# Naming convention

# Camel Case
myVariableName = "Apache"

# Pascal Case
MyVariableName = "Prachand"

# Snake Case
my_variable_name = "Eurocopter Tiger"

print(myVariableName)
print(MyVariableName)
print(my_variable_name)


# Many Values to Multiple Variables.

x,y,z = "Orange","Banana","Cherry"

print(x)
print(y)
print(z)


# Unpack a Collection
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)



# Output the variable
a = "Python "
b = "is "
c = "awesome"

print(a+b+c)


# Global Variable - variables declared outside the function

x = "awesome"

def myfunc():
    print("Python is "+x)

myfunc()


# Local Variable - variabes declared inside the function

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is "+x)

myfunc()
print("Python is "+x)


# Global variable - We can use the variable declared inside the function using this.

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# Built-in Data Types

x = "Hello World"   #str
x = 20  # int
x = 20.5  # float
x = 1j  # complex
x = ["apple","banana","cherry"]  # list
x = ("apache","prachand","dhruv") # Tuple
x = range(6)  # range
x = {"Name":'Rudra',"Type":"Helicopter"} #dict
x = frozenset({"Arjun","T-90","T-72"}) # frozenset
x = True #bool
x = b"Hello" #bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5))  # memoryview
x = None #Nonetype

# Random Number

import random

print(random.randrange(1,10))

# Looping through a String

for x in "elephant":
    print(x)

# String Length

a = "Hello, World"
print(len(a))


# Check String
txt = "The best things in life are free"
print("free" in txt)

# Using IF Statment
txt = "The best things in life are free"
if "free" in txt:
    print("Yes, 'free' is present")

# Check if NOT

txt = "The Best things in life are free"
print("expensive" not in txt)


#

txt = "The best things in life are free"
if "expensive" not in txt:
    print("No, 'expensive' is not present")


# Slicing Strings

b = "Hello World!"
print(b[2:5])

# Slice from Start
print(b[:5])

# Slice to the End
print(b[2:])


# Negative Indexing
print(b[-5:-2])

# Modify Strings

# UPPER CASE

a = "Eurofighter Typhoon"
print(a.upper())

# Lower
print(a.lower())

# Remove Whitespace

z = " Airbus A331"
print(z.strip())

# Replace String

e = "Hello World!"
print(e.replace("H","J"))

# Split String

a = "Hello, World!"
print(a.split(","))

g = "Eurocopter Typhoon"
print(g.split())


# Python Concatenation

n = "Hello"
m = "World"
#c = n+m
c = n+" "+m

print(c)

# Combine Strings with Numbers
# age = 36
# txt = "My Name is John, I am" + age
# print(txt)


# format() -- method

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# The format() method takes unlimited number of arguments, and are placed into the respective placeholders

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."

print(myorder.format(quantity, itemno, price))


# Another approach

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# Escape Character

txt = "We are the so called \"Vikings\" from the north"
print(txt)


# Boolean Value

print(10>9)

print(10 == 9)

# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))


# Function can Return a Boolean
def myfunc():
    return True

print(myfunc())

# isinstance function

x = 200
print(isinstance(x,int))