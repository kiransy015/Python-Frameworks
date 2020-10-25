# a=[]
# size = int(input('Enter size of list :'))
# for i in range(0,size):
# 	a.append(int(input('Enter list value :')))
# print(a)
#
# total=0
# for i in range(0,size):
#     total = total+a[i]
#
# print('Sum of all elements in the list :',total)


size = int(input('Enter size of list :'))
total = 0
for i in range(0,size):
    total = total+int(input('Enter the value :'))
    print('Sum of all values read :',total)

