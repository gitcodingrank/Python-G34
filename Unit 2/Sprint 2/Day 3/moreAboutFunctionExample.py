"""
There are two types of function in python:
1. User Defined/Custom Function: You can create function according to your requirement.
2. Inbuilt/Pre-Defined Function: Some functions are already there in python library rather than creating the sepereate function for the same functionality its better to use them.
"""

#User-Defined Function:
# def findListLength(list):
#     count = 0
#     for i in list:
#         count+=1
#     return count

# print(findListLength([1,2,3,4,5]))
# print(findListLength(["Rakesh", "Deepak", "Sunil", "Pawan"]))

# #Python Inbuilt Function: 
# len(iterable)
# print(len([1,2,3,4,5]))
# print(len(["Rakesh", "Deepak", "Sunil", "Pawan"]))

#sum(iterable): it supports only number type iterable
# print(sum([1,2,3,4,5]))

#id()
# name1 = "Suresh"
# name2 = "Suresh"
# print(id(name1))
# print(id(name2))

# print(abs(-23)) 
# print(abs(-23+10))
# print(abs(-23.45))

#List Methods
#append(), copy(), insert(), remove(element), pop(), pop(index), extend(), reverse(), index(element)

# names = ["Chunnu", "Pintu", "Chintu", "Bablu", "Munnu"]
# names.append("Chaman")
# #print(names)

# #insert(index, data)

# names.insert(1, "Rinku")
# print(names)

# #remove(element): it removes particular element from the list.
# # names.remove("Rinku")
# # print(names)

# #pop(): it removes the element at the end of the list and returns that removed element.

# removedElement = names.pop()
# #print(removedElement)
# print(names) #['Chunnu', 'Rinku', 'Pintu', 'Chintu', 'Bablu', 'Munnu']

# #pop(index): it removes particular element from specific index and returns that removed element:
# removedElement = names.pop(2)
# print(removedElement)
# print(names) #['Chunnu', 'Rinku', 'Chintu', 'Bablu', 'Munnu']

# #extends(): it extends the particular list- it merges the elements from another list.
# engineersNames = ["Rakesh", "Suresh"]
# names.extend(engineersNames)
# print(names) #['Chunnu', 'Rinku', 'Chintu', 'Bablu', 'Munnu', 'Rakesh', 'Suresh']

# names.reverse()
# print(names) #['Suresh', 'Rakesh', 'Munnu', 'Bablu', 'Chintu', 'Rinku', 'Chunnu']

# #count(element): it returns the count of occurance for particular element in the list.
# names.append("Rakesh")
# print(names.count("Rakesh")) 

# #index(element): it returns the index for particular element in the list.\\

# print(names.index("Suresh"))


#Other Methods:

import math

# print(math.factorial(5)) #120

# print(math.ceil(4.5)) #5
# print(math.ceil(4.4)) #5
# print(math.ceil(4.7)) #5
# print(math.ceil(4.2)) #5

# print(math.floor(4.5)) #4
# print(math.floor(4.4)) #4
# print(math.floor(4.7)) #4
# print(math.floor(4.2)) #4

# print(math.gcd(2,10))
# print(math.lcm(2,10))
#2 - 2*1
#10 - 5*2*1

import random

# print(random.random()) # generates randome number between 0 and 1

#fix the range for generating random number
# print(random.randint(1, 20))


#random method for list.
# print(random.choice(["Apple", "Banana", "Mango", "Grapes"]))

# fruits = ["Apple", "Banana", "Mango", "Grapes"]
# random.shuffle(fruits)

# print(fruits)
