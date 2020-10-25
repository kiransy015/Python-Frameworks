# # A generator function that yields 1 for first time,
# # 2 second time and 3 third time
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
#
#
# # Driver code to check above generator function
# for value in simpleGeneratorFun():
#     print(value)


# # A Python program to demonstrate use of
# # generator object with next()
#
# # A generator function
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
#
#
# # x is a generator object
# x = simpleGeneratorFun()
#
# # Iterating over the generator object using next
# print(x.__next__());  # In Python 3, __next__()
# print(x.__next__());
# print(x.__next__());



import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))





















