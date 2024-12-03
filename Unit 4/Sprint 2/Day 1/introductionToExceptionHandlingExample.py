#Exception Handling: it is one of most critical part of every programming language that ensures your code to handle runtime errors gracefully without terminating your program.

#Note: error always occurs on run-time.

#Exception: An event that disrupts the normal flow of your program.

#Why Exception Handling?
#1. prevents abrupt termincation of your program.
#2. on exception , you can give meaningful msg rather than stopping it.

#Example: 

# print("Welcome to India")

# print(4+4)

# age = 45
# print("Eligible" if age>=18 else "Not Eligible")

# #Prime Number Logic

# list = [1,2,3,4,5]
# print(list[8]) #IndexError

# print("Chlo Ghar Chle")

# num = 3
# count = 0
# for i in range(1, num+1): 
#     if num%i==0:
#         count+=1

# if count ==2:
#     print("Prime")
# else:
#     print("Not Prime")

#1000 lines of code.

# file = open('data.txt', 'r')


#How to Handle the Exeption?

"""
to handle exception, we use try and except block.
syntax:

try:
    code that can have error
except ErrorName:
    it handle the error when particular given error occurs.

"""


#Exmaple:

# print("Welcome to Exception Handling")

# try:
#     age 
#     print(age)
# except NameError:
#     print("Can't leave a variable with value")

# print("Let's go to Chitkara University")


#Example:


# print("Welcome to Exception Handling")

# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))

#     print(f"Addition is: {a+b}")

#     print(f"Division is: {a/b}")

# except ValueError:
#     print("Please enter the valid number.")
# except ZeroDivisionError:
#     print("A number can't divide by zero")

# print("Let's go to Chitkara University")

#Other Way for above program:

# print("Welcome to Exception Handling")

# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))

#     print(f"Addition is: {a+b}")

#     print(f"Division is: {a/b}")

# except (ValueError, ZeroDivisionError) as e:
#     print(f"Error is: {e}")

# print("Let's go to Chitkara University")


#Third Way:

# print("Welcome to Exception Handling")

# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))

#     print(f"Addition is: {a+b}")

#     print(f"Division is: {a/b}")

# except Exception as e:
#     print(f"Error is: {e}")

# print("Let's go to Chitkara University")


#Note: one try block can have more than one except block to handle the error gracefully and give the meaningful output to the user.

#else, and finally block.
#else: it runs when there is no error in the try block.

#Example:

# print("Welcome to Exception Handling")

# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))

#     addition = a+b
#     division = a/b

# except ValueError:
#     print("Please take valid Number.")
# except ZeroDivisionError:
#     print("A number can't divide by zero")
# else:
#     print(f"Division is: {division}")
#     print(f"Addition is: {addition}")




# print("Let's go to Chitkara University")

#finally: it executes every time where there is error or not error, it is used to close or stop the important resources:


# print("Welcome to Exception Handling")

# try:
#     file = open('data.txt', 'r')
#     print(file.read())

# except FileNotFoundError:
#     print("File doesn't exit, please create the file.")
# else:
#     print("Inside else block")
# finally:
#     try:
#         file.close()
#     except NameError:
#         print("file doesn't exist.")



# print("Let's go to Chitkara University")



#Problem: Create a program where you're taking input from the user to perform addition, substraction, mulitplication, and division, and also take care about errors, if any error occurs kindly handle it and give meaningful msg.


# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))

#     addition = a+b
#     division = a/b
#     subtraction = a-b
#     multiplication = a-b

# except ValueError:
#     print("Please take valid Number.")
# except ZeroDivisionError:
#     print("A number can't divide by zero")
# else:
#     print(f"Division is: {division}")
#     print(f"Addition is: {addition}")
#     print(f"Difference is: {subtraction}")
#     print(f"Product is: {multiplication}")


#Problem 2: Create a program, where your task is to read the file and if file doesn't exist, create the file.

# try:
#     file = open('data.txt', 'r')
#     print(file.read())
# except FileNotFoundError:
#     file = open('data.txt', 'w')
#     print("File has created.")
#     file.write('Welcome to Chitkara University')
#     print("Data has inserted.")
# finally:
#     file.close()


#How to raise exception? - using raise function.

# try:
#     age = int(input("Enter Age: "))

#     if age>=18:
#         print("permission granted.")
#     else:
#         raise ValueError('Age must be greater than or equal to 18')
# except ValueError as e:
#     print(f"Error is {e}")


#There are two types of exception:
#1. inbuilt exception: examples above
#Example: FileNotFoundError, NameError, ValueError, IndexError, KeyError, and so on.

#2. Custom Exception - you can create your own exception as well.

#Note: need to inheritate the exception class which is parent of all the clas.
"""
clas Excpetion:
    def __init__(self, message):
        self.message = message

"""


class AgeNotMatchedException(Exception):
    def __init__(self, message):
        super().__init__(message)

class StudentNotFoundExeption(Exception):
    def __init__(self, message):
        super().__init__(message)

# try:
#     age = int(input("Enter Age: "))

#     if age>=18:
#         print("permission granted.")
#     else:
#         raise AgeNotMatchedException('Age must be greater than or equal to 18')
# except AgeNotMatchedException as e:
#     print(f"Error is {e}")

#Example 2:

# try:
#     rollNumber = input("Enter Student RollNumber: ")

#     if rollNumber == "12345678":
#         print("Received Student Data.")
#     else:
#         raise StudentNotFoundExeption("Invalid Student Roll Number")
# except StudentNotFoundExeption as e:
#     print(f"Error is {e}")


#Problem: Create BookNotFoundException if the bookId is not matching with 12345 then raise this exception and give the meaninful msg.


