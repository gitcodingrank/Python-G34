#Lambda Function: It is an annoymous funciton(a function without name) which is used to write the function in short and concise manner.

"""
syntax:
variableName = lambda parameters : exprssion/body

#Normal Function

def welcome(name)
    print(f"Welcome {name}")

welcome("Rakesh")

#Convert above function to lambda function
welcomeFunc = lambda name : print(f"Welcome {name}")
welcomeFunc("Rakesh")

"""

#Example 1:
#Normal Function

# def welcome(name):
#     print(f"Welcome {name}")

# welcome("Rakesh")

# #Convert above function to lambda function

# welcomeFunc = lambda name : print(f"Welcome {name}")
# welcomeFunc("Rakesh")

# #Example 2:

# def add(a,b):
#     return a+b

# print(add(2,3))

# #Convert to lambda funciton
# addFun = lambda a,b: a+b
# print(addFun(2,3))

# #Example 3:

# def findEvenList(nums):
#     evenList = []
#     for i in nums:
#         if i%2==0:
#             evenList.append(i)
#     return evenList

# print(findEvenList([1,2,3,4,5,6,7,8,9,10]))

# #Let's convert above function into lambda function

# findEvenListFun = lambda nums : [x for x in nums if x%2==0]

# print(findEvenListFun([1,2,3,4,5,6,7,8,9,10]))


"""
Conclusion about Lambda Funciton:
1. It is single line function meaning that it supports single line the body.
2. for printing any expression, you don't need to write return keyword
3. for taking many paramerters, you can define parameters comma seperated.
"""

#Example 1: check a number is even or odd using lambda function.

# isEven = lambda num: num%2==0
# print(isEven(20))
# print(isEven(21))

# isEven = lambda num: "Even" if num%2==0 else "Odd"
# print(isEven(20))
# print(isEven(21))

#Example 2: print even number in one line from 1 to 10