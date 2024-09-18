#Note: Variable and List is a data structure - where data structure provide you some format/structure to store the data.

#Why List?
#-One limitation with Variable is that it can store one value at a time.

#Example: store 10 interger numbers in variable.
# num1= 10
# num2 = 11
# num3 = 12
# num4 = 13
# num5 = 14
# num6 = 15
# num7 = 16
# num8 = 17
# num9 = 18
# num10 = 19

#Note: Varibale is the best choice, you want to store less number of data of differnt type not same type.

# name = "Rakesh"
# age = 45
# isMarried = True

#Then If we want to store more data of same type then, Is there any solution?

#Solution: List/Array - It is a data structure which is used to store multiple data of same type(Homogenous) or differnt type(Hatrogenous) in a single variable.

#Declaration of List:

# names = [] #declared/created a list with names
# print(names) #empty list

#Initialization of List
#append(data): helps you to add/store the data to end of list.
#Syntax: list_name.append(data)

# Example 1: 
# names.append("Rakesh") #['Rakesh']
# names.append("Punit") #['Rakesh', 'Punit']
# names.append("Sunil")  #['Rakesh', 'Punit', 'Sunil']
# names.append("Shubham") #['Rakesh', 'Punit','Sunil' ,'Shubham']
# names.append("Mahi") #['Rakesh', 'Punit','Sunil' ,'Shubham','Mahi']
# print(names) # ['Rakesh', 'Punit','Sunil' ,'Shubham','Mahi']


#Example 1: add 1 to 20 numbers in below list.

# numbers =  []

# for num in range(1,21):
#     numbers.append(num)

# print(numbers)

#Initialization at the time Declaration


numbers = [1,2,3,4,5,6,7,8,9,10]

"""
How to access the element inside the list?
Note: Python list follows 0 based indexing, meaning that first element in the list starts with 0 index, second element at index 1 and so on.
Note: it also supports -ve indexing it means -1 index is for last element of the list and -2 or second last element of the list and so on.


Example:

nums = [1,2,3,4,5]
index   0 1 2 3 4

Note: to access any element of the list, it is important to know the index of that element.
Syntax: list_name[index]

print(nums[1])
print(nums[-4])

"""

#Example 1:

# nums = [1,2,3,4,5]
# print(nums[1]) #2
# print(nums[-4]) #2


#Example 2: Given a list of fruits, your task is to print each fruit in seperate line.

fruits = ["Papaya", "Mango", "Orange", "Kiwi", "Banana", "Apple", "Guava"]

#First Way:

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[4])
# print(fruits[5])
# print(fruits[6])

#Second way: using loop:

#1st Way:
# for fruit in fruits:
#     print(fruit)

#2nd Way: 
# for fruit in range(7):
#     print(fruits[fruit])

#Above range solution is static solution but as a developer, we need to create dynamic code so that due to any changes to the list, we could not change the loop code.

#For this it is important to know how many elements are there in the list
# count = 0
# for fruit in fruits:
#     count+=1

# print(f"number of element in the list:", count)

# #Other Solution: len(list_name): helps to give you total number of elements in the list.

# print(f"number of element in the list:", len(fruits))

# for fruit in range(len(fruits)):
#     print(fruits[fruit], end=' ')

#Good Examlpe 1: Given a list of numbers, you need to print square of each number in one line.

#input: nums = [1,2,3,4,5,6,7,8,9,10]
#output: nums = [1,4,16,25,36,49,64,81,100]

# nums = [1,2,3,4,5,6,7,8,9,10]

# for number in range(len(nums)):
#     print(nums[number]**2, end=", ")

#Good Examlpe 2: Given a list of numbers, you need to print even number in one line.

# for number in range(len(nums)):
#     if nums[number]%2==0:
#         print(nums[number]**2, end=", ")

#Good Examlpe 3: Given a list of numbers, you need to print odd number in one line.

# for number in range(len(nums)):
#     if nums[number]%2!=0:
#         print(nums[number]**2, end=", ")

#Good Examlpe 4: Given a list of numbers, you need to find odd number in the list and add to the new list.

# nums = [1,2,3,4,5,6,7,8,9,10]
# oddList = []

# for i in range(len(nums)):
#     if nums[i]%2!=0:
#        oddList.append(nums[i]) 

# print("Odd List:", oddList)

#Good Examlpe 5: Given a list of numbers, you need to find even number in the list and add to the new list.

# nums = [1,2,3,4,5,6,7,8,9,10]
# evenList = []

# for i in range(len(nums)):
#     if nums[i]%2==0:
#        evenList.append(nums[i]) 

# print("Even List:", evenList)

#Good Examlpe 6: Given a list of numbers, you need to find the factorial of even number and put them into a seperate list.

nums = [1,2,3,4,5,6,7,8,9,10]

#solution for factorial
# num = 5
# fact = 1
# for n in range(1, num+1):
#     fact*=n
# print(fact)

# evenFactorialList = []
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         fact = 1
#         for n in range(1, nums[i]+1):
#             fact*=n
#         evenFactorialList.append(fact)

# print("Factorial Number List:",evenFactorialList)

#Example 7: take input from user and add it to the list.

# numberList = []

# num = int(input("Enter Numbers: "))
# numberList.append(num)

# print("List: ", numberList)


#Using loop: 

# numberList = []

# while True:
#     num = int(input("Enter Numbers: "))
#     numberList.append(num)

#     res = input("Do you want to add more number(Y/N): ")
#     if res=='N' or res == 'n':
#         print(f"Current List: ", numberList)
#         break

# nums = input("Enter Number space seperated: ")
# print(nums)


# numberList = []

#Example 1:

numberList = []

#Taking input for the list.
while True:
    num = int(input("Enter Numbers: "))
    numberList.append(num)

    res = input("Do you want to add more number(Y/N): ")
    if res=='N' or res == 'n':
        print(f"Current List: ", numberList)
        break


#Another Loop for performing following task on number list.
#1. sum of all numbers
#2. average of all numbers
#3. list even numbers
#4. list odd numbers
#5. Exit

while True:
    print("1. Sum of all Numbers")
    print("2. Average of all Numbers")
    print("3. List Even Numbers")
    print("4. List Odd Numbers")
    print("5. For Exit")
    choice = int(input("Enter Your Choice: "))

    if choice==1:
        #logic for finding the sum
        sum = 0
        for num in numberList:
            sum+=num
        print("Sum of All Numbers: ",sum)
    elif choice==2:
        #logic for average
        sum = 0
        for num in numberList:
            sum+=num
        print("Average of All Number: ",sum/len(numberList))
    elif choice==3:
        #logic for even number
        print("Even Numbers: ",end ='')
        for num in numberList:
            if num%2==0:
                print(num, end=' ')
    elif choice ==4:
        #logic for odd numebr
        print("Odd Numbers: ",end ='')
        for num in numberList:
            if num%2!=0:
                print(num, end=' ')
    elif choice==5:
        #logic for exit
        res = input("Do you want to Exit(Y/N): ")
        if res =='Y' or res =='y':
            print("Thank you for using!")
            break
    else:
        print("Invalid Input")