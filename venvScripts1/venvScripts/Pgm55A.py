class Xdemo():
	def __init__(self):
		print('Running XDemo class constructor')
		
	def b1(self):
		print('Running b1 in XDemo')
		
class Ydemo(Xdemo):
	def __init__(self):
		Xdemo.__init__(self)
		print('Running YDemo class constructor')
		
	def b2(self):
		print('Running b2 in YDemo')
	
ref = Ydemo()