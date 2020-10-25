#Set is unordered DataStructure and it doesnot allow duplicate elements
b={20,40,10,50,90,10,60,10}
print(b)

#Adding elements into a set
b.add(200)
print(b)


#Merging elements of 2 different sets
b={20,40,10,50,90}
c={10,30,40}
b.update(c)
print("After merge :",b)
print(c)

#Removing elements from a set
b.remove(40)
print("After remove :",b)

#Updating elements
b.remove(30)
b.add(80)
print("After update :",b)


#Set doesnot support indexing
print(b[0])



