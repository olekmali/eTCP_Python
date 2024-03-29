# More about program control structures - selection and repetition with ranges
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative, changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    x = 1
    print('More, changed to one')
print( "The number is "+str(x) )

N = int(input("Please enter an integer >=10: "))
for i in range(N):
    print(i, end=', ')
print( )

for i in range(2, N):
    print(i, end=', ')
print( )

for i in range(0, N, 3):
    print(i, end=', ')
print( )

for i in range(1,6):
    for j in range(1,6):
        print(i*j, end=',\t')
    print(  )
