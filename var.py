x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Case-Sensitive
a = 4
A = "Sally"
print(a)
print(A)
#A will not overwrite a

# assign multiple value in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value and multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

country = ("Ind","Usa","Uk")
a,b,c = country
print(a)
print(b)

user = {"name":"narendra", "age":25,"email":"narendra@gmail,.com"}
a,b,c = user.keys()
print(a,b,c)


# Global Variables
#Global variables can be used by everyone, both inside of functions and outside.

x = 5   # global variable
def my_func():
    print("Inside function:",x)

my_func()    
print("outside function:",x)    

a = 10
def change_value():
    a = "hello"
    print("Inside Function:",a)
change_value()
print("outside function:",a)    

# function inside variable of make a global varible for use a global keyword
a = 15
def func():
    global a
    a = "Python"
    print("Function Inside:",a)
func()    
print("function Outside:",a)    
