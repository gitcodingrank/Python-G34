#tuple - it is a data structure, ordered, and immutable collection of elements

#Characteristic of Tuple:
#1. ordered
#2. immutable
#3. follows indexing
#4. allow duplicate

#decalaration of tuple

#syntax - variableName = ()

# nums = () #here, we created a tuple with name nums.
# print(nums)
# print(type(nums)) #<class 'tuple'>

#Note: once tuple is immutable, therefore, addition, updation, and modification of any element is not allowed.

#nums = (1,2,3,4,5,6,7,8,9,10)

#indexing
# print(nums[4])
# print(nums[len(nums)-1])

#support -ve indexing like list and string
#print(nums[-1])

#looping in tuple
# #1st way:
# for item in nums:
#     print(item, end=" ")

# print()

# #2nd way:
# for i in range(len(nums)):
#     print(nums[i], end=" ")


#condition inside loop:

#Problem: print only even numbers

# for item in nums:
#     if item%2==0:
#         print(item, end=" ")

#tuple slicing

# fruits = ("Papaya", "Mango", "Orange", "Grapes", "Guava")

# print(fruits[1:])
# print(fruits[:])
# print(fruits[::-1])

#immutability

# fruits = ("Papaya", "Mango", "Orange", "Grapes", "Guava")

# fruits[0] = "Kiwi" #TypeError: 'tuple' object does not support item assignment


#packing and upacking - tuple and list.

#packing - store multiple elements into one variable 
# #Example:
# nums = [1,2,3,4,5] #packing

# #unpacking - expending the list or tuple into individual variables.

# a,*b= nums #unpacking
# print(a)
# print(b)


fruits = ("Papaya", "Mango", "Orange", "Grapes", "Guava") #packing


# fruit1, fruit2, fruit3, fruit4, fruuit5 = fruits

# print(fruit1, fruit2)

# fruit1 , *restFruits = fruits

# print(fruit1, restFruits)

#Note: in the case of tuple unpacking, while *arws opeator it returns always list.

#inbuilt function fpr tuple:

nums = (1,2,3,4,5)

print(sum(nums))
print(max(nums))
print(min(nums))
print(len(nums))
print(sorted(nums, key=None, reverse=True))

#Ended.


 














