#Generate a multiplication table (1-10) for numbers 1 through 5

# for table in range(1,6):
#     for number in range(1,11):
#         print(table,"*",number,"---",table*number)


#Print all pairs of numbers (i, j) where 1 ≤ i, j ≤ 3.

# for i in range(1, 3):
#     for j in range(1,4):
#         print(f"({i}, {j})", end=" ")
#     print()

#Print a right-angled triangle of stars with 5 rows.

""""
*
* *
* * *
* * * *
* * * * *
"""

# for i in range(1,6):
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print()

""""
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
********** 
"""

# for row in range(1,11):
#     if (row==1 or row==10):
#         for star1 in range(1,11):
#             print('*',end='')
#     else:
#         for star2 in range(1,11):
#             if star2 == 1 or star2 == 10:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#     print()


"""
1
*
1 2
* *
1 2 3
* * *
1 2 3 4
* * * *
1 2 3 4 5
* * * * *
"""

# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print()

"""
   *
  ***
 *****
*******
"""

rows = 21

for i in range(1,rows+1):
    # for space
    for space in range(rows-i):
        print(' ', end='')
    # for start
    for star in range(2*i-1):
        print('*', end='')
    print()

"""
   *
  ***
 *****
  ***
   *
"""