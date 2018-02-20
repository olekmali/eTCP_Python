# Operations on numbers
print( 5+3 )
print( 5-3 )
print( 5*3 )
print( 5/3 )    # always floating point division
print( 5**3 )   # to the power of 
print( 5//3 )   # "floor division" simply rounds the result ALWAYS down, NOT TOWARSD zero
print( 5%3 )    # for >0 it behaves as we always expect it to do
print()

# look closely what happens when floating point arguments are used, does not look not very precise!
print( 16%3 )
print( 16.1%3 )
print( 16%3.1 )
print( 16.1%3.1 )
print()

# look closely what happens when negative arguments are used, remember the "floor division" rule
print( 16%3 )
print( (-16)%3 )
print( 16%(-3) )
print( (-16)%(-3) )
print( 16//3 )
print( (-16)//3 )
print( 16//(-3) )
print( (-16)//(-3) )
print()

print( -5**2 )          # obvious but reminded just in case ;-)
print( (-5)**2 )
print( (1j * 1j) )      # complex numbers are here
print()

print( round(5/3, 4) )  # rounds a floating point number to n decimal digits

# Note: there are two additional class-based numerical data types: Decimal and Fraction
