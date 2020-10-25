from abc import ABC,abstractmethod


class Asample(ABC):

    @abstractmethod
    def x1(self):
        pass

    @abstractmethod
    def x2(self):
        pass

class Bsample(Asample):

    def x1(self):
        print('Running x1 in Bsample')

class Csample(Bsample):

    def x2(self):
        print('Running x2 in Csample')

ref = Csample()
ref.x1()
ref.x2()
