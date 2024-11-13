#Bubble Sort Algorithm: to sort the elements either in ascending or descending order.
#definition- it is simpel algorithm that works by repeatedly swaping adjacent elements. If they are in wrong order.
#Ascending: Greater element will bubble up to its correct position
#Descending:Smaller element will bubble up to its correct position 


#How does it work? - Ascending Order
#1. Initial Setup - Start with entire list as unsorted
#2. Swap with Adjacent Element: It will swap adjacent element if they in wrong order[ascending: if element is greater than adjacent element then swap, descending: if element is greater than adjacent element then swap]
#3. Repeat: In Each pass, you will able to shift larger element at last, keep repeating above process until the list is sorted.

"""
Example - Ascending Order
list = [5,0,6,2,3,1]
First Pass: [0,5,2,3,1,6]
Second Pass: [0,2,3,1,5,6]
Third Pass:[0,2,1,3,5,6]
Fourth Pass:[0,1,2,3,5,6]

list = [6,4,2,8,9,7,0]
First Pass: [4,2,6,8,7,0,9] n-1
Second Pass: [2,4,6,7,0,8,9] n-2
Third Pass: [2,4,6,0,7,8,9] n-3
Fourth Pass: [2,4,0,6,7,8,9] n-4
Fifth Pass: [2,0,4,6,7,8,9] n-5
Sixth Pass: [0,2,4,6,7,8,9] n-6


Code:
list = [6,4,2,8,9,7,0]
for i in range(len(list)):
    for j in range(len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

Visualization:
Round 1 : i = 0
          j = 0 , j<6
          [4,2,6,8,7,0,9] - n-1
Round 2: i = 1
         j = 0, j<5
         [2,4,6,7,0,8,9] - n-2
Round 3: i = 2
         j = 0, j<4
         [2,4,6,0,7,8,9] - n-3
Round 4: i = 3
         j = 0, j<3
         [2,4,0,6,7,8,9] - n-4
Round 5: i = 4
         j = 0, j<2
         [2,0,4,6,7,8,9] - n-5
Round 6: i = 5
         j = 0, j<1
         [0,2,4,6,7,8,9] - n-6

"""

list = [6,4,2,8,9,7,0]

#Ascending Order

# print(f"Before Sorting: {list}")

# for i in range(len(list)):
#     for j in range(len(list)-i-1):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]


# print(f"After Sorting: {list}")


#Descending Order

print(f"Before Sorting: {list}")

for i in range(len(list)):
    for j in range(len(list)-i-1):
        if list[j] < list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]


print(f"After Sorting: {list}")