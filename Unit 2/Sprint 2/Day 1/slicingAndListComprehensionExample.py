#Slicing In List: - It is used to slice/extract some part of your list in continuous manner and return that sliced/extracted list.  

"""
Syntax:
listName[sp:stop:step] - default values:  sp = 0, stop: end of list, step:1

nums = [1,2,3,4,5,6,7,8,9,10]

nums[:] - [1,2,3,4,5,6,7,8,9,10]
nums[1:] - [2,3,4,5,6,7,8,9,10]
nums[1:3] - [2,3]
nums[1::2] - [2,4,6,8,10]

"""

# nums = [1,2,3,4,5,6,7,8,9,10]

# list1 = nums[:]
# print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list2 = nums[2:]
# print(list2) #[3, 4, 5, 6, 7, 8, 9, 10]

# list2 = nums[2:5]
# print(list2) #[3, 4, 5 ]

# list3 = nums[::2]
# print(list3) #[1, 3, 5, 7, 9]

# nums = [1,2,3,4,5,6,7,8,9,10]

# print(nums[-1:-5:-1])

# print(nums[-1::-1])

#List Comprehension: It is used to create the list and do some operation on list in short and concise manner.

"""
Syntax:
list = [expression loop condition]

Problem: Create a list of numbers from 1 to 10

#Without LC
nums = []
for i in range(1,11):
    nums.append(i)

#With LC
list = [x for x in range(1,11)]
print(list) #[1,2,3,4,5,6,7,8,9,10]
    
"""

# list = [x for x in range(1,11)]
# print(list) #[1,2,3,4,5,6,7,8,9,10]

# list = [x**2 for x in range(1,11)]
# print(list) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list = [x**2 for x in range(1,11) if x%2==0]
# print(list) # [4, 16, 36, 64, 100]


nums = [23,34,45,56,67,89,34,12]

# list = [x for x in nums if x%2==0]
# print(list)