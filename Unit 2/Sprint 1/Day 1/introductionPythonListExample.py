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

names = [] #declared/created a list with names
print(names) #empty list

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


