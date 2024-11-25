#Till now in Object Oriented Programming:
"""
Introduction to OOPS
Why OOPS
Features
Class
Object
static/non static attributes/methods
"""

#Example: Given Student class with instance attributes - name, city, marks. Kindly create 5 different student class object.

# class Student:

#     def __init__(self, name, city, marks):
#         self.studentName = name
#         self.studentCity = city
#         self.studentMarks = marks
    
#     def __str__(self):
#         return str({"name":self.studentName, "city":self.studentCity, "marks":self.studentMarks})

# #Asked to create 5 different object of the class? 
# student1 = Student('Rakesh', "Noida", 456)
# student2 = Student('Prem', "Delhi", 156)
# student3 = Student('Sonal', "Haryana", 343)
# student4 = Student('Rohan', "Chandigarh", 453)
# student5 = Student('Raman', "Rajpura", 346)

# # print(student1.studentName)
# # print(student3.studentCity)

# studentList = [student1, student2, student3, student4, student5]

# #print every student name in seperate line
# # for student in studentList:
# #     print(student.studentName)


# for student in studentList:
#     print(student)


#Rest Oops Pillars:

#Encapsulation:
#Why Encapsulation -

# class Student:
#     #Class Variable - class/object to accesss
#     university = "Chitkara"
#     def __init__(self, name, city, marks):
#         #Instance Variable - Need object to access
#         self.studentName = name
#         self.studentCity = city
#         self.studentMarks = marks

    
#     def __str__(self):
#         return f"Name: {self.studentName}, City: {self.studentCity}, Marks: {self.studentMarks}"
    
# student1 = Student('Rakesh', "Noida", 456)
# print(student1.studentMarks)
# print(student1.university)


# class User:
#     def __init__(self, name):
#         self.name = name
#         self.loginStatus = False

#     def verifyEmail(self, email):
#         #perform validation logic
#         return True
    
#     def verifyPassword(self, password):
#         #perform validation logic
#         return True
    
#     def login(self, email, password):
#         isVerified = False
#         isVerified = self.verifyEmail(email) and self.verifyPassword(password)
        
#         if isVerified:
#             self.email = email
#             self.password = password
#             self.loginStatus = True
#             print("Logged in Successfully.")
#         else:
#             print("Invalid Credentials, Please try again.")


# user1 = User('Prakash')

# # print(user1.name)
# # print(user1.email)
# # user1.login("prakash@gmail.com", "12345")
# # print(user1.email)
# # print(user1.password)

# print(user1.verifyEmail("prakash@gmail.com"))


#According to above example, class data is not secure anyone can access it outside the class.

#Encapsulation: Making all the methods and attribute as private so that outside the class none can access it.

#How to make methods and variables as private: 
#Syntax: __variable/methodName


# class User:
#     def __init__(self, name):
#         self.__name = name #private attribute/variables
#         self.__loginStatus = False #private attribute/variables

#     def __verifyEmail(self, email): #private method
#         #perform validation logic
#         return True
    
#     def __verifyPassword(self, password): #private method
#         #perform validation logic
#         return True
    
#     def login(self, email, password):
#         isVerified = False
#         isVerified = self.__verifyEmail(email) and self.__verifyPassword(password)
        
#         if isVerified:
#             self.__email = email
#             self.__password = password
#             self.__loginStatus = True
#             print("Logged in Successfully.")
#         else:
#             print("Invalid Credentials, Please try again.")
            
#     def logout(self):
#         self.__loginStatus=False
#         print("Logged out successfully")

#     def printDetails(self):
#         if self.__loginStatus:
#             return f"Name: {self.__name}, Email: {self.__email}"
#         else:
#             return "You're logged out, Please login again."


# user1 = User('Prakash')

# print(user1.name)
# print(user1.email)
# user1.login("prakash@gmail.com", "12345")
# print(user1.email)
# print(user1.password)

#print(user1.__verifyEmail("prakash@gmail.com")) #AttributeError - has no attribute as __verifyEmail

#print(user1.__name) #AttributeError - has no attribute as __name
# user1.login("prakash@gmail.com", "12345")
# print(user1.printDetails())
# user1.logout()

# print(user1.printDetails())

#In above example, anyhow we're anle to mantain the encapsulation by making attributes and methods as private, but still it is not fully encapsulated class because you're not able to access the private variable as well as not able to change the variable data.

#Fully Encapsulated class follows:
#1. all the methods and attributes of the class must be private.
#1. it must have getter and setter method to get and update the value of the attributes.

# class User:
#     def __init__(self, name):
#         self.__name = name #private attribute/variables
#         self.__loginStatus = False #private attribute/variables

#     def __verifyEmail(self, email): #private method
#         #perform validation logic
#         return True
    
#     def __verifyPassword(self, password): #private method
#         #perform validation logic
#         return True
    
#     def login(self, email, password):
#         isVerified = False
#         isVerified = self.__verifyEmail(email) and self.__verifyPassword(password)
        
#         if isVerified:
#             self.__email = email
#             self.__password = password
#             self.__loginStatus = True
#             print("Logged in Successfully.")
#         else:
#             print("Invalid Credentials, Please try again.")
            
#     def logout(self):
#         self.__loginStatus=False
#         print("Logged out successfully")

#     def printDetails(self):
#         if self.__loginStatus:
#             return f"Name: {self.__name}, Email: {self.__email}"
#         else:
#             return "You're logged out, Please login again."
    
#     #Getter methods - to get the value
#     def getName(self):
#         return self.__name
    
#     def getEmail(self):
#         return self.__email
    
#     #Setter method - to set/update the value

#     def setName(self, name):
#         self.__name = name
    
#     def setEmail(self, email):
#         self.__email = email


# user1 = User('rohan')
# user1.login('rohan@gmail.com', '12345')
# # print(user1.printDetails())

# # print(user1.getEmail())
# # user1.setEmail('random@gmail.com')
# # print(user1.getEmail())

# user2 = User('admin')

# user2.login('admin', 'admin')
# print(user2.printDetails())


#4. Inheritance: in this a class can access the properties/methods of another class.
#Note: rather than owning anything its better to owe.

"""
Cat Family - Tiger, Lion

Cat properties:
    fur = True
    jump = True
    tail = True
    legs = 4
    - other 20 properties

    methods
    canJump()
      return True

Tiger Properties:

"""

# class Cat:

#     #class properties - to access - class/object
#     jump =True
#     tail =True
#     fur = True
#     legs = 4

#     def __init__(self, name):
#         self.name = name


# class Tiger(Cat):
#     pass

# class Lion(Cat):
#     pass

# cat = Cat('Cat')

# print(cat.name)
# print(cat.fur)
# print(cat.jump)

# print("--------------------")

# tiger = Tiger('Tiger')

# print(tiger.name)
# print(tiger.fur)
# print(tiger.jump)

# print("--------------------")

# lion = Lion('Lion')

# print(lion.name)
# print(lion.fur)
# print(lion.jump)


# class Person:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city
    
#     def printDetails(self):
#         print(f"Name: {self.name}, City: {self.city}")
    
# class Employee(Person):
#     def __init__(self, name,city, salary):
#         super().__init__(name, city)
#         self.salary = salary
    
#     def printDetails(self):
#         super().printDetails()
#         print(f"Salary: {self.salary}")

# employee = Employee('Rakesh', 'Noida', 50000)
# employee.printDetails()

#Polymorphism: As name suggest - poly - many and morphism - forms - in polymorphism, one method can perform different tasks according to the object. 

#There are two types of polymorphism:
#1. method overloading - python doesn't support it. 
#2. method overriding - you can achieve using inheritance.

##1. method overloading - python doesn't support it, but some of the methods of python perform method overloading.

#Example:

# print(len([2,3,3,4,5])) # 5
# print(len("chitkara")) # 8

# class Maths:

#     @staticmethod
#     def sum(*args):
#         return sum(args)
    

# print(Maths.sum(1,2,3,4,5))
# print(Maths.sum(1,2,3))
# print(Maths.sum(1,2))

#2. Method Overriding - you can achieve method overriding with the help of inheritance:


# class Shape:
#     pi = 3.14
#     def area(self):
#         pass

# class Rectangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     #here you've overridden parent class method - method overrding.
#     def area(self):
#         return self.length * self.width
    
# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

    
#     #here you've overridden parent class method - method overrding.
#     def area(self):
#         return self.pi * (self.radius ** 2)
    

# rectangle = Rectangle(10, 20)
# print(rectangle.area())

# print("----------------------")

# circle = Circle(10)
# print(circle.area())

#Abstraction - it shows only the essential information to the user and hider complex implementation.
#Example: Tv Remote, ATM

#How to achieve Abstraction in Python - to achieve abstraction in python, we abstract class.

#Abstract class: it is similar to other, but it also contains abstract method and you can't create the object of abstract class.

#Note: to create the abstract in python you need to import abc module.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def drive(self):
        pass

vehicle = Vehicle()# TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract method 'drive'

