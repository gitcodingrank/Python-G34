#Problem:  10 Test Cases - 1 Test Case - 9 Test Cases are hidden

#Input Taking: 

"""
input: read the input statement carefully

First Test Case:
4 3
1 2 3
4 5 6
7 8 9
3 2 1
rows, columns = [int(n) for n in input().split()]
list = []
# for row in range(rows):
#     list.append([int(num) for num in input().split()])

for row in range(rows):
    numlist = input().split()
    innerList = []
    for num in numList:
        innerList.append(int(num))
    list.append(innerList)

    
    
9 Test Cases - Hidden

"""

#Input taking in case of 2d list
#solution 1
# rows, columns = [int(n) for n in input().split()]

# list = []
# for row in range(rows):
#     list.append([int(num) for num in input().split()])

# print(list)


#solution 2
# strList = input().split()
# rows = int(strList[0])
# columns = int(strList[1])

# list = []

# for row in range(rows):
#     strs = input().split()
#     innerList = []
#     for char in strs:
#         innerList.append(int(char))
#     list.append(innerList)

# print(list)