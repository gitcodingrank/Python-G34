#Why Loop: 

#If i ask you to print "Hello World" 10 times?
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

#What if i want you to print "Hello World" 1000 times?
#Yes, you can print 1000 times as well but in this way your code will look less readable, lengthy and harder to maintain.
#In this way your code will have duplicacy/Redundancy, which is not recommended as a developer.

#What is the solution: Loop
#Loop: It is an iterative statement which is used to execute/run block of code again and again.

#There are following types of loop in python:
#1. while loop:
#2. for loop:

#1. while loop: it is used to execute/run block of code again and again.
"""
syntax:

startingPoint
while condtion:
    #block of code
    #step: increment/decrement

"""

#Increment/Decrement: it is just a way to increase or decrease the value by some number.
#Note: in python, increment and decrement operator is not supported but you can achieve this facility by using + and - operator.

#Increment: 

# num = 10

#increase the value of num by 1

# num = num + 1
# print(num)

#increase the value of num by 10
# num = num + 10
#  num =  num+ 10
#  variable = value
# print(num) # 21

#Decrease the value of num by 10
# num = num - 10

# print(num) #11

#Example 1: print hello world 10 times.

#Note: loop only keeps on executing lines of code until the condition is true.

# conditon = True

# while conditon:
#     print("Hello World")

#Procee of While loop Execution: check condition(True) --> block of code---> again check condtion(True) --> block of code--->check condtion(False)--->come out of the loop.

#According to above condition, you while loop has become infinite loop as the condition is never gonna False.
#What if we want to execute while for specific rounds, then need to take care about following part of loop:

#1. startingPoint
#2. where to stop (condition)
#3. step

# #Example 1: print hello world 5 times.
# sp = 1
# #condition = sp <= 5
# while sp <= 5:
#     print("Hello World")
#     sp = sp + 1

#Visualization/Dry Run for above loop
"""


Given: sp = 1
Round 1: sp <= 5: True
           print "Hello World"
           sp = 1 + 1 => 2 
           sp = 2
Round 2: sp <= 5: True
           print "Hello World"
           sp = 2+1 => 3
           sp = 3
Round 3:  sp <= 5: True
           print "Hello World"
           sp = 3+1 => 4
           sp = 4
Round 4:  sp <= 5: True
           print "Hello World"
           sp = 4+1 => 5
           sp = 5
Round 5:  sp <= 5: True
           print "Hello World"
           sp = 5+1 => 6
           sp = 6
Round 6:  sp <= 5: False -> Come out of the loop

"""

#Example 2: print number from 1 to 10.
# sp = 1

# while sp <= 10:
#     print(sp)
#     sp = sp + 1

#Example 3: print number from 10 to 1.
# sp = 10

# while sp >= 1:
#     print(sp)
#     sp = sp - 1

#Example :4 print number from 1 to 10 but go 2 step at a time.

# sp = 1

# while sp <= 10:
#     print(sp)
#     sp = sp + 2

#Good Example 1: print 10 natural numbers. 

# sp = 1

# while sp <= 10:
#     print(sp)
#     sp = sp + 1

#Good Example 1: print n natural numbers. 

# n = int(input("Enter the number: "))
# sp = 1

# while sp <= n:
#     print(sp)
#     sp+= 1 # sp = sp + 1

"""
shorthand version of arithmetic operator:
num = 1
num = num + 1 ---> [num+= 1]
num = num - 1 ---> [num-= 1]
num = num * 1 ---> [num*= 1]
num = num / 1 ---> [num/= 1]
num = num // 1 ---> [num//= 1]
num = num ** 1 ---> [num**= 1]
"""

#Good Example 2: to know how to use condional statement inside loop:
#Problem Statment: print only even number from 1 to 10

# sp = 1

# while sp <= 10:
#     #create condtion to print only even number
#     if sp%2==0:
#         print(sp)
#     sp+=1

#Problem Statment: print both even and odd number from 1 to 10

# sp = 1

# while sp<=10:
#     if sp%2==0:
#         print("Even Number", sp)
#     else:
#         print("Odd Number", sp)
#     sp+=1

#Good Example 3: print multiple of 3 from 1 to 20

# sp = 1

# while sp <= 20:
#     if sp%3==0:
#         print(sp)
#     sp+=1
# print(sp) #21

#Good Example 4: find out the sum of first 5 natural numbers.

sp = 1
total = 0

while sp <= 5:
    total+= sp
    sp+=1
print(total)
"""
Visualization(Dry Run):
Given = sp = 1, total = 0

Round/Iteration 1: sp<=5: True
                     total = 0 + 1 => 1
                     [current total = 1] 
                     sp = 1 + 1 -> 2
                     [current sp = 2] 
Round/Iteration 2: sp<=5: True
                     total = 1 + 2 => 3
                     [current total = 3] 
                     sp = 2 + 1 -> 3 
                     [current sp = 3]
Round/Iteration 3: sp<=5: True
                     total = 3 + 3 => 6
                     [current total = 6] 
                     sp = 3 + 1 -> 4
                     [current sp = 4]
Round/Iteration 4: sp<=5: True
                     total = 6 + 4 => 10
                     [current total = 10] 
                     sp = 4 + 1 -> 5
                     [current sp = 5]  
Round/Iteration 5: sp<=5: True
                     total = 10 + 5 => 15
                     [current total = 15] 
                     sp = 5 + 1 -> 6
                     [current sp = 6]  
Round/Iteration 6 sp<=5: False --> Come out of the loop    

"""
    