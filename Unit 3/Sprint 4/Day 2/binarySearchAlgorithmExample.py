#Binary Search Algorithm: It is an efficient algorithm that on sorted list and divides the search interval in two halves, if the target element is greater than the mid element, then you search in right half, otherwise you search in left half.


#How does it work?
#1. Intial Setup: Start with sorted list
#2. Divide the Search Interval: it divides the list by its search interval into two halves, and you will get the mid element index
#3. Check for target: it checks if the target is greater then mid element then check in right half otherwise check in left half.


"""
list: [ 1,2,3,6,8,9,10,23]
target = 3

low, high = 0, len(list)-1
while (low<=high):
    mid = (low+high)//2
    if list[mid]==target:
        print(mid)
        break
    elif target < list[mid]:
        high = mid - 1
    else:
        low = mid + 1

"""

list = [1,2,3,6,8,9,10,23]
target = 2
bag = -1
low, high = 0, len(list)-1
while (low<=high):
    mid = (low+high)//2
    if list[mid]==target:
        bag = mid
        break
    elif target < list[mid]:
        high = mid - 1
    else:
        low = mid + 1

print(bag)