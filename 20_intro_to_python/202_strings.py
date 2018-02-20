# Basic operations on strings
print("Hello Python world!")

var1 = "Hello Python world!"
print(var1)

var2 = 3
print(var1 + " " + str(var2) + " times in a row.")

var1 = "this variable is now reused."
print(var1.title())

print( "This 'is' a string1" )              # \' can be avoided
print( 'This "is" a string2' )              # \" can be avoided
print( "This is \\na string3" )             # \\ works
print( 'This is \\na string4' )             # \\ works
print( "This is \na string5" )              # \n works
print( 'This is \na string6' )              # \n works
print( r"This is \na string7" )             # raw string - no escape sequences
print( r'This is \na string8' )             # raw string - no escape sequences
print( """This is a triple " string9""" )
print( """This is a triple \" string10""" ) # \ works as an escape character
print( """This is
a multi-line 
string11""" )

print( "double-quoted string behaves like a string class".title() )
print( 'single-quoted string behaves like a string class'.title() )

word = 'Python'
"""
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5   6
 -6  -5  -4  -3  -2  -1
"""
print( word[0] )
print( word[5] )
print( word[-1] )   # prints w[last char]
print( word[2:4] )  # prints w[2] w[3] and not w[4]
print( word[2:] )
print( word[:2] )
print( word[-2:] ) # prints last two characters
another = word[-2:]
print( another )
