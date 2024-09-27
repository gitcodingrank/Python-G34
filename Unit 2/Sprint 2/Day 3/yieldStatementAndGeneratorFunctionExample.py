#yield statement: Unlike return, yeild keyword remebers the previous and in each execution it stops the function returns the value and again resumes the function returns the value and so on.

#such functions are known as generator function, and these function return iterator.

# def printEvenNumbersFromList(nums):
#     for i in nums:
#         if i%2==0:
#             yield i


# nums = [1,2,3,4,5,6,7,8,9,10]
# value = printEvenNumbersFromList(nums)

# for i in value:
#     print(i, end=" ")

# for i in printEvenNumbersFromList(nums):
#     print(i, end=" ")