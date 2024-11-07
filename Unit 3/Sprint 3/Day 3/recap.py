#Any Doubt in ST-2 Syllabus and in 

#String Contest Problems Discusion:

#Even Length String: abcxyz
#Odd Length String: abcdxyz

"""
even string = abcxyz = length 6//2 = 3
firstString = string[:3:]
secondString = string[3::]
print(fistString[::-1]+secondString[::-1])


odd string = abcdxyz = length 6//2 = 3
firstString = abc
left - d - position - 3
secondString = xyz
print(fistString[::-1]+ string[3] +secondString[::-1])

"""


#How to convert a string to list using inbuilt function? - split() 

# str  = "apple"

# strList = str.split(" ")
# print(strList)

# strList.append("banana")

# #How to convert a list to string using inbuilt function? - join()

# newString = "".join(strList)
# print(newString)


#Problem 1: Given list of student dictionary:


studentList = [
    {
        "name":"Pawan",
        "age":23,
        "city":"Noida",
        "university":"Chitkara University"
    },
    {
        "name":"Sunil",
        "age":22,
        "city":"Delhi",
        "university":"Chandigarh University"
    },
    {
        "name":"Chintu",
        "age":24,
        "city":"Delhi",
        "university":"Delhi University"
    },
    {
        "name":"Rohan",
        "age":22,
        "city":"Gurugram",
        "university":"Delhi University"
    },
    {
        "name":"Sita",
        "age":20,
        "city":"Noida",
        "university":"Sharda University"
    },
    {
        "name":"Prince",
        "age":12,
        "city":"Haryana",
        "university":"Amity University"
    },
    ]

# for item in studentList:
#     if item["university"]=="Delhi University":
#         print(item["name"])

# for item in studentList:
#     if item["city"]=="Noida":
#         print(item["name"])

# studentFromNoida = list(filter(lambda student: student["city"]=="Noida",studentList))

# print(studentFromNoida)


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]