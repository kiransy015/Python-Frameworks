def deco(func):
    def inner(a,b):
        print("Before execution")
        func(a,b)
        print("After execution")
    return inner

@deco
def sum_of_two_nos(a,b):
    print("Inside the function")
    print(a+b)

sum_of_two_nos(1,2)




# def deco(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         func(a,b)
#     return inner
#
# @deco
# def divnos(a,b):
#     print(a/b)
#
# divnos(10,20)




















