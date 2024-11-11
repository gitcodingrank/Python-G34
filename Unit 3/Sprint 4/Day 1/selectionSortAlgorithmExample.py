#Selection Sort: It is comparison based algorithm that works by dividing the list into sorted, unsorted part, and repeatedly searching mininum(ascending)/maximum(descending) element from unsorted part and swap with first element of unsorted part, and keep on doing this until list is sorted.

#How does it work? - Ascending Order
#1. Intial Setup: Start with the entire is as unsorted.
#2. Find the Mininum Element: Find Mininum Element from unsorted part.
#3. Swap: Swap the mininum element with first element of unsorted part.
#4. Repeat: Repeat above process until the list is sorted.

"""
Example: Ascending Order
list = [5,1,3,2,0]

First Pass: Smaller Element in [5,1,3,2,0] is 0 then swap with 5 - [0,1,3,2,5]
Second Pass: Smaller Element in [1,3,2,5] is 1 then swap with 1 - [0,1,3,2,5]
Third Pass: Smaller Element in [3,2,5] is 2 then swap with 3 - [0,1,2,3,5]

Example - Ascending order
list = [7,0,4,6,1,5]

First Pass: Smaller [7,0,4,6,1,5] 0 with swap with 7 [0,7,4,6,1,5]
Second Pass: Smaller[7,4,6,1,5] 1 with swap with 7 [0,1,4,6,7,5]
Third Pass: Smaller[4,6,7,5] 4 with swap with 4 [0,1,4,6,7,5]
Fourth Pass: Smaller[6,7,5] 5 with swap with 6 [0,1,4,5,7,6]
Fifth Pass: Smaller[7,6] 6 with swap with 7 [0,1,4,5,6,7]

Descending Order - Try by yourself:


list = [7,0,4,6,1,5]

for i in range(len(list)-1):
    smallIndex = i
    for j in range(i+1, len(list)):
        if list[smallIndex] > list[j]:
            smallIndex = j
    list[i], list[smallIndex] = list[smallIndex], list[i]

    

How to Swap Element?
Problem 1: Swap two element without taking help of third variable.

a = 4
b = 5

#Solution 1: with the help third variable
temp = a
a = b
b = temp

#Solution 1: withput the help third variable

a , b = b, a 


#Example 2: 
list = [5,6,8]
#Solution 1: with the help third variable
temp = list[1]
list[1] = list[2]
list[2] = temp

#Solution 1: withput the help third variable
list[1], list[2] = list[2], list[1]

"""

#Ascending Order
# list = [7,0,4,6,1,5]


# print(f"Before Sorting: {list}")

# for i in range(len(list)-1):
#     smallIndex = i
#     for j in range(i+1, len(list)):
#         if list[smallIndex] > list[j]:
#             smallIndex = j
#     list[i], list[smallIndex] = list[smallIndex], list[i]


# print(f"After Sorting: {list}")


#Descending Order:

list = [7,0,4,6,1,5]


print(f"Before Sorting: {list}")

for i in range(len(list)-1):
    largeIndex = i
    for j in range(i+1, len(list)):
        if list[largeIndex] < list[j]:
            largeIndex = j
    list[i], list[largeIndex] = list[largeIndex], list[i]


print(f"After Sorting: {list}")