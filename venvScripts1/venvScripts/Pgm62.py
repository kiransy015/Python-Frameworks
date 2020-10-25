#IndexError
print('-----------------#IndexError#-------------------')
print('---------Execution Started----------')
a=[30,40,10,50,90]
try:
    print('Running try block')
    print(a[100])
except IndexError as e:
    print(e)
    print('Running except block')
else:
    print('Running else block')
finally:
    print('Running finally block')
print('---------Execution Ended----------')


#TypeError
print('-----------------#TypeError#-------------------')
print('---------Execution Started----------')
a=(30,40,10,50,90)
try:
    print('Running try block')
    del a[0]
except TypeError as x:
    print(x)
    print('Running except block')
else:
    print('Running else block')
finally:
    print('Running finally block')
print('---------Execution Ended----------')

#Handling Exception in Generic way
print('-----------------#Handling Exception in Generic way#-------------------')
print('---------Execution Started----------')
a=[30,40,10,50,90]
try:
    print('Running try block')
    del a[100]
except Exception as x:
    print(x)
    print('Running except block')
else:
    print('Running else block')
finally:
    print('Running finally block')
print('---------Execution Ended----------')


#How to handle multiple exceptions
print('-----------------#How to handle multiple exceptions#-------------------')
print('---------Execution Started----------')
a=[30,40,10,50,90]
x=10
y=2
try:
    z=x/y
    print(a[100])
except ZeroDivisionError as e:
    print('-----------------------------')
    print(e)
    print('-----------------------------')
except IndexError as e:
    print('-----------------------------')
    print(e)
    print('-----------------------------')
else:
    print(z)
print('---------Execution Ended----------')












