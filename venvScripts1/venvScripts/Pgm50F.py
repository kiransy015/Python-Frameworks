str = 'Python and Selenium Automation'
d={}
for s in str:
	if s in d:
		count=d.get(s)
		count=count+1
		d.update({s:count})
	else:
		d.update({s:1})
print(d)


