#Example 1: find out factorial any number using for loop.

# fact = 1
# num = 5

# for i in range(1, num+1):
#     fact*=i

# print(fact)

#Example 2: find out the sum of odd number from 1 to 50

# total = 0

# for i in range(1, 51):
#     if i%2!=0:
#         total+=i

# print(total)

#Exmaple 3: count the even number from 1 to 20

# count = 0
# for i in range(1,21):
#     if i%2==0:
#         count+=1

# if count==0:
#     print("There is no even numeber")
# else:
#     print("Even Numbers are:", count)



# Example: check a number is prime or not.
"""
Visualization:
Prime Number has two factors which means they can either divived by itself or 1

Examples:
3---> 3%1----3/2----3/3
      Yes    No     Yes
       1             1
Note: If Factor count is exact 2 then you can say its prime number

4---> 4%1----4%2----4%3-----4%4
      Yes    Yes    No       Yes
       1      1               1
Once there is 3 factors for 4 number that's why its not prime number.
"""

# num = 6
# count = 0
# for i in range(1, num + 1):
#     if num%i==0:
#         count+=1

# if count==2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")
