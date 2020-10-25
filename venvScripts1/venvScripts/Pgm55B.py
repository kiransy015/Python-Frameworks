class XDemo():
	def __init__(self,arg1):
		print('Running XDemo class Constructor')
		
	def b1(self):
		print('Running b1 in XDemo')
		
class YDemo(XDemo):
	def __init__(self):
		XDemo.__init__(self,20)
		print('Running YDemo class Constructor')
		
	def b2(self):
		print('Running b2 in YDemo')
		
ref = YDemo()
