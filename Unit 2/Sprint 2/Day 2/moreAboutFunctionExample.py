#Passing Arguments

#Example 1: Create a function that take two parameters of number type and print the diffrerence of those number.

# def findDifference(num1,num2):
#     print(num1-num2)


# #Positional Arguments
# findDifference(34, 20) 
# findDifference(56, 78,78) #TypeError: findDifference() takes 2 positional arguments but 3 were given


#Example 2: Create a function that accept a list of numbers and find out the sum of all the numbers


# def sumOfNumberListElement(numList):
#     sum = 0
#     for i in numList:
#         sum+=i
#     print(f"Sum of Numbers - {sum}")


# #Arguments
# numList = [1,2,3,4,5,6,7,8,9,10]
# sumOfNumberListElement(numList) #First Call with [1,2,3,4,5,6,7,8,9,10] arguments

# sumOfNumberListElement([45, -45, -3])  # Second Call with [45, -45, -3] arguments

#Student Task:

# def anyFun():
#     print("Nothing is here")

# anyFun()


# def printABoutYou(name="No Name Found", age="Not yet born", city="No City Found"):
#     print(f"Your Name {name}")
#     print(f"Your Age {age}")
#     print(f"Your City {city}")


# #Default Arguments
# printABoutYou("Rakesh", 45, "Noida")
# print("-------------------------------")
# printABoutYou("Rakesh", 45)
# print("-------------------------------")
# printABoutYou()


# def printABoutYou(name, age):
#     print(f"Your Name {name}")
#     print(f"Your Age {age}")

# printABoutYou("Rakesh", 56)
# print("------------------------------------")
# # printABoutYou(56, "Rakesh")
# #Solution for second call
# #Keyword Arguments
# printABoutYou(age = 56, name = "Rakesh")


#Arbitrary Arguments: *varible_name - it returns tuple
#sum(iterator) - iterator - list/tuple

# def findSum(a,b,c,d,e,f,g,h,i):
#     print(a+b+c+d+e+f+g+h+i)

# findSum(1,2,3,4,5,6,7,8,9)

#In below both of the case it will give error
# findSum(1,2,3,4,5)
# findSum(1,2,3,4,5,56,34,23,34,5,67,78,89,45,34,23,56)

# def findSum(*numbers):
#     # print(arwt)
#     print(sum(numbers))

# #Arbitrary Arguments:
# findSum(1,2,3,4,5,56,34,23,34,5,67,78,89,45,34,23,56)

"""
Student Tasks:

Task 1:
Write a function introduce_person(name, age, city) that prints a sentence introducing a person.
Call the function using positional arguments and keyword arguments in different orders.

Task 2:

Write a function greet_person(name, greeting="Hello") that prints a greeting.
Call the function with:
Only the name argument.
Both name and greeting arguments.

Task 3:

Write a function sum_numbers(*args) that accepts any number of arguments and returns their sum.
Call the function with different numbers of arguments.

"""


#Note: 

# def isEven(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")

# isEven(45)
# isEven(11)
# isEven(67)
# isEven(34)



#According to above examples, your functions are printing the result immeditely, what if you don't want your function to print result immeditely, you just want your function to return the result so that whenever you need to print/use the result, you can use it.

#How will you do the above facility using function?
#using return keyword

#Note: using return keyword, your function can also return something.

"""
syntax:
return expression
"""

#Example 1: 

# def isEven(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"

# result = isEven(45)
# #           Odd
# print(result)

# print("-------------------")
# print(isEven(56))


#Problem: given below expression, your task is to find out the product of given expression

#exp1 = 45 + 56
#exp2 = 56 - 10

#output = exp1 * exp2

def sum(a,b):
    return a+b

def difference(a,b):
    return a-b

def product(a,b):
    return a*b

exp1 = sum(45, 56)
exp2 = difference(56, 10)
result = product(exp1, exp2)
print(result)

#shorthand way

print(product(sum(45, 56),difference(56, 10)))