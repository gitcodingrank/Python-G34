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

student = {
    "name":"Chintu",
    "age":45,
    "city":"Noida",
    "isMarried": True,
    "skills":["HTML", "CSS", "JS"]
}

#Problem 1: given student dictionary, your task is to delete an entry/item where key is age

# del student["age"]
# student.pop("age")

#Problem 2: given student dictionary, your task is to update the name value as "Chunnu"

# #First Way
# student["name"] = "Chunnu"


# #Second Way
# student.update({"name":"Chunnu"})

#Problem: Given below employee dictionary, your task is to get homeAddress city

employee = {
    "name":"Munna",
    "salary":100000,
    "department":"IT",
    "designation":"SDE-1",
    "address":{
        "homeAddress":{
            "city":"Noida",
            "state":"UP"
        },
        "officeAdress":{
            "city":"Agra",
            "state":"UP"
        }
    }
}










