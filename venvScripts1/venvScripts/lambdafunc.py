# https://www.geeksforgeeks.org/overuse-of-lambda-expressions-in-python/


# ************************ filter with lambda ************************
lst = [1,2,3,4,5,6,7]
evens = []

for i in lst:
    if i%2==0:
        evens.append(i)
print("Even nos :",evens)

lst = [1,2,3,4,5,6,7]
def even(n):
    if n%2==0:
        return True

evens = list(filter(even,lst))
print("Even nos :",evens)

lst = [1,2,3,4,5,6,7]
evens = list(filter(lambda n:n%2==0,lst))
print("Even nos :",evens)


# ************************ reduce with lambda ************************
from functools import reduce

lst = [1,2,3,4,5,6,7]
evens = list(filter(lambda n:n%2==0,lst))
print("Even nos :",evens)

sum = reduce(lambda a,b:a+b,evens)
print("Sum of even nos :",sum)


# ************************ map with lambda ************************

lst = [1,2,3,4,5,6,7]
evens = list(filter(lambda n:n%2==0,lst))
print("Even nos :",evens)

sqrno = list(map(lambda n:n*n,evens))
print("Square nos :",sqrno)


# ************************ greater of two nos ************************
num = (lambda x,y:"x" if x>y else "y" if x<y else "Both are same")(4,5)
print(num)
