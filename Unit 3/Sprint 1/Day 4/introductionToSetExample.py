#Set - it is a data structure which is collection of unique elements.

#Points about Set:
#1. Unordered
#2. Mutable
#3. No Indexing
#4. Unique elements

#Decalration of Set

# list = [1,2,3,4,5,2,3,1,2,1,2,3,4]

# nums = set()
# print(nums) # 
# print(type(nums)) #<class 'set'>

# nums = {1,2,3,4,5}
# print(nums)

# personSet = set()

# #How to add elements to the set.

# personSet.add("Rakesh")
# personSet.add("Pawan")
# personSet.add("Siya")
# personSet.add("Kunal")

# personSet.add("Rakesh")

# print(personSet)

#How to add multiple element to the set?

# personSet.update(["Shivangi", "Rohan"])

# print(personSet)

# #How to remove/delete element from set?

# #remove('')

# personSet.remove('Rohan')
# #personSet.remove('Sita') #Error if  element is not present inside set.
# personSet.discard('Sita')#No Error if element is not inside set.

# personSet.discard('Rakesh')
# print(personSet)

# #pop() - it deletes arbitary element

# personSet.pop()
# print(personSet)


# numSet = {1,2,3,4,5,5,6,4,3,2,1}
# print(numSet)
# # print(len(numSet))

# #looping set

# for item in numSet:
#     print(item, end=" ")


#Problem 1: given a list of numbers your task is to print only unique numebers.

# numsList = [1,2,3,4,5,6,3,2,1,2,3,5,6,7,2,3,8,7,8,9,10]
# numsSet = set(numsList)
# print(numsSet)

#Set Operations:

# set1 = {1,2,3}
# set2 = {3,4,5}

# #union - |
# unionResult = set1 | set2
# print(unionResult) #{1,2,3,4,5}

# #intersection - &

# intersectionResult = set1 & set2
# print(intersectionResult)


#copy(), clear()

nums = {1,2,3,4,5,6}

# print(f"Before Clearing the set: {nums}")

# nums.clear()

# print(f"After Clearing the set: {nums}")

# numsSet = nums.copy()
# print(numsSet)


