#Recursion: It is just a technique which is used to break down complex problem into smaller sub-problems.and


#To Use Recursion in your code, you need to understand about two imporant parts of Recursion:
#1. Recursive Function: It is like a function which call itself during the its execution, if your function keeps on calling itself again and again then it will end up with infinite call.
#2. Base Condition: It is used to stop/termiate the recursive function

"""
syntax:

#declartion of function
def add():
    if baseCondition:
        #stop
    add()


#calling the function
add()
"""

#Example 1: Find out the factorial of given number.

#Using Tranditional Approach
# num = 5
# fact = 1

# for i in range(1, num+1):
#     fact*=i
# print(fact)

#Recursive Approach - using Recursion

# def factorial(num):
#     if num==1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(10)) 

#Example 2: Define a function sum_of_natural_numbers(n) that returns the sum of the first n natural numbers.

#Without Recursion

# def sumOfNaturalNumber(nums):
#     sum = 0
#     for i in range(1, nums+1):
#         sum+=i
#     return sum

# print(sumOfNaturalNumber(10))

#Recusrion?

# def sum_of_n_natural_numbers(n):
#     if n==1:
#         return 1
#     return n + sum_of_n_natural_numbers(n-1)

# print(sum_of_n_natural_numbers(10))


#Example 3: Print list of numbers using recursion
names = ["Rakesh", "Deepak", "Suresh", "Pankaj", "Rishi", "Rohan"]

def printListElement(nameList, index):
    if index >= len(nameList):
        return
    # print(nameList[index])
    yield nameList[index]
    printListElement(nameList, index+1)

for i in printListElement(names, 0):
    print(i, end=" ")


"""
Task 6:
Write a recursive function that takes a string and returns its reverse.

Task 7:
Count the Number of Digits in a Number

Task 8:
Sum of Digits of a Number
"""
