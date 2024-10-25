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

student = {}

#1. dictionaryName["keyName"] = value

student["name"] = "Pawan" #additing one item where key is name and value is pawan

student["city"] = "Noida" #additing one item where key is city and value is Noida

student["age"] = 23 #additing one item where key is age and value is 23

print(student)

