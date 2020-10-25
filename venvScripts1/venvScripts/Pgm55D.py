class Organization():
	Company = 'Nokia'
	
class Employees(Organization):

	
	def __init__(self,EmployeeName):
		self.EmpName = EmployeeName
		
	def CreateLeave(self,StartDate,EndDate):
		print('Applying Leave by Employee :',self.EmpName," ,Organization ",Organization.Company)
		Manager.ApproveLeave(self,StartDate,EndDate)

	def ModifyLeave(self,StartDate,EndDate):
		print('Modifying Leave by Employee :',self.EmpName," ,Organization ",Organization.Company)
		Manager.ApproveLeave(self,StartDate,EndDate)
		
	def CancelLeave(self,StartDate,EndDate):
		print('Cancelling Leave by Employee :',self.EmpName," ,Organization ",Organization.Company)
		Manager.ApproveLeave(self,StartDate,EndDate)

		
class Manager(Employees):
	# def __init__(self):
    #     print('Employee Manager')
	
	def __init__(self,EmployeeName):
		Employees.__init__(self,EmployeeName)
		
	def ApproveLeave(self,StartDate,EndDate):
		print('Approving Leave for Employee :',self.EmpName," ,Organization ",Organization.Company)
		
class TeamLead(Employees):
	def __init__(self,EmployeeName):
		Employees.__init__(self,EmployeeName)

class Engineer(Employees):
	def __init__(self,EmployeeName):
		Employees.__init__(self,EmployeeName)		
	
print('---------------By Employee------------')	
E1 = Engineer('Ram')
E1.CreateLeave("01/02/2019","01/24/2019")
E1.ModifyLeave("01/02/2019","01/24/2019")
E1.CancelLeave("01/02/2019","01/24/2019")
print('---------------By TeamLead------------')	
TL1 = TeamLead('Sam')
TL1.CreateLeave("01/02/2019","01/24/2019")
TL1.ModifyLeave("01/02/2019","01/24/2019")
TL1.CancelLeave("01/02/2019","01/24/2019")
print('---------------By Manager------------')	
M1 = Manager('Jam')
M1.CreateLeave("01/02/2019","01/24/2019")
M1.ModifyLeave("01/02/2019","01/24/2019")
M1.CancelLeave("01/02/2019","01/24/2019")




	
