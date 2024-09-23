#Function: It is a block of code related to specific functionality.

#Why Function?

# num1 = 5
# count = 0
# for i in range(1, num1+1):
#     if num1%i==0:
#         count+=1
# if count==2:
#     print("Prime Numbers")
# else:
#     print("Not Prime Number")

# a, b = 45, 50
# print(a+b)

# value = input("Enter Value: ")
# print("Enter Value is:", value)

# c = 6
# print(c**2)

# num2 = 6
# count = 0
# for i in range(1, num2+1):
#     if num2%i==0:
#         count+=1
# if count==2:
#     print("Prime Numbers")
# else:
#     print("Not Prime Number")

# result = 2**3 + 5//3 + 5 * 5
# print(result)

# num3 = 7

# count = 0
# for i in range(1, num3+1):
#     if num3%i==0:
#         count+=1
# if count==2:
#     print("Prime Numbers")
# else:
#     print("Not Prime Number")

#Without using function, you're having to write duplicate code, there is no reusability but with the help of function we can reuse the code.


#Declaration of Function:
"""
syntax:
def functionName():
    #function body
"""

#Declared function with name "add"
# def add():
#     num1 = 45
#     num2 = 15
#     print(num1 + num2)

#How to use/call created function? - with helf of its name
#syntax: functionName()
#Calling the function means executing the function.


# add()
# add()
# add()
# add()
# add()
# add()

#Example 2:

#Declared three different function with name: playMusic(), stopMusic(), loopMusic()
# def playMusic():
#     print("Music started playing..")

# def stopMusic():
#     print("Music stopped playing..")

# def loopMusic():
#     print("Music started looping..")


#calling created function:

# playMusic()
# loopMusic()
# stopMusic()

#Example 3:

# def welcome():
#     print("Welcome Rakesh! to Chitkara University")


# welcome()
# welcome()

#Once above functions are static function therefore whenever you call these function they return whatever written inside their body.

#How to create dynamic function - to create dynamic function you need to understand about function parameters and function arguments.

#function parameters - they are just function variables that you take at the time function declaration.

# def playMusic(music):
#     print(f"{music} started playing...")


#calling the above function

# music1 = "abc..." 
#Function Arguments: it is just a actual/original data/value that you're passing to the function at the time calling.

# playMusic(music1)
# playMusic("xyz...")


def add(a, b):
    print(a+b)



add(3,2) 
add(10,20)
add(13,17) 


