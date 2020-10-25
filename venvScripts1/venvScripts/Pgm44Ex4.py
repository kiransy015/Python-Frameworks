class KDemo:
    def display(self):
        print("b=",self.b)

    def __init__(self):
        self.b=100

ref = KDemo()
ref.display()