# filter functionality
from functools import reduce


List = [1,2,3,4,5,6,7,8]
# evens = []
#
# def get_even_no(list):
#     for i in range(0,len(list)):
#         if list[i]%2==0:
#             evens.append(list[i])
#     print("Even nos :",evens)
#
# get_even_no(List)
#
#
# def even(n):
#     if n%2==0:
#         return True
#
# evens = list(filter(even,List))
# print("Even nos :",evens)
#
#
# evens = list(filter(lambda n:n%2==0,List))
# print("Even nos :",evens)



# Reduce functionality
# evens = list(filter(lambda n:n%2==0,List))
# print("Even nos :",evens)
# sum = reduce(lambda a,b:a+b,evens)
# print("Sum of even nos :",sum)


# map functionality
# square = list(map(lambda n:n*n,List))
# print("Square of nos :",square)
#
# div = list(map(lambda n:n/2,List))
# print("Division by 2 :",div)


