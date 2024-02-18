list1 = ["abc", 34, True, 40, "male"]
print(list1)

# indexing and slicing
print(list1[0:])
print(list1[0:7:2])
print(list1[::-2])
print(list1[6:1:-2])
print(list1[-5:-2:1])
print(list1[-1:-6:-3])

# change items
lst = ["nandu","shyam","mohan",88,44]
lst[1] = "ram"
print(lst)
lst[1:3] = ["mohan","yash"]
print(lst)
lst[1:3] = ["ankit"]
print(lst)


## Method
# append method
lst.append("lokesh")  
print(lst)
lst.append(44)

# insert method
lst.insert(1,"anku")
print(lst)

#extend method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# tuple extend
thistuple = ("kiwi", "orange")
lst.extend(thistuple)
print(lst)

# remove method
lst.remove("orange")
print(lst)

# pop method
lst.pop()
print(lst)
lst.pop(0)   # remove by index value
print(lst)

# del method

del lst[1]
print(lst)

# clear method for clear list
lst.clear()
print(lst)

# list comperehenson
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


## sort list
# string list sorted
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)    # ascending order
thislist.sort(reverse=True)
print(thislist) # descending order

print(sorted(thislist))

# sort numeric list
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)
print(thislist)

# You can also customize your own function by using the keyword argument key = function.

def myfunc(n):
  return abs(n - 90)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

list1 = ["ran","Yash",88,4]
#list1.sort()   # int and str items not sorted
print(list1)

# copy method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "orange", "cherry"]
mylist = list(thislist)
print(mylist)

# join method

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3,4,7]

list1.extend(list2)
print(list1)