# def my_function():
# 	print("Hello from a function")

# my_function()


# def my_function(fname):
# 	print(fname + " Topley")

# my_function("Recce")
# my_function("Sam")
# my_function("Goku")

# # my_function(fname) --- > parameter
# # my_function("Recce") --- > argument


# # Function should correct number of arguments

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# # *args --- > Can get n number of arguments in a tuple and print by indexing the tuple

def my_function(*kids):
	print("The youngest child is " + kids[2])

my_function("Amar", "Akbar","Antony")


# Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# **kwargs  --- Receive arguments as dictionary

def my_function(**child):
	print("His name is  "+ child["lname"])

my_function(fname = 'Peter' ,lname = 'Parker')


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# passing a list

def my_function(food):
	for x in food:
		print(x)
fruits = ["apple","mango","orange"]
my_function(fruits)


def my_function(x):
	return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def myfunction():
	pass


def tri_recursion(k):
	if (k>0):
		result = k + tri_recursion(k-1)
		print(result)
	else:
		result = 0
	return result

print("\n\nRecursion Example Results")
tri_recursion(6)



### Lambda Function Python
# A lambda function is a small anonymous function.


# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))


x = lambda a, b : a*b
print(x(5,6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



# Usage of Lambda function

def my_toss(n):
	return lambda a : a*n

mydoubler = my_toss(5)
print(mydoubler(11))

# print(my_toss(5))


### Arrays

cars = ["Ford","Volvo","BMW"]

x = cars[0]
print(x)


print(len(cars))


for x in cars:
	print(x)

cars.append("Genesis")
cars.pop(1)


cars.remove("Vovlo")
