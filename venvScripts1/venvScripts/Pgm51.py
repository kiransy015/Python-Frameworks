#Tuple will allow duplicate values
a=(20,40,50,60,40)
print(a)
#Tuples can be accessed using index value
print(a)
print(a[0])


## index and count
print(a.index(60))
print(a.count(40))

#From a tuple u cant remove elements
del a[0]
print(a)

