#Probblem 1: create a program to check a letter is vowel or consonant. 
#vowels: a,e,i,o,u
#Solution: using if elif else statemnt

#if statement: best when you've one condition and want to test for true condition
#if else statement: best for one condtion if you want to test particular condition for both true and false.
#if elif else statment: best when you've more than one condition.

# letter = input("Enter Any Alphabet: ")

# if letter == "a":
#     print("Vowel")
# elif letter == "e":
#     print("Vowel")
# elif letter == "i":
#     print("Vowel")
# elif letter == "o":
#     print("Vowel")
# elif letter == "u":
#     print("Vowel")
# else:
#     print("Consonant")

#Problem 2: user will enter username and password you need to print based on below data.
# if username and password is correct print "Logged In Succcessfully"
# if incorrect print "Invalid Username" or "Inavalid Password" according to the situation.

#Note: when your one condition is connected/dependent on another condition then in this case, you can proceed with nest if else statement.

#Nested if statement: when one condition is connected to another condition
#if inside another if

"""
syntax:

if condition1:
    #once condition1 is true
   if condition2:
        #once condition2 is true
        if condition3:
        #once condition3 is true
        else:
            #once condition3 is false
    else:
       #once condition2 is false  
else:
    #once condition1 is false

"""

# username= input("Enter Username: ")
# password= input("Enter Password: ")

# if username == "admin":
#     if password == "12345":
#         print("Logged In Successfully")
#     else:
#         print("Invalid Password")
# else:
#     print("Invalid Username")


#Problem 2: print "Selected for Job" according to below criteria
#degree="mca", percentage>=80, isDSA=true

# degree = "mca"
# percentage = 80
# isDSA = True

# if degree == "mca":
#     if percentage >= 80:
#         if isDSA:
#             print("Selected for Job")
#         else:
#             print("Have not met the DSA Criteria")
#     else:
#         print("Have not met the perentage Criteria")
# else:
#     print("Invalid Degree")

#Problem 3: print "Do Celebration" according to below criteria
#isFriday=true, isClass=false, isAssignment=false

# isFriday = True
# isClass = False
# isAssignment = False

# if isFriday:
#     if isClass == False:
#         if isAssignment == False:
#             print("Do Celebration")
#         else:
#             print("There is assignment")
#     else:
#         print("Have Class")
# else:
#     print("Not Friday")


#Question: if you have 10 connected or dependent condtions then still you can write the solution but you will end with less readable and harder to maintain.

# if isFriday:
#     if isClass == False:
#         if isAssignment == False:
#             print("Do Celebration")
#             if isAssignment == False:
#                 print("Do Celebration")
#                 if isAssignment == False:
#                     print("Do Celebration")
#                     if isAssignment == False:
#                         print("Do Celebration")
#                     else:
#                         print("There is assignment")
#                 else:
#                     print("There is assignment")
#             else:
#                 print("There is assignment")
#         else:
#             print("There is assignment")
#     else:
#         print("Have Class")
# else:
#     print("Not Friday")

#Solution is Logical Operator:




