#Iterator: it is object which is used to traverse through sequence/collection(iterable) one by one.

list = [1,2,3,4,5,6]

numbers = iter(list)

# value = next(numbers)
# print(value) #1
# print(next(numbers)) #1
# print(next(numbers)) #2
# print(next(numbers)) #3
# print(next(numbers)) #4
# print(next(numbers)) #5
# print(next(numbers)) #6

#Iterator in 'for' loop

for i in list:
    print(i, end=" ")

for i in range(len(list)):
    print(list[i], end=" ")