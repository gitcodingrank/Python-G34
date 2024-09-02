# Comparison Operator: it compare same and different type of value, or you can use it to create conditions.
#Note: whenever we compare two different value that kind of comparison is known as condition or criteria
#-Comparison operator always returns Boolean value (Either True or False)

#There are following types of Comparison Operators:
#Operators: 
#1.  <(less than): it returns true once first value is greater than 
#2.  >(greater than): it returns true once first value is less than
#3.  <=(less than or equal to): it returns true once first value is greater than or equal to other value 
#4.  >=(greater than or equal to): it returns true once first value is less than or eqaul to other value.
#5. == (double equalt to): to check equality
#6. !=(not equal to): to not check equality

#Examples: check a number is negative or positive

num = 34
#conditionToCheckNegativeNumber = num < 0
#print(conditionToCheckNegativeNumber) #False

#Case 1: less than
print(num < 0) #False
#False: Number is positive
#True: Number is negative

#Case 2: greater than
print(num > 0) #True
#True: Number is positive
#False: Number is negative

#Example 2: check a number is greater or eqaul to

# num1 = 60
# num2 = 60

# print(num1 > num2) #False
# print(num1 < num2) #False

# print(num1 >= num2) #True
# print(num1 <= num2) #True


#5. == (double equal to): to compare/check equality
#5. != (not equal to): to compare/check not equality

#Example: check a number is equal to another number or not

# num1 = 45
# num2 = 56

# print(num1 == num2) #False
# print(num1 != num2) #True

# #Let's compare now with different types of value

# #Exmaple: 
# name1 = "Prince"
# name2 = "Rohan"

# print(name1 == name2) #False
# print(name1 != name2) #True

# print(45 == "45") #False
# print(45 != "45") #True


# print(True == 1) #True
# print(False == 0) #True

#Note: when you've numeric types of data to compare then only proceed with <, >, <=, >= operators, if you've mix kind of data to compare then proceed with ==, !=


#Good Example 1: Take a number from the user using input statement and check that number is odd or even.

# num = int(input("Enter Number: "))

# print(num % 2==0) #True
# #True: Number is even
# #False: Number is odd








