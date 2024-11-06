#how to delete/remove an entry/item from the dictionary?

#Initialization at the time of declaration
# student = {
#     "name":"Chintu",
#     "age":45,
#     "city":"Noida",
#     "isMarried": True,
#     "skills":["HTML", "CSS", "JS"]
# }

#Delete Entry using del keyword
#Syntax - del dictionaryName[keyName]

# print(student)

# del student["age"]

# print(student)

# del student["age"] #KeyError: 'age'

#using pop('keyName', defaultValue)

#syntax - dictionaryName.pop(keyName, defaultValue) #if you're not mentioned the default value and entry is also not available with given key then default value is None(Nothing, absence of value, Null)

#Note: it returns the value of given key

# print(student)

# removedAgeKeyValue = student.pop("age")

# print(removedAgeKeyValue)

# print(student)


# removedAgeKeyValue = student.pop("age", None)

# removedAgeKeyValue = student.pop("age", "It is no more part of student dictionary")

# print(removedAgeKeyValue)


#using popItem()

#Syntax - dictionaryNmae.popItem() - it deletes the most recent added entry to the dictionary and returns it.

# mostRecentAddedEntry = student.popitem()

# print(mostRecentAddedEntry)

# print(student)

#Inbuilt function of dictionary:

# student = {
#     "name":"Chintu",
#     "age":45,
#     "city":"Noida",
#     "isMarried": True,
#     "skills":["HTML", "CSS", "JS"]
# }

#keys() 
#syntax - dictionaryName.keys()

# print(student.keys())

# studentKeys = student.keys()

# print(studentKeys[0]) #TypeError: 'dict_keys' object is not subscriptable

# studentKeys = list(student.keys())

# print(studentKeys[0])

# for key in student.keys():
#     print(key, end=" ")


#values()

# print(student.values()[0]) #TypeError: 'dict_values' object is not subscriptable

# studentValues = list(student.values())

# print(studentValues[0])


# for value in student.values():
#     print(value, end=" ")


#items() - return list of tuples where each tuple is item(key, value)

# print(student.items())

# studentItems = list(student.items
# ())

# # print(studentItems[0][0])

# key, value = studentItems[0] # ('name', 45)

# print(key, value)

# print(list(student.items()))

# [('name', 'Chintu'), ('age', 45), ('city', 'Noida'), ('isMarried', True), ('skills', ['HTML', 'CSS', 'JS'])]

# for chintu, babita in student.items():
#     print(chintu, babita)

# student = {
#     "name":"Chintu",
#     "age":45,
#     "city":"Noida",
#     "isMarried": True,
#     "skills":["HTML", "CSS", "JS"]
# }

#Problem 1: given student dictionary, your task is to delete an entry/item where key is age

# del student["age"]
# student.pop("age")

#Problem 2: given student dictionary, your task is to update the name value as "Chunnu"

# #First Way
# student["name"] = "Chunnu"


# #Second Way
# student.update({"name":"Chunnu"})

#Problem: Given below employee dictionary, your task is to get homeAddress city
# employee = {
#     "name":"Munna",
#     "salary":100000,
#     "department":"IT",
#     "designation":"SDE-1",
#     "address":{
#         "homeAddress":{
#             "city":"Noida",
#             "state":"UP"
#         },
#         "officeAdress":{
#             "city":"Agra",
#             "state":"UP"
#         }
#     }
# }


# print(employee["address"]["homeAddress"]["city"])


#Problem 1: Guess the output for the following statement:

# student = {
#     "studentName":"Madan",
#     "studentAge":23,
#     "isMarried":False,
#     "Skills":["HTML", "CSS", "JS"]
# }

#print(student["city"])#KeyError: 'city'

# print(student.get("city", None))

# print(student.get("city", "Entry is not found with this key"))

# nums = {}

# nums[1] = 1

#nums = {'1':1}

# print(nums.get(1)) #1
# print(nums.get(2)) #None
# print(nums.get(2,0)) #0

# nums[2] = 1

# #nums = '1':1, '2':1}

# print(nums)

# print(type(list(nums.keys())[0]))

# if 2 in nums:
#     print("Found")
# else:
#     print("Not Found")

#Problem: Given a string, your task is to find out the count of vowels and consonants in the following format.

#input - str = "apple"
#output= {'vowels':2, 'consonants':3}

#Solution 1:

# str = "apple"

# vowels = 0
# consonants = 0

# for char in str:
#     if char in "aeiou":
#         vowels+=1
#     else:
#         consonants+=1

# print({"vowels":vowels, "consonants":consonants})

# #Solution 2:

# vowels = sum([1 for char in str if char in "aeiou"])
# consonants = sum([1 for char in str if char not in "aeiou"])

# print({"vowels":vowels, "consonants":consonants})


#Problem 2 : Given a string below, your task is to find out the freequency of character.

#input - str = "apple"
#output - {'a':1, 'p':2, 'l':1, 'e':1}

#Solution 1:
# str = "apple"
# charFrequency = {}

# for char in str:
#     if char in charFrequency:
#         charFrequency[char]= charFrequency[char] + 1 
#     else:
#         charFrequency[char]=1

#Solution 2:

# str = "apple"
# charFrequency = {}

# for char in str:
#     charFrequency[char]= charFrequency.get(char, 0) + 1 


# #Solution 3:

# result = {char: str.count(char) for char in set(str)}

#Problem: given a number list, your task is to find out the frequency of number.

# nums = [1,2,3,2,3,2,1,3,1,2,3,2,1,4]

# dict = {}

# for num in nums:
#     dict[num] = dict.get(num, 0) + 1


#Problem: Given a string, your task is to find out the frequency of word.

# str = "hello hello world hello hi hi bye"
# strList = str.split()
# #print(strList) #['hello', 'hello', 'world','hello', 'hi', 'hi', 'bye']

# charFrequency = {}

# for word in strList:
#     charFrequency[word]= charFrequency.get(word, 0) + 1 

#JSON and its relation with python dictionary.

#JSON: it stands for Javascript Object Notation which is light weight data interchange format and it is easy for humans to read and write, and machine to parse and generate.


#data exchange

"""

Client Side(Frontent)
           Request       |
   --------------------> |  JSON
           Response      |
   <-------------------   
                         Server Side(Backend)

"""

#Syntax of json - it is 100% similar to python dictionary

#Python Dictionary
# studentDict = {
#     "name":"Pawan",
#     "age":23,
#     "city":"Noida"
# }

#Note: json is a textual/string type data.

#Python Dictionary
# studentJson = '{"name":"Pawan","age":23,"city":"Noida"}'

# print(type(studentDict))
# print(type(studentJson))

#How to convert dictionary to json? 

employee = {
    "name":"Pawan",
    "age":23,
    "city":"Noida"
}

import json

employeeJson = json.dumps(employee)
print(employeeJson)

print(type(employeeJson))

#Convet json into python dictionary

employeeDict = json.loads(employeeJson)

print(employeeDict)
print(type(employeeDict))



