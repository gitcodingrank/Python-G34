#Logical Operator: it is the best choice if you've more than one related/dependent conditons or non related/independent conditons.

#There are following type of logical Operators:
#1. and 
#2. or
#3. not

#1. and:  if all the given conditions are true then the entire expression will be true if any of the condition is false then entire expression will be false.

"""
syntax:
condition1 and condtion2 and condition3 and condition4

A        B       A and B
True    True       True
True    False      False
False   True       False
False   False      False

Note: and operator always find its next True, if anywhere it finds False then it makes the entire expression as False.

"""

#Problem 2: user will enter username and password you need to print based on below data.
# if username and password is correct print "Logged In Succcessfully"
# if incorrect print "Invalid Username" or "Inavalid Password" according to the situation.

#Without Using Logical and Operator:

username= input("Enter Username: ")
password= input("Enter Password: ")

# if username == "admin":
#     if password == "12345":
#         print("Logged In Successfully")
#     else:
#         print("Invalid Password")
# else:
#     print("Invalid Username")

#Using Logical Operator

if username == "admin" and password == "12345":
    print("Logged In Successfully.")
else:
    print("Invalid Credential")