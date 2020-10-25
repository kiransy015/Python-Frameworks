#X union Y
print("---------------First approach-----------")
x={10,30,80,100}
y={40,60,10,30,200}

u=set()
for i in x:
	u.add(i)
for j in y:
	u.add(j)
print(x)
print(y)
print(u)

#X union Y
print("---------------Second approach-----------")
x={10,30,80,100}
y={40,60,10,30,200}

u=set()
u.update(x)
u.update(y)
print(x)
print(y)
print(u)


#X union Y
print("---------------Third approach-----------")
x={10,30,80,100}
y={40,60,10,30,200}

u=x.union(y)
print(x)
print(y)
print(u)

