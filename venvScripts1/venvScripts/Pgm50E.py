Ipstr = 'Python and Selenium Automation'
lst = Ipstr.split(' ')
str_temp=''

for s in lst:
	size = len(s)	
	for i in range(size-1,-1,-1):
		str_temp=str_temp+s[i]
	str_temp=str_temp+' '
print(str_temp)
		


