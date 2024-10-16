# #Below is the jagged list
# nums = [
#     [1,2,3],
#     [4,5],
#     [6,7,8,9,10]
# ]

# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         print(nums[i][j], end=" ")
#     print()

# nums = [
#     [1,2,3,5,4],
#     [4,5,5,3,5],
#     [6,7,8,9,10]
# ]

# for i in range(len(nums)):
#     for j in range(len(nums[0])):
#         print(nums[i][j], end=" ")
#     print()

#Example 1: Given a list below, your task is to perform following Operations.

nums = [
    [1,2,3,4],
    [4,5,6,4],
    [7,8,9,6],
    [7,8,9,10],
]

"""
Visualization:
1(nums[0][0]) + 5(nums[1][1]) + 9(nums[2][2])

for i in range(len(nums)):
    print(nums[i][i], end=" ")

4(nums[0][3]) + 6(nums[1][2]) + 8(nums[2][1]) + 7(nums[3][0])

for i in range(len(nums)):
    print(nums[i][len(nums)-1-i], end=" ")
"""


#Example 2: 

# nums = [
#     [1,2,3,4],
#     [4,5,6,4],
#     [7,8,9,6],
#     [7,8,9,10],
# ]

"""
1(nums[0][0])  2(nums[0][1])  3(nums[0][2]) 4(nums[0][3])--
4(nums[1][3]) 6(nums[1][2]) 5(nums[1][1])  4(nums[1][0])--
7(nums[2][0]) 8(nums[2][1]) 9(nums[2][2])  6(nums[2][3])
|
|

"""
# for i in range(len(nums)):
#     if i%2==0:
#         #move forward
#         pass
#     else:
#         #move backward
#         pass

# nums = [
#     [1,2,3,4],
#     [4,5,6,4],
#     [7,8,9,6],
#     [7,8,9,10],
# ]


#Implementation of all Matrix operations

#Addition

matrix1 = [
    [1,2,3],
    [4,5,6]
]

matrix2 = [
    [1,5,4],
    [7,8,9]
]

addMatrix = [
    [0,0,0],
    [0,0,0]
]

for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        addMatrix[i][j] = matrix1[i][j] + matrix2[i][j]

print(addMatrix)

#Subtraction
#Mulitplication