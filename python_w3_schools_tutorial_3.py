# Tuples

# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

mytuple = ("apple","banana","cherry")
print(type(mytuple))


# Indexing the Tuple Items
# Ordered
# Unchangeable or Immutable
# Allow Duplicates

mytuple = ("apple","banana","cherry","apple","cherry")
print(mytuple)

# Length of Tuple
print(len(mytuple))



# Create Tuple with One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

# The output will be Tuple for the above one

thistuple = ("apple")
print(type(thistuple))

# The output will be string

# Supports String, Int and Boolean data types. (Distinct or combination)
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Tuple Constructor

thistuple = tuple(("Nissan", "Renault","Mitsubushi"))
print(thistuple)


######################################################################

# Accessing the Tuple (Simillar to List)

thistuple = tuple(("Nissan", "Renault","Mitsubushi","Honda","Toyato","Suzuki"))

# Indexing (Positive, Negative and Range)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

# Check item present in Tuple
if "Honda" in thistuple:
  print("Yes, 'Honda' is in the manufacturers tuple")


################################################################

# Change Tuple Values

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x  = ('Boeing', 'HAL', 'Chengdu')
y = list(x)
y[1] = 'Lockheed Martin'
x = tuple(y)

print(x)


# Add Items
# Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

# Convert into List and Do the Append mode

x = ('Boeing', 'Airbus','Embraer','Bombardier')

y = list(x)
y.append('Comac')
x=tuple(y)

print(x)


# Add Tuple to a Tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove a item from Tuple (Tip: Convert into a List)

thistuple = ("Tata", "Ashok Leyland", "Eicher")
y = list(thistuple)
y.remove("Eicher")
thistuple = tuple(y)
print(y)


# Delete the Tuple completely

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists



################################################################


# Packing and Unpacking Tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

bikes = ('TVS', 'KTM','Bajaj','Hero')

(a,b,c,d) = bikes

print(a,b,c,d)

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# Using Asterisk *

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#################################################################


# Loop Through a Tuple

thistuple = ("Tejas","Tejas MK2","AMCA")

for x in thistuple:
  print(x)


# Loop through the Index Numbers
thistuple = ("Tejas","Tejas MK2","AMCA")
for i in range(len(thistuple)):
  print(thistuple[i])


# While Loop Usage

fighter = ("Sukhoi-30","J-20","F-16","Eurofighter","Tejas")
i = 0
while i < len(fighter):
  print(fighter[i])
  i = i+1


#############################################################################

# Join Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples

fruits = ("alpha","beta","Gamma")
mytuple = fruits*2

print(mytuple)


# Tuple Methods
# count()
# index()

print(fighter.count('Tejas'))



###################################################################

# Set

myset = {"apple","banana","cherry"}

# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.


# Sets are unordered, so you cannot be sure in which order the items will appear.

#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

thisset = {'splendor','shine 100','ct100'}

# No Duplicates

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:


# Length of the set.
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Set can have Int, String and Boolean and combination of all

set1 = {"abc", 34, True, 40, "male"}

# Type
print(type(set1))

# The Set constructor

thisset = set(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thisset)


##############################################################################

# Access the Item in a set

# Only For Loop will work

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Check any item is present in the set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


## Note: We cannot change the set items. But we can add new items.


##################################################################################

# Add Set Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)



#############################################################################

# Remove Items

thisset = {"BMW","Audi","Mercedes Benz","Porsche"}

thisset.remove("Audi") 
# thisset.discard("Audi")  -- No error will be thrown

print(thisset)


## Usage of Pop Method

# Remove the random item in a set
thisset.pop()

print(thisset)

# Clear method

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

## Del Keyboard

# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset)


## Loop through the Set

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


## Join the sets

## Union and Update method

set1 = {1,2,3}
set2 = {'a','b','c'}

set3 = set1.union(set2)
print(set3)

# update method

set1.update(set2)

print(set1)

## Keep only the duplicates

x = {'apple','orange','banana','kiwi'}
y = {"google","microsoft","apple"}

x.intersection_update(y)

print(x)
print(type(x))

z = x.intersection(y)

print(z)
print(type(x))


### Keep all except the Duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

## True and 1 are consider same

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)


######################################################################################

## Dictionary in Python

## >> Ordered
## >> Changeable
## >> No duplicates
## >> Key : Value pairs

thisdict = {
  "brand" : "Mustang",
  "YOM": 1964,
  "Engine_capacity": 6.0
}


print(len(thisdict))

## Constructor in Dictionary

thisdict_1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict_1)

### Accessing the Dictionary Items

x = thisdict["Engine_capacity"]
print(x)


## Get Keys
print(thisdict.keys())

## Get Values
print(thisdict.values())

## Get Items - Print Key and Values
print(thisdict.items())


## Check if key exists

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


### Change Values in Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

## Update method

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


## Add Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

## Update Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

## Remove Dictionary

## Pop method

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

## Remove last inserted item - popitem()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

## We can use del keyword to delete key or entire dictionary

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

## Clear dictionary -- Empty dictionary

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

########################################################################

## Loop through the dictionary

for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x,y in thisdict.items():
  print(x,y)


### Copy the dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


### Nested Dictionaries

mybikes = {
  "Apache" : {
  "type" : "Commuter",
  "CC": 160
  },
  "Street Triple RS": {
  "type" : "Sports Bike - Naked",
  "CC": 765
  },
  "Curvv": {
  "type" : "Car",
  "CC": 1500
  }
}

## Access the item in nested dictionary above

print(mybikes["Curvv"]["type"])