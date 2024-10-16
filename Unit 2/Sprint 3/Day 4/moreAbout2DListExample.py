items=[
	["Ajay", 28, "male", [1,2,3]],
	["Hitesh", 30, "male", [4,5,6]]
];

#Want to access 3
print(items[0][3][2])
print(items[1][2][1])
print(items[1][0][2])


#Student Tasks:

#Problem 1:

# items=[
# 	[1,2,3],
# 	[4,5,6],
# 	[7,8,9]
# ];

# rows = len(items)
# columns = len(items[1])

# #outer loop: rows
# for row in range(rows):
#     #inner loop: columns
#     for column in range(columns):
#         print(items[row][column], end=" ")
#     print()


#Problem 2
# items=[
# 	[1,2,3],
# 	[4,5,6],
# 	[7,8,9,56,34],
#     [2,3,4,6,7,8,10]
# ];

# rows = len(items)

# #outer loop: rows
# for row in range(rows):
#     #inner loop: columns
#     for column in range(len(items[row])):
#         print(items[row][column], end=" ")
#     print()

#Problem 3: print row wise sum of the following 2D List.

#input
items=[
	[1,2,3],
	[4,5,6],
	[1,8,9]
];

#output
6
15
24

#outer loop: rows
# for row in range(len(items)):
#     #inner loop: columns
#     sum = 0
#     for column in range(len(items[0])):
#         sum+=items[row][column]
#     print(sum)

#Problem 4: print even sum row wise.

#outer loop: rows
# for row in range(len(items)):
#     #inner loop: columns
#     sum = 0
#     for column in range(len(items[0])):
#         if items[row][column]%2==0:
#              sum+=items[row][column]
#     print(sum)

#Problem 5: print yes if there is atleast one prime number in row if not then print no, do this for all rows

def checkPrime(num):
    count=0
    for i in range(1, num+1):
        if num%i==0:
            count+=1
    return count==2


for row in range(len(items)):
    #inner loop: columns
    noticePerson = False
    for column in range(len(items[0])):
        if checkPrime(items[row][column]):
             noticePerson=True
             break
    if noticePerson:
        print("Yes")
    else:
        print("No")


#Problem 6: Do above operation column wise.

