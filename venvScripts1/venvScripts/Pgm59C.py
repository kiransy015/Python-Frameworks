from abc import ABC,abstractmethod

class Dsample(ABC):

    @abstractmethod
    def P1Sample(self):
        pass

    def P2Sample(self):
        print('Running P2 in Dsample')

class ESample(Dsample):

    def P1Sample(self):
        print('Running P1 in Esample')

ref = ESample()
ref.P1Sample()
ref.P2Sample()