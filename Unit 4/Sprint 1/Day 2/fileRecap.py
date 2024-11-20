#What are the important step in every mode? - file opening and closing

# file = open('students.json', 'r')
# print(file.read())
# file.close()


# #modern way to open the file and in this way python automatically close the file if it is no longer needed.

# with open('students.json', 'r+') as file:
#     print(file.read())
#     file.write("Hello Everyone")


#Good Example: given students.json file, your task is to read and write the data.
import json

def addStudent(student):
    with open('students.json', 'r+') as file:
        studentData = json.loads(file.read())

        studentData["students"].append(student)
        print(studentData)
        file.seek(0)
        file.write(json.dumps(studentData))
        file.truncate()

addStudent({"name":"Chaman", "age":34, "city":"Delhi"})
