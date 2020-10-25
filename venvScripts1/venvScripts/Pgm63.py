Size=int(input('Enter Size of List'))
a=[]
count=0
for i in range(0,Size):
    count=i
    try:
        value=int(input('Enter value for index '))
    except ValueError as e:
        print(e)
        i=count-1
    else:
        a.append(value)
print(a)