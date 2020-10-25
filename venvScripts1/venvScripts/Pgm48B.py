lst = [10,20,30,40,50,40]

print('Before :',lst)
for i in lst:
	if lst.count(i)>1:
		lst.remove(i)
print('After :',lst)
		