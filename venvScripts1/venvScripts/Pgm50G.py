str = 'Python and Selenium Automation'
lst = str.split(' ')
print("Size ",len(lst))
str_temp=''
for i in range(len(lst)-1,-1,-1):
	str_temp=str_temp+lst[i]+' '
print(str_temp)

	

