# bASIC Program control structures
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a+b
print( )
print( )

a, b = 0, 1
while b < 100:
    print(b, end=', ')
    a, b = b, a+b
print( )
print( )
