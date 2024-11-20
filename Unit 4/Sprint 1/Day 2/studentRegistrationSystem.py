import uuid
import json

def addStudentToFile(student):
    with open('students.json', 'r+') as file:
        studentData = json.loads(file.read())

        studentData["students"].append(student)
        print(studentData)
        file.seek(0)
        file.write(json.dumps(studentData))
        file.truncate()

def getStudentsFromFile():
    with open('students.json', 'r') as file:
        studentData = json.loads(file.read())
        return studentData["students"]


def menu():
    print("1. Add Student")
    print("2. Get Students By Id")
    print("3. Get All Students")
    print("4. Update Student By Id")
    print("5. Delete Students By Id")
    print("6. Exit")

def addStudent():
    student = {}
    student["id"] = str(uuid.uuid4().int)[:15:]
    student["name"] = input("Enter Student Name: ")
    student["city"] = input("Enter Student City: ")
    student["marks"] = input("Enter Student Marks: ")
    addStudentToFile(student)
    print("Student has registered successfully.")

def getStudentById():
    pass

def getAllStudents():
    for student in getStudentsFromFile():
        print("======================================")
        print(f"Student Id: {student["id"]}")
        print(f"Student Name: {student["name"]}")
        print(f"Student City: {student["city"]}")
        print(f"Student Marks: {student["marks"]}")
        print("======================================")

def updateStudentById():
    pass

def deleteStudentById():
    pass

while True:
    menu()
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        addStudent()
    elif choice == 2:
        getStudentById()
    elif choice == 3:
        getAllStudents()
    elif choice == 4:
        updateStudentById()
    elif choice == 5:
        deleteStudentById()
    elif choice == 6:
        res = input("Do you want to exit(n/y): ")
        if res in ["y", "Y"]:
            print("Thank you using my application.")
            break
    else:
        print("Invalid Choice, Please Try Again.")