#Conditional Statement: Why are we learning?
#Reason: So that on the basis of particular condition you can provide meaningful statement/msg to the user/customer.

#How to create condition? - Using Comparison Operator
#Examples:

#Create condition to check age is greater or eqault to 18
# age = 19
# print(age >= 18) #True

# #Create conditon to check number is even or odd
# num = 45
# print(num%2==0) #False


#In the case of Comparison opeartor, it always returns Boolean value that is 110% understandable by developer and your python but your cusotmer/user doesn't understand it.

#There are following types of conditional statement in python:
#1. if statement
#2. if else statement
#3. if elif else statement


#1. if statement: if the given the condition is true then the code/statement inside if block will execute and if the condition is false then the code/statement inside if block will not execute.

"""
syntax:

if condition:
    print("If condition is true")

"""

#Note: Python is indendation oriented programming language therefore for particular concept like conditional statements, loop, functions and other important concepts you need to use proper indendation.

#Example 1: Check a number is negative or positive

# num = 56

# #conditionToCheckNegativeNumber = num < 0
# # print(conditionToCheckNegativeNumber) #False
# #if statement

# if num < 0:
#     print("Starting of if block")
#     print("Number is negative")
#     print("Ending of if block")
    
# print("Out side the if block")


#Example 2: create a condition to check person is eligible for voting or not.

# age = 19

# # if False:
# #     print("Eligible for voting") #unreachable code

# if age >= 18:
#     print("Eligible for voting.")

#Example 3: create a problem to check username is correct or not.

# username = input("Enter Username: ")

# if username =="admin":
#     print("Logged in Successfully.")


#Limitation of if statement: it always run the code inside if block if the condition is true it never runs anything if the condition is false, in this way it can hamper the user experience.


#if you want to give msg on false condition then if statement is not the best choice then what is the best choice: if else statement.

#2. if else statement: if the given the condition is true then the code inside if block will execute and if the condition is false then code inside else block will execute.

"""
syntax:

if condition:
    print("If condition is true")
else:
    print("If the condition is false")

"""

#Example 1: check a number is even or odd

# num = int(input("Enter Number: "))

# if num%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")

#Example 2: check any person username to login and give proper msg on invalid username

# username = input("Enter Username: ")

# if username == "admin":
#     print("Logged in successfully.")
# else:
#     print("Invalid Username")

#Exmaple: check a number is negative, positive or zero.

#Limitation if else statement: if else statement is the best choice if you've only one condition.
#because in the case of more conditions, you need create nested else if statement

#Exmaple: check a number is negative, positive or zero.
#using if statement:

num = 56
if num == 0:
    print("Number is zero.")
else:
    if num > 0:
        print("Number is positive.")
    else:
        print("Number is negative.")


#Example 2: print dayName on the basis of dayNumber where day 1 is as Monday.
#Conditions to print correct dayname: 7

# dayNumber = int(input("Enter Day Number: "))

# if dayNumber==1:
#     print("Monday")
# else:
#     if dayNumber ==2:
#         print("Tuesday")
#     else:
#         if dayNumber ==3:
#             print("Wednesday")
#         else:
#             if dayNumber ==4:
#                 print("Thursday")
#             else:
#                 if dayNumber ==5:
#                     print("Friday")
#                 else: 
#                     if dayNumber ==6:
#                         print("Saturday")
#                     else:
#                         if dayNumber==7:
#                             print("Sunday")
#                         else:
#                             print("Invalid Day Number")

#According to abvoe problem, if you will solve using if else statement it will make your code less readable and harder to mantain then what is the solution to create more readable and easy to maintain code.

#3. if elif else statement: if you've more than one independent conditions then you can proceed with if elif statement.
# among many conditions if any of the condition is true then code inside particular block will execute otherwise code insde else block will execute. 

"""
syntax:

if condition1:
    print("If condition1 is true")
elif condition2:
    print("If condition2 is true")
elif condition2:
    print("If condition3 is true")
elif condition3:
    print("If condition4 is true")
elif condition4:
    print("If condition5 is true")
elif condition5:
    print("If condition6 is true")
else:
    print("if any of the codition is not true")

"""


#Example: print dayName with the help of dayNumber where dayNumber 1 as Monday

dayNumber = int(input("Enter Day Number: "))

if dayNumber ==1:
    print("Monday")
elif dayNumber == 2:
    print("Tuesday")
elif dayNumber == 3:
    print("Wednesday")
elif dayNumber == 4:
    print("Thursday")
elif dayNumber == 5:
    print("Friday")
elif dayNumber == 6:
    print("Saturday")
elif dayNumber == 7:
    print("Sunday")
else:
    print("Invalid Day Number")


