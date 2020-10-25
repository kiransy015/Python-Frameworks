from functools import reduce

# lst = [1,2,3,4,5,6,7,8,9]
#
# even = list(filter(lambda a:a%2==0,lst))
# print("Even nos :",even)
#
# sum = reduce(lambda a,b:a+b,even)
# print("Sum of Even nos :",sum)
#
# sqnos = list(map(lambda a:a*a,even))
# print("Square of Even nos :",sqnos)

num = (lambda x: "one" if x == 1 else( "two" if x == 2
                       else ("three" if x == 3 else "ten")))(3)
print(num)


num = (lambda x,y:"x" if x>y else "y" if x<y else "Both are same")(4,5)
print(num)
