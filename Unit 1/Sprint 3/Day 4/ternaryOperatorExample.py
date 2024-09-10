#Ternary Operator: it is used to use conditonal statement in concise manner or you can say it is the shorthand way of if else statement.

"""
syntax:

[Print Statement if True] if condition else [Print Statement if False]

Examples: 

age > = 18 - print "Eligible for vote."

age = 23

print("Eligible for Vote") if age>=21 else print("Not Eligible for vote")

"""

#Example: 

# age = 17

#Case 1:
# print("Eligible for Vote") if age>=21 else print("Not Eligible for vote")

#Case 2: you can also return the statement.

# result = "Eligible for Vote" if age>=21 else "Not Eligible for vote"
# print(result)

#More Concise way:

# print("Eligible for Vote" if age>=21 else "Not Eligible for vote")


#Example 2: Ternary Operator with Logical Operator:


isFriday = False
isRaining = False
isAssingment = False

# if isFriday or isRaining or not isAssingment:
#     print("Do Party")
# else:
#     print("No Party")


#Try above solution using ternary operator:
# print("Do Party") if isFriday or isRaining or not isAssingment else print("No Party")

# print("Do Party" if isFriday or isRaining or not isAssingment else "No Party")