class Sample:
    b = 10
    __a=30
    print('__a=', __a)
    print('b=',b)

class Test(Sample):
    print('Printing Sample Class b value in Test Class =', Sample.b)
    print('Printing Sample Class a value in Test Class =', Sample.__a)


#__a=30
#print('__a =',__a)