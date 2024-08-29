#Single Line Comment: tells about what particular lines of code is all about.

#Variable: it is like a container/box which is used to store some technical/virtual data.

#technical data: it is colletion of numbers and words

#Numbers: 1. integer numbers(+ve(23, 34, 89098), -ve(-45,-675,-690)), 2. decimal number(456.56, 34232.00045(float number))
#Real Life Examples: customerAge = 34, orderCount=45,salary=98789.67, ITDepartmentSalary=45434.4534

#Words(Strings): It is collections of characters(numbers + letters+ special symbols) enclosed with single ('') or double duatation marks ("")
#Real Life Examples: customerName = "Bob Singh", address = "Nand Colony Sector 73", username = "bob@1234", password = "bob123434@", pincode = "201301"


#Declaration is also known as creating/making something.


#Declaration/creation/defining of variable
#Syntax: how to use particular concept in python, please don't be the friend of syntax.
#varible_name


#Examples

#pictures 
#age

#Note: it is important to initialize/store/add value to the variable at the time of declaration.

#how to store/initilize/add value to the variable: = (sign/operator): assignment operator - it is used to assign/store value to the variable.

# pictures = "Annual Function Award"
# name = "Shivani"
# age = 23

#Note: left side of assignment operator(=) is always variable and right side of this assignment operator(=) is always value.


#how to check what is there inside paticular variable: print() - its like a tool which helps us to print something on console.
#print(variable_name)

# print(pictures)
# print(name)
# print(name, age)
# print("Shivani", age)
# print("Hello, I'm",name, "and",age, "years", "olds.")


#Rules for taking valid variable name

#1. Start with a letter or underscore (_)

#1name #invalid variable name as it is starting with number
#$age #invalid variable  name as it is starting with special symbol($)
#_age #valid variable name as it is starting with underscore(_)
#fatherName #valid variable name as it is starting with letter.

#2. Can contain letters, numbers, and underscores.

#father name #invalid variable name as it is containing space
#age$ #invalid variable name as it is containing $
#father_name  #valid variable name as it is containing underscore and letters.

#3. Case-sensitive, myVar, and myvar are considered different variables.

#4. Avoid using Python-reserved words as variable names like while, if, and 

#class #invalid variable name as it is python pre-defined word which is having some functionality.
#Class #valid variable name
#if #invalid variable name as it is python pre-defined work which has certain functionality

#5. At the time of declaration of a variable its important to Initialize it.

#----------------------------------------------------------------
#VariableNamingConvention: so that, you can create meaningful variable names.

#Note: if your variable name is single worded, then naming convention rules don't apply like:

name = "Thapa"
age = 34

#What if when we have multi-word variable name, for this we've two types of naming convetion which are given follow.


#camelCaseNamingConvention:

fatherName
firstName
customerName
myClassTeacherName

#snack_case_naming_convention

father_name
first_name
customer_name
employee_name
employee_age
my_class_teacher_name

