class Circle:
	pi = 3.142
	def __init__(self,r):
		self.radius = r
		
	def AreaofCircle(self):
		area = Circle.pi*self.radius*self.radius
		print("Area of a Circle :",area)
		
	def CircofCircle(self):
		circ = 2*Circle.pi*self.radius
		print("Circumference of a Circle :",circ)
		
	def DiameterofCircle(self):
		diameter = 2*self.radius
		print("Diameter of a Circle :",diameter)
		
print('------------------------------')
c1 = Circle(3.5)
c1.AreaofCircle()
c1.CircofCircle()
c1.DiameterofCircle()
print('------------------------------')
c2 = Circle(4.5)
c2.AreaofCircle()
c2.CircofCircle()
c2.DiameterofCircle()
print('------------------------------')
c3 = Circle(5.5)
c3.AreaofCircle()
c3.CircofCircle()
c3.DiameterofCircle()