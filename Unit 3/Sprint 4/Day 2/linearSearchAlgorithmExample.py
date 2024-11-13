#Linear(Sequential) Search: it is simple algorithm that sequentially checks every element in the list, if element matches with target element then it returns/prints that element, if it reaches at end of list/not found, then you can return appropriate msg.


#How does it work?
#1. Initial Setup: Start with sorted and unsorted list.
#2. Compare with Target Element: It compares with each element in sequence if any element matches with target element then it returns that element otherwise it returns some other msg.


"""
Example:

Analogy 1
list = [1,23,4,6,7,3,8,10]
target = 7
Round 1: goto to 1 and compare target == list[0]
Round 2: goto to 23 and compare target == list[1]
Round 3: goto to 4 and compare target == list[2]
Round 4: goto to 6 and compare target == list[3]
Round 5: goto to 7 and compare target == list[4] - return index

Analogy 2
list = [1,23,4,6,7,3,8,10]
target = 11
Round 1: goto to 1 and compare target == list[0]
Round 2: goto to 23 and compare target == list[1]
Round 3: goto to 4 and compare target == list[2]
Round 4: goto to 6 and compare target == list[3]
Round 5: goto to 7 and compare target == list[4]
Round 6: goto to 3 and compare target == list[5]
Round 7: goto to 8 and compare target == list[6]
Round 7: goto to 10 and compare target == list[7]

at last you can return msg - "not found", "-1", False

"""


#Example 1: consider below list, and create function that takes list and target element and returns the arget element index, if its not found then return -1
# list = [1,23,4,6,7,3,8,10]
# target = 11


# def linearSearch(list, target):
#     for i in range(len(list)):
#         if list[i] == target:
#             return i
#     return -1

# print(linearSearch(list, target))



