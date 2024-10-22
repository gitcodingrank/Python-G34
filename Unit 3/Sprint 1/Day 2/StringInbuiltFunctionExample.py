# String Inbuilt Functions:
# Capitalize(), count(), endswith, startswith, find, index, isalpha, isnum, isdigit, islower, isnumeric, isupper, lower, max, min, replace, splits with, strip

#lower() - it converts string into lower case.

# str = "CHITKARA"
# print(str.lower()) # chitkara

#upper() - it converts string into upper case.

# str = "chitkara"
# # str1 = str.upper()
# print(str.upper()) # CHITKARA
# print(str) # chitkara

#capitalize() - it converts the first char/letter of string into upper case.

# str = "chitkara university"
# print(str.capitalize())

#title() - it converts each word first letter into capital in the string.

# str = "chitkara university"

# print(str.title())


#startswith(string) - it checks if the original string is starting with given string or not, if yes then it returns True if not then it returns False.


# str = "hello world"
# print(str.startswith("h")) #True
# print(str.startswith("Hello")) #False
# print(str.startswith("hello"))



#endswith(string) - it checks if the original string is ending with given string or not, if yes then it returns True if not then it returns False.


# str = "hello world"
# print(str.endswith("h")) #False
# print(str.endswith("d")) #True
# print(str.endswith("world")) #True
# print(str.endswith("ld")) #True

#Problem Statement: 
# Given list of string, your task is to capital those which are starting with "J"

# langs = ["Java", "Python", "C", "Javascript", "R"]

# #Solution 1:
# for i in range(len(langs)):
#     if langs[i].startswith("J"):
#         langs[i] = langs[i].upper()

# print(langs)

#Solution 2: List Comprehension.

#count(str) - it counts how many time particular char/sequence are there inside original string.

#functionality - it returns the count of specific element if not available then it returns 0 as count.

# str = "helloll"

# print(str.count("l"))
# print(str.count("p"))
# print(str.count("ll"))

#find(string) - it checks particular string is available inside original string or not if not then it returns -1 else it return index


# str = "hello world"

# print(str.find("hello")) #0
# print(str.find("world")) #6
# print(str.find("python")) #-1

#index(string) - it returns the index of particular string in the original string.


# str = "hello world"

# print(str.index("e")) #1
# print(str.index("ll")) #1
# print(str.index("p")) #ValueError - substring is not found.

#split(seperator) - it seperates the string by given seperator and converts into list.

#Note: if you don't define any seperator for spliting then by default the seperator is " "

# langs = "java python javascript .net"
# print(langs.split()) 

# langs = "java-python-javascript-.Net"
# print(langs.split("-")) 


#Problem: take number input from user by space seperated like below and find out the maximum value in the list.

# input = "12 34 45 23 12"

# inputValue = input("Enter Numbers: ")
# strList = inputValue.split(" ")
# numList = [int(char) for char in strList]

# print(max(numList))

# #shorthand way:

# print(max([int(char) for char in input("Enter Numbers: ").split(" ")]))

# print(max(list(lambda char: int(char), input("Enter Numbers: ").split(" "))))


#strip() - it removes front and back space of the strings.


# str = "    hello     "
# print(str)
# print(str.strip())

#replace - it replaces the some portion of the string with char/sequence.

# str = "hello universe"

# print(str.replace("universe" , "world"))

# print(str.replace("ratan tata" , "world"))


#isalpha() - it checks string is containing only alphabets or not.

# str  = "hello"

# print(str.isalpha()) #True

# str1 = "hello123"

# print(str1.isalpha()) #False


#isnumeric() - it checks if a string is containing only numbers

# str = "1232323"

# print(str.isnumeric()) #True

# str1 = "hello123121"

# print(str1.isnumeric()) #False


#isalnum() - it checks if given string is conatining either alphabets or numbers.

# str = "hello123"

# print(str.isalnum())

# str = "hello"

# print(str.isalnum())

#isupper()

# str = "CHITKARA"

# print(str.isupper()) #True


#python inbuilt function for strings operation:

#max(Iterable)
#min(Iterable)

#Note: in the case, string max() and min() functions compares according to the characters ascii value:

#ascii table reference: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html

# str = "world"

# print(max(str))
# print(min(str))
