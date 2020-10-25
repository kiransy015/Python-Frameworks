str = 'Python and Selenium Automation'
s = str.replace(' ','$')
print(str)
print(s)

s = ''
for i in range(0,len(str)):
	if str[i]==' ':
		s = s+'$'
	else:
		s=s+str[i]
print(str)
print(s)
		
