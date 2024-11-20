#Till now, you all know, how to open file with modes - r, w, and a
#you all know about closing of file.


#Assignment Problems:
#Problem 1: 

# list = ["Chaman", "Pawan", "Rohan", "Chunnu", "Munnu"]

# writeFile = open('students.txt', 'w')
# for i in range(len(list)):
#     if i==0:
#         writeFile.write(list[i])
#     else:
#         writeFile.write("\n"+list[i])
# writeFile.close()

# readFile = open('students.txt', 'r')
# for name in readFile:
#     print(name.strip())

# while True:
#     line = readFile.readline()
#     if not line:
#         break
#     print(line.strip())

# allLines = readFile.readlines()
# print(len(allLines))
#readFile.close()

# wordList = readFile.read().splitlines()
# print(wordList)

# #Freequency: 
# print({word:wordList.count(word) for word in set(wordList)})


#Cursor Positioning in File:
#tell() - tells the position of cursor
#seek(n) - it changes the cursor position

#Note: on writing and reading your cursor postion gets changed.

# file = open('data.txt', 'r')
# print(file.tell())#0
# print(file.read())#Students are okay
# print(file.tell())#17
# print(file.read())
# file.seek(0)
# print(file.tell())#0
# print(file.read())
# print(file.tell())
# file.close()

# file = open('data.txt', 'a')
# print(file.tell())
# file.seek(0)
# file.write("Chitkara")

#Advance Modes: 'r+' - opened the file for both reading and writing, and if file doesn't exist then it gives error: FileNotFoundError

#Note: it doesn't truncate(clear) the file data on opening the file.
#Note: in this case cursor points in the beginning of file.

# file = open('data.txt', 'r+')
# print(file.tell())#0
# print(file.read())#readig 
# print(file.tell())
# file.write("Chitkara")#writing
# file.seek(0)
# file.write("Chaman")
# print(file.tell())
# file.truncate()
#file.close()


#Advance Modes: 'w+' - opened the file for both reading and writing, and if file doesn't exist then it creates the file

#Note: it truncates(clears) the file data on opening the file.
#Note: in this case cursor points in the beginning of file.

# file = open('data.txt', 'w+')
# print(file.tell())#0
# file.write("Hello Everyone")
# print(file.tell())#14
# print(file.read())
# file.seek(0)
# print(file.read())
#file.close()


#Advance Modes: 'a+' - opened the file for both reading and writing, and if file doesn't exist then it creates the file

#Note: it doesn't truncate(clear) the file data on opening the file.
#Note: in this case cursor points at end of file.

# file = open('data.txt', 'a+')
# print(file.tell())#14
# print(file.read())
# file.seek(0)
# print(file.read())
# print(file.tell())
# file.seek(0)
# file.write('Something Went Wrong')


#Examples: Add list of students to students.txt file and add one more student to it.

import json

students = ["Chaman", "Rohan", "Sunil", "Pankaj"]

file = open('data.txt', 'r+')
#file.write(students) #TypeError: write() argument must be str, not list

#Wthout JSON
# file.write(" ".join(students))
# file.truncate()
# studentStr = file.read()
# studentsList = studentStr.split()
# studentsList.append("Chinki")
# # print(studentsList)

# file.seek(0)
# file.write(" ".join(studentsList))
# file.truncate()

#With the help of JSON
# file.write(json.dumps(students))

#add another sutdents
# studentList = json.loads(file.read())
# studentList.append("Chinki")
# file.seek(0)
# file.write(json.dumps(studentList))
# file.truncate()


    