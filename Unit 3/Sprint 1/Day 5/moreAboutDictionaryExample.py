#Dictionary: It is a data structure which is use to store the data in the form key-value pair.

#Note: key-value pair is also known as one item/entry in the dictionary. 

#Importnat Points
# 1. Unordered.
# 2. Mutable
# 3. Accessing through Keys
# 4. Keys are unique whereas values can be duplicate.
# 5. Keyas are always of string type whereas values can be any type.


#Declaration of Dictionary

#student = {}
# student = dict() 

# print(student)
# print("Empty Dictionary" if len(student)==0 else "Not Empty")


# student = {
#     "name":"Pawan",
#     "marks":450,
#     "city":"Noida",
#     "skills":["HTML", "CSS", "JS"],
#     "subjects":("Maths", "Science", "English", "Computer"),
#     "isMarried":False

# }

# print(student)


#How to add item/entry to the dictionary.

# student = {}

# #1. dictionaryName["keyName"] = value

# student["name"] = "Pawan" #additing one item where key is name and value is pawan
# student["city"] = "Noida" #additing one item where key is city and value is Noida
# student["age"] = 23 #additing one item where key is age and value is 23


# print(student)


# employee = {}

#1. dictionaryName['KeyName'] = value

# employee["name"] = "Rakesh"
# employee["salary"] = 45000
# employee["city"] = "Delhi"

# print(employee)

#2. using update({})

#to add/update multiple entries/items to the dictionary
#sytnax = dictionaryName.update({})

# employee.update({'name':"Rakesh", "city":"Noida", "salary":50000})

# print(employee)


#how to access the value? - using keyName

student = {
    "name":"Pawan",
    "marks":450,
    "city":"Noida",
    "skills":["HTML", "CSS", "JS"],
    "subjects":("Maths", "Science", "English", "Computer"),
    "isMarried":False

}

#sytanx = dictionaryName['keyName']
# print(student['name'])
# print(student['city'])
# print(student['skills'][1])

#above student is skilled in html or not.

# if "HTML" in student['skills']:
#     print("Yes, he is skilled")
# else:
#     print("Yes, he is not skilled")


# if key doesn't exist

# print(student['age']) #KeyError: 'age'

#dictionaryName.get('keyName', None) - it doesn't give any error if the key is not available inside dictionary instead it gives default value as None that you can change.


# print(student.get('age'))
# print(student.get('age', "Key is not available inside dictionary"))


#how to update the value of dictionary? - using keyName


#1. dictionaryName['keyName'] = value

#updating value Pankaj for key name
# student['name'] = "Pankaj"
# student['city'] = "Patna"

# print(student)

#2. to update multiple entries/items - using update({})

# student.update({'name':"Chintu", "city":"Haryana"})

# print(student)


