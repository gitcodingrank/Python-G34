#Object Oriented Programming: It is most popular programming paradigm where object is the first citizen.
#In other word: With the help of object, you can solve any problem.

#Benifit of Object Oriented Programming:
#1. Reusability
#2. Stratured/Modularity
#3. Data Security/Hiding
#4. Abstraction

#Pillars of Object Oriented Programming:
#1. class
#2. object
#3. Encapsulation
#4. Inheritance
#5. Polymorphism
#6. Abstraction


#1. class - it is a blueprint/structure for creating the objects.
#Note: you can create class using 'class' keyword, and always give the name of the class in PascalCaseNamingConvetion.

"""
synatax:
class ClassName:
    #class body
"""

class Mobile:
    #properties
    #behaviors
    pass

#Note: in a class, there are two types of methods, and attribute/variables/states/properties

#Methods:
#1. static/class method 
#2. non static/instance method

#States/Propeties/Variables/Attributes
#1. static/class attributes/variables
#2. non static/instance attributes/variables

#Example of static variables/Attributes and methods/behaviors


# class Maths:
#     #static/class variable/attribute
#     pi = 3.14

#     #static methods/behaviors
#     @staticmethod
#     def findRectangleArea(length, width):
#         return length * width
    
#     @staticmethod
#     def welcome(name):
#         return f"welcome {name}"

#Note: how to access the static variable and method of the class?
#Answer: you can access either using class name or using class object.

# print(Maths.pi)
# print(Maths.findRectangleArea(20,10))
# print(Maths.welcome('Rakesh'))
    

#non static/instance variables/methods
#Note: to define instance attributes/variables, you need to use constructor function.

# class Maths:
#     #static/class variable/attribute
#     pi = 3.14

#     def __init__(self, name):
#         #instance variable/attribute/state
#         self.name = name

#     #static methods/behaviors
#     @staticmethod
#     def findRectangleArea(length, width):
#         return length * width
    
#     #instance/non-static method
#     def welcome(name):
#         return f"welcome {name}"
    
#Note: to access instance/non-static varibales/methods, you need to create the object.

#Without object
#print(Maths.name) #AttributeError: type object 'Maths' has no attribute 'name'


#Object: instance/reference of class which has methods(behaviors) and attribtues(states/properties)
#you can create n number of object of a class.

"""
how to create object?
syntax:

object/instance= ClassName()
"""

#Note: at the time of creating the class object, class constructor function automatically get called.

# class Maths:
#     #static/class variable/attribute
#     pi = 3.14

#     def __init__(self, name):
#         #instance variable/attribute/state
#         self.name = name

#     #static methods/behaviors
#     @staticmethod
#     def findRectangleArea(length, width):
#         return length * width
    
#     #instance/non-static method
#     def welcome(self):
#         return f"welcome {self.name}"
    
#     def __str__(self):
#         return f"Name is {self.name}"

# obj1 = Maths("Rakesh")
#print(obj1) #<__main__.Maths object at 0x000002810AF66270>

#Note: i don't want object to return this <__main__.Maths object at 0x000002810AF66270> instead i want it to print whatever i want.
#Note: to do this you need to override one internal method def__str__()

#After overriding the __str__ method
# print(obj1)
# print(obj1.name)
# print(obj1.welcome())
# obj2 = Maths()

#Constructor Function: it helps to create the object of the class.
# you can define one constructor one class
# At the time of creating class object, given constructor function gets called, if constructor function is not given then defualt constructor gets called by python internally.
#default constructor: def __init__()
#It is mendatory to have constructor function in class

#Example: 

# class Student:
#     #static/class Attribute/variabels
#     univerisity = "Chitkara"
#     universityAddress = "Rajpura Road, Punjab"

#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, City: {self.city}"


# student1 = Student("Rakesh", 34, "Noida")
# #print(student1)#<__main__.Student object at 0x000001FC84B86090>

# #First Way
# # print(student1.name)
# # print(student1.age)
# # print(student1.city)

# print(student1)



