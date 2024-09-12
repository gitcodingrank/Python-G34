#break statement: it is used to break/terminate/stop the running loop at certain condition.

"""
syntax
while condition:
    if breakCondition:
        break
    # print(sp)
    increment/Decrement

"""

#Example: print from 1 to 10 but break at 6

# sp = 1
# while sp<=10:
#     if sp==6 or sp ==7:
#         break
#     print(sp)
#     sp+=1
# """
# output:
# 1
# 2
# 3
# 4
# 5
# """

#Example: find out the first even number from 1 to 10

# sp = 1
# while sp<=10:
#     if sp%2==0:
#         print("Even", sp)
#         break
#     sp+=1


#continue statement: it is used to terminate/stop/skip only particular iteration/round accoding to given condition.

#Example 1: print number from 1 to 5 except 3

# sp = 1

# while sp<=5:
#     if sp==3:
#         continue
#     print(sp)
#     sp+=1

"""
above loop has become infinite loop because at sp value 3 you continue statement is terminating the current round because of this sp value has stucked at 3
Visualization:
Given: sp=1
Round 1: sp<=5: True
            sp==3: False
            print: 1
            sp = 1 +1 =>2
Round 2: sp<=5: True
            sp==3: False
            print: 2
             sp = 2 +1 =>3
Round 3: sp<=5: True
           sp==3: True
            continue/terminate
Round 4: sp<=5: True
            sp==3: True
            continue/terminate
Round 5: sp<=5: True
            sp==3: True
            continue/terminate
"""

#What is the solution

# sp = 0

# while sp<=4:
#     sp+=1
#     if sp==3:
#         continue
#     print(sp)

#Example: print 1 to 10 except 5 and 7

sp = 0

while sp<10:
    sp+=1
    if sp == 5 or sp ==7:
        continue
    print(sp)