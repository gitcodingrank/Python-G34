#Opening and Closing Files
#To open the file - open(filePath, mode)
#Important Modes: r(reading), w(writing), a(appending)
#To Close the file - fileName.close()


#Mode: 'r'(reading mode) - it opens with file only for reading, if the file doesn't exist then it will give error FileNotFoundError.

#Note: it doesn't erase(clear) the file existing data at the time opening.

# file = open('note.txt', 'r')
# #print(file) #<_io.TextIOWrapper name='note.txt' mode='r' encoding='cp1252'>
# #Reading the file - using fileVariableName.read()
# print(file.read())

# #Write the file - using fileVariableName.write('Data')
# file.write("Data is complex") #io.UnsupportedOperation: not writable
# file.close()


#Mode: 'w'(writing mode) - it opens with file only for writing, if the file doesn't exist then it creates the file instead of giving error.

#Note: it erases(clears) the file existing data at the time of opening.

# file = open('data.txt', 'w') - once this file named data.txt was not there then it create this file at time of opening.

# file = open('note.txt', 'w')
# #print(file.read()) #io.UnsupportedOperation: not readable
# file.write("Hello World")
# file.close()


#Mode: 'a'(appending/merging mode mode) - it opens with file only for appending(adding the data to existing file), if the file doesn't exist then it creates the file instead of giving error.

#Note: it doesn't erase(clear) the file existing data at the time of opening.

# file = open('note.txt', 'a')
#print(file.read()) #io.UnsupportedOperation: not readable
# file.write("\nLearning Python From Chitkara")
# file.write("\nDoing Everyday Practice")


#Example: Read File which has below data mentioned below:
"""
note.txt
Hello World
Learning Python From Chitkara
Doing Everyday Practice
"""
#Your task is to read the data line by line

#Solution
#Note: to read the data line by line - fileVariableName.readline()

file = open('note.txt', 'r')
# print(file.readline()) #first line in the file
# print(file.readline()) #second line in the file

# print(file.readline()) #third line in the file

#To read all lines at once:
# print(file.readlines())

# for data in file:
#     print(data)


#Example 2: Given below file with data.
"""
data.txt
Chitkara University
""" 
#Your task is to convert Chitkara with Delhi

# fileReading = open('data.txt', 'r')
# data = fileReading.read()
# print(data)
# replacedData = data.replace("Chitkara", "Delhi")
# print(replacedData)
# fileReading.close()


# fileWriting = open('data.txt', 'w')
# fileWriting.write(replacedData)
#fileWriting.close()


#Example 2: Given below file with data.
"""
data.txt
I am learning Java From Chitkara University
Java is easy to learn
""" 
#Your task is to replace Java with Python







