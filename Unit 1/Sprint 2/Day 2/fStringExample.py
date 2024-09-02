# #F-String: using this concept, you can directly use/embed variable and expression into the string.

# #life with f string

# # name = "Alice"
# # age = 45
# # #Hi, I'm Alice and I'm 45 years old.
# # print("Hi, I'm", name, "and I'm", age, "years old.")

# # #using F-String
# # print(f"Hi, I'm {name} and I'm {age} years old.")

# #Good Example 1: Create Dynamic Email

# # email = "
# # Dear Rakesh

# # I'm from Masai, where i will teach you about Python Programming Languange.

# # Best Regards
# # Anand Singh Yadav
# # "

# #Note: if you're creating multi-line string using double quatation mark then it will give you error then what is the solution for multi-line string: triple quatation marks("""  """)

# #triple quatation marks("""  """):
# # your python doesn't support multi-line comment, but you can use below method to keep multi line comment but this is not recommended.
# #You can use it for creating multi-line string.

# studentName = input("Enter Student Name: ")
# teacherOrg = input("Enter Teacher Organization: ")
# programmingLanguange = input("Ente Programming Language: ")
# teacherName = input("Enter Teacher Name: ")

# email = f"""
# Dear {studentName}

# I'm from {teacherOrg}, where i will teach you about {programmingLanguange} Programming Languange.

# Best Regards
# {teacherName}
# """

# print(email)

