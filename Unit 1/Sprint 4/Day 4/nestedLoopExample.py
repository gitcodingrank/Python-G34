#Nested Loop: Loop Within Loop
#Other Words: When Any loop each iteration/round is related/connected to some set of rounds then in this condition you can achieve this using nested loop.

"""
Syntax:
# outer loop
for var1 in range(n):
    #inner loop
    for var2 in range(n):
"""

#Example: Gol Gappa Analogy:
#20rs -- 4pcs

# outer loop
# for chintu in range(1, 5):
#     print(f"Chintu has done with his round {chintu}")
#     #inner loop
#     for family in range(1,5):
#         print(f"Family Member {family} has done with his round {chintu}")

# using while loop
# chintu=1
# while chintu<=4:
#     print(f"Chintu has done with his round {chintu}")
#     #inner loop
#     family=1
#     while family<=5:
#         print(f"Family Member {family} has done with his round {chintu}")
#         family+=1
#     chintu+=1

#Example 2: Father-Son Analogy
#Problem Statement: Father will go for 2 rounds, in each round of father son will go for 5 rounds

# outer loop
# for father in range(1,3):
#     print(f"Father has started his round {father}")
#     # inner loop
#     for son in range(1, 6):
#         print(f"Son has done his round {son}")
    
#     print(f"Father has end his round {father}")

#Using While loop
# father = 1
# while father<=2:
#     print(f"Father has started his round {father}")
#     # inner loop
#     son=1
#     while son<=5:
#         print(f"Son has done his round {son}")
#         son+=1
#     print(f"Father has end his round {father}")
#     father+=1

#Student Task:Print in the blow manner:
"""
Father Round 1: Son Runds: 1 2 3 4 5
Father Round 2: Son Runds: 1 2 3 4 5
"""

# for father in range(1,3):
#     print("Father Round:",father, end=' ')
    
#     print("Son Rounds:", end="")
#     for son in range(1, 6):
#         print(son, end=' ')
#     print()


"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

# for father in range(1,6):
#     for son in range(1,6):
#         print(son, end=' ')
#     print()

"""
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
"""

# for father in range(1,6):
#     for son in range(5,0,-1):
#         print(son, end=' ')
#     print()

"""
* * * * *
* * * * *
* * * * *
* * * * *
"""

# for father in range(1,6):
#     for son in range(5,0,-1):
#         print('*', end=' ')
#     print()

"""
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# for father in range(1,6):
#     for son in range(1, father+1):
#         print(son, end=' ')
#     print()

"""
*
* *
* * *
* * * *
* * * * *
"""

# for father in range(1,6):
#     for son in range(1, father+1):
#         print('*', end=' ')
#     print()

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# for father in range(5,0,-1):
#     for son in range(1, father+1):
#         print(son, end=' ')
#     print()

"""
* * * * *
* * * * 
* * *
* * 
* 
"""

for father in range(5,0,-1):
    for son in range(1, father+1):
        print('*', end=' ')
    print()

#Conclusion: Outer loop is responsible for rows whereas inner loop is responsibel for column

