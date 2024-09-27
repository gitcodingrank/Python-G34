#1. return is like big bom whereas berak is like a small bom.

def printEvenNumbersFromList(nums):
    print("Starting of For Loop")
    for i in nums:
        if i%2==0:
            print(i)
            break
            # return i
    print("Ending of For Loop")

# print(printEvenNumbersFromList([1,2,3,4,5,6,7,8]))
printEvenNumbersFromList([1,2,3,4,5,6,7,8])

#2. return able to retun some expression whereas break can't do this.