from abc import ABC,abstractmethod

class Xsample(ABC):

    @abstractmethod
    def a1(self):
        pass

class Ysample(Xsample):

    def a1(self):
        print('Priniting a1 in Ysample class')
        
ref = Ysample()
ref.a1()
