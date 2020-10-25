 str = 'Python and Selenium Automation and Training'
lst = str.split(' ')
str_temp=''
for s in lst:
	if s=='and':
		str_temp=str_temp+" "+"or"
	else:
		str_temp=str_temp+" "+s
print('Before :',str)
print('After :',str_temp)

		
