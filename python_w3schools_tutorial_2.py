# Python In Built Data Types
# List, Tuple, Set and Dictionary
######################################################
# List
mylist = ["apple","banana","cherry"]

print(mylist)

# How to index list items

# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# List allow duplicates

thislist = ['QRSAM','VL-SRSAM','MR-SAM','QRSAM','AKASH-NG','S-400']
print(thislist)

print(len(thislist))

# List Items - Data Types

list1 = ["Tejas","C-130","B-1B Lancer"]
list2 = [2013,1950,1970]
list3 = [True,False,True]

print(list1)
print(list2)
print(list3)

# Hetero data type
list4 = ["abc",34,True,45.6]
print(list4)

print(type(list4))

# List Constructor

print(list(('apple','nanana','orange')))

# Accessing the List Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change list items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Change List using Range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# Inserting Less items than Original
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Method - Custom insert at any place
thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

# Add List Items
# Append Items - Add Items at the end
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Append one list to another list
# extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

### extend() method can join (tuples, sets, dictionaries etc)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print(type(thislist))


## Remove specified Items
# Remove() method
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# pop() method

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Not specifying index in pop will remove last entry

# Del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete the entire list
# thislist = ["apple", "banana", "cherry"]
# del thislist

# Clear List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Python Loop List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through Index
thislist = ["Kawasaki C2","LM C130","Embraer KC390"]
for i in range(len(thislist)):
  print(i)
  print(thislist[i])

while i< len(thislist):
  print(thislist[i])
  i=i+1

print(range(3))

# List Comprehension
# Shorcut to create new list from existing list

bike = ["KTM","TVS","Bajaj","Honda","Yamaha","Suzuki","Hero"]
newlist = []

# for x in bike:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# Shortcut
# Syntax -- newlist = [expression for item in iterable if condition == True]

newlist = [x for x in bike if "a" in x]
print(newlist)

# Bike without a letter
newlist = [x for x in bike if "a" not in x]
print(newlist)

newlist = [x for x in bike]
print(newlist)



# Iterable
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression

newlist = [x.upper() for x in bike]
print(newlist)


newlist  = ['hola' for x in bike]
print(newlist)

# Expression with Condition
newlist = [x if x!= "KTM" else "Husqvarna" for x in bike]
print(newlist)


# Sorting in Python 
# Ascending Order
bike.sort()
print(bike)

# descending order
bike.sort(reverse = True)
print(bike)

# Sorting - Custamize sort function
def myfunc(n):
  return abs(n-50)

thislist = [100,50,65,83,24]
thislist.sort(key = myfunc)
print(thislist)

# Sorting is case sensitive
# caps vs small. Caps will be sorted first followed by small letter.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# To avoid this

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# To make a copy of list
# Trial list1 = list2 will have changes in both list everytime
list1 = ['a','b','c']
list1[1] = 'd'
list2 = list1
print(list1)
print(list2)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Join 2 list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append list elements one by one
for x in list2:
  list1.append(x)

print(list1)


# extend method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
