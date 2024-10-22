# #String: it is collection/sequence of characters(letters + numbers + special symbols) enclosed with single, double, and triple quotation mark.

# #Examples:
# studentName = "Rakesh"
# favoriteLetter = 'a'
# accountNumber = "1232323232"
# ifscCode = "BOB3423D"
# panCardNumber = "ATFSH2312H"
# adhaarCardNumber = "2932938983"
# mobileNumber = "9888232823"
# password = "rakesh@12312"
# pincode = "201301"
# msg = "Hi, I'm rakesh from Patna, and learning about Python in Chitkara University."

# #Point 2: Like list, string also follows 0 based indexing, meaning that first letter is at index 0, second is at index 1 and so on.

# str = "Chitkara"

# # print(str)
# # print(str[0])
# # print(str[3])

# #Check numbers of characters in string - using len(iterable)
# print(len(str))

# #Print characters using loop:

# #1st way:

# for char in str:
#     print(char, end=" ")


# print()

# #1st way:

# for i in range(len(str)):
#     print(str[i], end=" ")


#Example 1 : Given below string check how many vowels are there in the below string.

# #1st Way
# str = "apple"
# vowels = "aeiou"
# count = 0
# for char in str:
#     if char in vowels:
#         count+=1

# print(f"Vowels in {str} are {count}")

# #2nd Way

# # result = sum([1 for char in str if char in vowels])
# # print(result)

# # print(sum([1 for char in str if char in vowels]))


# #Point 3: 
# # String is immutable(unchangable) where as list is mutable(changable).
# #Other Words, once you've declared a string then you can not change/modify/update it as it is immutable(unchangable).
# #Note: But you can replace/reassign the value of string.


# #Exampels:


# #List: mutable(changable)
# # nums = [1,2,3,4,5,6]

# # nums[1] = 10 #modified the existing element of nums list at index 1

# # print(nums)

# # #String: immutable(unchangable)
# # password = "rekesh@123"

# # # password[0] = "m" #Trying to modify the char of the password string at index 0 which is not possible as string is immutable.

# # password = "mekesh@123" #replacement/reassignment - which is possible

# # print(password)


# #Example 1: Given below string your task is to change the first character with M

# # str = "Rupesh"

# # strList = [char for char in str]

# #1st Way:
# # strList = []

# # for char in str:
# #     strList.append(char)

# # print(strList)

# # strList[0] = "M"
# # print(strList)

# # udpatedStr = ""
# # for ele in strList:
# #     udpatedStr+=ele

# # print(udpatedStr)

# #2nd Way:
# #str = "Rupesh"
# # updatedStr = "M" + str[1:]
# # print(updatedStr) #Mupesh


# #Example 2: Given a string in small case your task is to convert into capital case without using inbuilt function.

# name = "chitkara"

# def myUpper(str):
#     smallCaseLetter = "abcdefghijklmnopqrstuvwxyz"
#     capitalCaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# #     updatedString = ""

# #     for char in str:
# #         for i in range(len(smallCaseLetter)):
# #             if char == smallCaseLetter[i]:
# #                 updatedString+= capitalCaseLetter[i]
# #     return updatedString
            

# # print(myUpper("chitkara"))
# # print(myUpper("apple"))


# # #Example 3: Given list of string, your task is to capital those which are starting with "j"

# # langs = ["java", "Python", "c", "javascript", "r"]

# # for i in range(len(langs)):
# #     name = langs[i]
# #     if name[0]=="j":
# #         langs[i] = myUpper(langs[i])
    
# # print(langs)


# #string slicing - extacting the some portion from the original string, and it is always in continuous manner.

# """
# sytax:

# [startPoint:endPoint:step] #ByDefault - startPoint - 0, endPoint - end of given String, step: 1

# stringVariableName[:] - startPoint - 0, endPoint - end of given String, step: 1

# stringVariableName[1:10:2] - startingPoint - 1, endPoint <10, step - 2 at a time.

# """


# # str = "chitkara"

# # print(str[:])
# # print(str[:4])
# # print(str[::2])
# # print(str[2:])
# # print(str[::-1])
# # print(str[:-4:-1])

# #Example: given a string below, check that string is palindrome or not.

# str1 = "madam" #Palindrome
# str2 = "car" #Not Palindrome

# str1ReverseForm = ""
# for i in range(len(str1)-1,-1,-1):
#     str1ReverseForm+=str1[i]

# if str1 == str1ReverseForm:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# print("-------------------------------------")

# #Shorthand way:
# print("Palindrome" if str1==str1[::-1] else "Not Palindrome")