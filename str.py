# String 
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

print("string")
print("hello")
print('hello')
print("------------------")

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes
# we  can use three double quotes and three single quotes:
print("Multiline string")
a= a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("------------------")

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
print("Looping Throgh")
fruites = "Mangos"
for x in fruites:
    print(x)
print("--------------------------")    

# String lenght
print("String lenght")
a = "Hello Python"
print(len(a))  # count a white spaces
print("-----------------------")


# String check
# check string for use IN and Not IN keyword
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
if "hello" not in txt:
    print("yes","hello not present")
    
print("-----------------------")
    
# String Slicing 

a = "python" 
print("String Slicing")   
print(a[0:4])  # pyth
print(a[::2])   # pto
print(a[1:9])  #ython
print(a[::-1])  # nohtpy
print(a[1:3:-2]) # no output
print(a[-1:-5])   # no output
print(a[-1:-3:-2]) # n
print(a[-6:-2])  # pyth
print(a[-5:-1:2])  #yh
print(a[-6:-1:-2])  # no output
print(a[6:3:-2])  # n

print("---------------------------")

## Modify Strings 

# upper case
print("Upper case")
name = "Narendra patidar"
print("Upper case:",name.upper())  # NARENDRA PATIDAR
print("Lower Case",name.lower())   # narendra patidar
print("Capitalize:",name.capitalize())   # Narendra patidar

# remove whitespace
a = " hello word "  # The strip() method removes any whitespace from the beginning or the end:
print("remove whitespaces:",a.strip())  # hello word

a = "Hello, World!"
print("replace string:",a.replace("H", "J"))  # Jello, World!

# Split String
print("Split String:",a.split(','))

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print("String Concatenation:",c)


# String Format
# age = 36
# txt = "My name is John, I am " + age
# print(txt)  # As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

print("------------------------")

# Escape caractor
print("Escape Caractor")
txt = 'It\'s alright.'
print(txt) 
txt = "Hello\rWorld!"
print(txt) 


print("-----------------------------")
## String Method
# Join method
# Join all items in a tuple into a string, using a hash character as separator:
print("Join Method")
myTuple = ("John", "Peter", "Vicky")
x = ",".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
myseprate = "test"
print(myseprate.join(myDict.values()))


# Count method
print('Count Method:')
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

# Find method
print("Find method")
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)
