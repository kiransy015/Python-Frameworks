class Ademo():

    val =10

    @staticmethod
    def info():
        print('Running class method')

    def x1(self):
        print('Running x1 in Ademo class')

    def x2(self):
        print('Running x2 in Ademo class')

class Bdemo(Ademo):
    def x3(self):
        print('Running x3 in Bdemo class')

    def x4(self):
        print('Running x4 in Bdemo class')

print('--------------------------')
ref = Ademo()
ref.x1()
ref.x2()
ob = Bdemo()
ob.x1()
ob.x2()
ob.x3()
ob.x4()
ob.info()
print('Class variable value :',ob.val)