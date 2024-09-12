#Why For Loop: As compare to while loop, for loop is the simple and consise in term of use that makes your code more readable and maintainable.

#Problem with While loop: 
#1. in the case of while loop we're having to write following this at different place that increase the length/lines of code.
#1. statingPoint
#2. where to stop(condition)
#3. step(increment/decrement)

#Solution: your for loop solves the problem of while loop where you can write all three part of loop at one place using range() function

#2. in the case of continue statement, it ends up with infinite loop, if you don't use continue statement in the right manner.

#Solution: your for loop solves the problem of infinite loop and effectively use continue and break statement.

#For Loop: it is also used to execute block of code/same lines of code again and again until the condition is true.

"""
syntax:

for var_name in sequence:
    print("code to execute")

Note: you can use range() to decite the sequence
Example:

Case 1:
range(n) #n is integer number here
#Example:
for sp in range(5):
    print("code to execute")

range(5) #sp=0, where to stop(sp<5), step=sp+=1

Case 2:
range(1, 5) 
#Example:
for sp in range(1,5):
    print("code to execute")

range(1,5) #sp=1, where to stop(sp<5), step=sp+=1

Case 3:
range(1, 5, 2) 
#Example:
for sp in range(1,5,2):
    print("code to execute")

range(1,5,2) #sp=1, where to stop(sp<5), step=sp+=2

"""

#Example 1: print number from 1 to 10

# for sp in range(10): #sp = 0, sp<10, step=sp+=1
#     print(sp+1)

# for sp in range(1,11): #sp = 1, sp<11, step=sp+=1
#     print(sp)

# for sp in range(1,11,1): #sp = 1, sp<11, step=sp+=1
#     print(sp)

#Example 2: print even number from 1 to 20
#range(1, 21)

# for sp in range(1,21):
#     if sp%2==0:
#         print(sp)

#for loop execution process: 
#sp = 1---->check condition(true)-->for loop body execution --->increment of sp--->check condition(true)-->for loop body execution --->increment of sp--->check condition(false) -->come out fo the loop/for loop stopped.

