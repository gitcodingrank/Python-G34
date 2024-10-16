#1D List: it is just is collection of elements shared as a single variable.

nums = [1,2,3,4,5,6,7,8,9,10]

#2D List: it is also collections of elements in the form of matrix which is also shared as a single variable.

nums = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]

#Example 1: Create a list which is having string, numbers, and another list.

student = ["Chintu", 34, True, ["Java", "Javascript", "Python", "React"]]

#Why 2D List? - if you want to store the data in the form of rows and column then 2D List is the best choice.
#It is just collection of inner lists.


#Declaration of list

# nums = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

#to access particular element in the 2D List - listName[row][column]
#Example
# print(nums[0][2])
# print(nums[1][4])
# print(nums[2][3])

#replacement/updatino:

# nums[2][3] = 20
# print(nums)

# nums = []
# # nums.append([1,2,3,4,5])
# # print(nums)
# bag = []
# for i in range(1, 16):
#     if (i==5) or (i==10) or (i==15):
#         bag.append(i)
#         nums.append(bag)
#         bag = []
#     bag.append(i)

# print(nums)

#To access element through loop, two things are important: rows and columns.

#Consistent columns.
# nums = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

#Rows
# print(len(nums)) #3
# #Columns
# print(len(nums[0])) #5

#Not Consistent columns.
# nums = [
#     [1,2,3,4,5],
#     [6,7,8],
#     [11,12,13,15]
# ]

#Rows
# print(len(nums)) #3
#Columns
#Note: in the above case, you will have to select each rows for exact column size.

# print(len(nums[0]))
# print(len(nums[1]))
# print(len(nums[2]))


#Consistent Column Example
# nums = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

# rows = len(nums)
# columns = len(nums[0])

# #outer loop: rows
# for row in range(0, rows):
#     #inner loop: columns
#     for column in range(0,columns):
#         print(nums[row][column], end=" ")
#     print()

#Different Column Size:
nums = [
    [1,2,3,4,5],
    [6,7,8],
    [11,12,13,15]
]

rows = len(nums)

#outer loop: rows
for row in range(0, rows):
    #inner loop: columns
    for column in range(0,len(nums[row])):
        print(nums[row][column], end=" ")
    print()




     