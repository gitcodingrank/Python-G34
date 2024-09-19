#Good Example 1: Given a list of numbers, you need find out square of even number and put them to the seperate list.

# nums = [1,2,3,4,5,6,7,8,9,10]

# evenSquareList = []

# for i in nums:
#     if i%2==0:
#        evenSquareList.append(i**2)

# print(evenSquareList)

#Good Example 2: Check a given list is empty list or not.

# list1 = [] #List1 is empty

# if len(list1)==0:
#     print("List1 is empty")
# else:
#     print("List1 is not empty")

# list2 = [3,4,5] #List2 is empty
# if len(list2)==0:
#     print("List2 is empty")
# else:
#     print("List2 is not empty")


#Good Example 3: Given a list of numbers, you need to find out the minimum number and print it.

# nums = [50,6,3,1,45,78,56,34,22]

# minValue = nums[0]

# for i in range(1,len(nums)):
#     if minValue > nums[i]:
#         minValue = nums[i]

# print("Minimum Value is:",minValue)
# #Can you find out the maximum value?

#Important functions of list:
# nums = [1,2,3,4,5,6,7,8,9,10]
# total = sum(nums)

# #Assignment: Try without using sum function
# print(total)

# minValue = min(nums)
# #Assignment: Try without using sum function
# print(minValue)

# maxValue = max(nums)
# #Assignment: Try without using sum function
# print(maxValue)

# size = len(nums)
# #Assignment: Try without using sum function
# print(size)

#List Methods

# nums = [4,12,34]

# nums.append(45) #add element at the end of list
# print(nums) # [4,12,34, 45]

# nums.insert(2, 56) #[4,12,56,34 45]
# print(nums)

# nList = [90,100,120]

# nums.extend(nList)
# print(nums)

# numbers = [1,2,3,4,5,6,7,8,9,10]

# numbers.remove(5)
# print(numbers)

# fruits = ["Apple", "Banana", "Mango", "Grapes"]

# fruits.remove("Mango")
# print(fruits) #['Apple', 'Banana', 'Grapes']

#list.pop(): it removes element from end of the list, and it also returns removed element

# removedElement = fruits.pop()
# print(removedElement) #Grapes
# print(fruits)

#list.pop(index): it removes element at certain index and returned that removed element

# fruits = ["Apple", "Banana", "Mango", "Grapes"]

# removedElement = fruits.pop(0)
# print(removedElement)
# print(fruits)

#list.reverse():

# nums = [1,2,3,4,5]
# nums.reverse()
# print(nums)


#Conclusion list:
"""
1. List is the best choice if your frequent operations are traversing/searching/visiting each element of the list.

2. List is the worst choice if your frequent operations are deleting and additing elements at sepecific element.

Examples:

nums = [1,2,3,4,5]

Case 1: Addition
add 6 at index 1
In this case to add particular eleemnt, you're having to do lots of shifting which takes time that's why addition at some index is not the best choice.

Case 2: Deletion
nums = [1,2,3,4,5]
delete element at index 3
In this case to delete particular eleemnt, you're having to do lots of shifting which takes time that's why deletion of element at some index is not the best choice.

3. List is the best choice for same type(homogenous data) of data not for different type(hatrogenous) of data

"""

# names = ["Rakesh", "Chaman", "Deepak"]
# ages = [45, 12, 23]
# isMarried = [True, False, False]

#Problem: print the age and married status of Rakesh

# #Main Logic
# for i in range(len(names)):
#     if names[i]=="Rakesh":
#         print("Ages of Rakesh: ", ages[i])
#         print("Married Status of Rakesh: ","Married" if isMarried[i] else "Not Married")


#Hatrogenous:

# persons = ["Rakesh", 45, True, "Chaman", 12, False, "Deepak", 23, False]
# #Problem: print the age and married status of Rakesh
# #Extra Work: Filteration of data for putting the main logic
# names =[]
# for i in range(0,len(persons),3):
#     names.append(persons[i])

# ages =[]
# for i in range(1,len(persons),3):
#     ages.append(persons[i])

# marriedStatus =[]
# for i in range(2,len(persons),3):
#     marriedStatus.append(persons[i])

# print(names)
# print(ages)
# print(marriedStatus)

# #Main Logic
# for i in range(len(names)):
#     if names[i]=="Rakesh":
#         print("Ages of Rakesh: ", ages[i])
#         print("Married Status of Rakesh: ","Married" if marriedStatus[i] else "Not Married")














