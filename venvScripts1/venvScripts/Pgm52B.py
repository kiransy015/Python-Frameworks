#X intersection Y
print("---------------First approach-----------")
x={10,30,80,100}
y={40,60,10,30,200}

i = x.intersection(y)
print(x)
print(y)
print(i)


print("---------------Second approach-----------")
x={10,30,80,100}
y={40,60,10,30,200}

for k in x:
	if k in y:
		i.add(k)
print(x)
print(y)
print(i)
