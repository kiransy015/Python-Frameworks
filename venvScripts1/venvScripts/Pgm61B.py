class Sample:
    _a=10
    b=20
    print('_a =',_a)
    print('b =', b)

class Test(Sample):
    print('Printing Sample class b value in Test Class ',Sample.b)
    print('Printing Sample class _a value in Test Class ', Sample._a)