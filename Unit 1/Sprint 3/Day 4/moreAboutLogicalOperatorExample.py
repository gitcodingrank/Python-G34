#Logical Operator: 
#1. Best Alternative of nested if else statmeent(once we have more than one dependent conditons)
#2. it makes your code concise, easy to maintatin, and easy to understand.


#There are following types of Logical Operators:
#1. and logical operator
#2. or logical operator
#3. not logical operator


#1. and logical operator: in the case of logical operator, if the all given conditions are true then entire expression will be true if any of the condition is false then entire expression will be false.

#best for dependent conditions

"""
syntax:
condition1 and condition2 and condition3 and condition4


Case 1: 
conditon1 = True
conditon2 = True
conditon3 = True
conditon4 = True

result = condition1 and condition2 and condition3 and condition4
result is True

Case 2: 
conditon1 = False
conditon2 = True
conditon3 = True
conditon4 = True

result = condition1 and condition2 and condition3 and condition4
result is False

Case 3: 
conditon1 = False
conditon2 = False
conditon3 = True
conditon4 = False

result = condition1 and condition2 and condition3 and condition4
result is False


Table:

  A     B      C               A and B and C
True  True    True             True and True and True : [True]
True  True    False            True and True and False :[False]
True  False    False           True and False and False :[False]
False  False    False          False and False and False :[False]

Note: and opeartor always finds its next True, if anywhere it finds False entire expression will be False.
"""


#Example: Print Do marriege according to following criteria:
#Gender:  Male, Age>=21, graduate: True,  isJob: True

#Without Logical Operator: 

# gender = "male"
# age = 23
# isGraduate = True
# isJob = True

# if gender=="male":
#     if age>=21:
#         if isGraduate:
#             if isJob:
#                 print("Do Marriege.")
#             else:
#                 print("Sorry, You don't have job.")
#         else:
#             print("Sorry, do Graduation first.")
#     else:
#         print("Age is below 21")
# else:
#     print("Gender is not matching.")

#Above code is harder to maintain and dificult to understand then to make this code more readable and easy to maintain let's proceed with logical operator.
#Logical and operator in above problem is the best choice.

#Using logical and operator:

# gender = "male"
# age = 23
# isGraduate = True
# isJob = True

# if gender == "male" and age>=21 and isGraduate and isJob:
#     print("Do Marriege")
# else:
#     print("You're not eligiblle for marriege.")



#Logical or Operator: In this case if among many conditions if any of the condition is true then entire expression will be True, if none of the condition is True then entire expresssion will be False.

#best for independent conditions

"""
syntax:

conditon1 or condition2 or condition3 or condition4

Note: or operator it always finds its first True, if it doesn't find the True anywhere then it will make entire expression as False.

Case 1: 
conditon1 = True
conditon2 = True
conditon3 = True
conditon4 = True

result = condition1 or condition2 or condition3 or condition4
result is True

Case 2: 
conditon1 = True
conditon2 = False
conditon3 = True
conditon4 = False

result = condition1 or condition2 or condition3 or condition4
result is True

Case 2: 
conditon1 = False
conditon2 = False
conditon3 = False
conditon4 = False

result = condition1 or condition2 or condition3 or condition4
result is False


Table:


Table:

  A     B      C               A or B or C
True  True    True             True or True or True : [True]
True  True    False            True or True or False :[True]
True  False   False            True or False or False :[True]
False  False  False            False or False or False :[False]

"""


#Example 1: check a letter is vowel or consonant:

# letter = 'a'

#Without Logial Operator:

# if letter =='a':
#     print("Vowel")
# elif letter == 'e':
#     print("Vowel")
# elif letter == 'i':
#     print("Vowel")
# elif letter == 'o':
#     print("Vowel")
# elif letter == 'u':
#     print("Vowel")
# else:
#     print("Consonant")


#Logial or operator:

# letter = 't'

# if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
#     print("Vowel")
# else:
#     print("Consonant")


#Example: Print Do marriege according to following criteria:
#Gender:  Male, Age>=21, graduate: True,  isJob: True
#Gender:  Female, Age>=21, graduate: True,  isJob: True

#Solution
gender = "male"
age = 23
isGraduate = True
isJob = True

# if (gender == "male" and age>=21 and isGraduate and isJob) or (gender == "feamle" and age>=21 and isGraduate and isJob):
#     print("Do Marriege")
# else:
#     print("You're not eligible")

# if (gender == "male"  or gender == "feamle") and age>=21 and isGraduate and isJob:
#     print("Do Marriege")
# else:
#     print("You're not eligible")


#Exmaple : print DO party if you have any of below condition:
#isFriday: True
#isRaining: True
#isAssignment: False


# isFriday = True
# isRaining = False
# isAssingment = False

# if isFriday or isRaining or isAssingment==False:
#     print("Do Party")
# else:
#     print("No Party")

#3. not opeartor: it is used to negate the condtion value, if condition is True then this opeartor will make it false, if the value is True then this will make it False.

"""
syntax:
not condition

Note: not operator is used to negate the value.

"""

#Example 1: Print Do Party not day must not be Friday.

# isFriday = False

# if not isFriday:
#     print("Do Party")
# else:
#     print("Not Party")

#Exmaple : print DO party if you have any of below condition:
#isFriday: True
#isRaining: True
#isAssignment: False

# isFriday = False
# isRaining = False
# isAssingment = False

# if isFriday or isRaining or not isAssingment:
#     print("Do Party")
# else:
#     print("No Party")




