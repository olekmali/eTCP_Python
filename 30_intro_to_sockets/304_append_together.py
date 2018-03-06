import sys

"""
This program demonstrates how to append data together
and then how to split it using the first occurrence of an empty line
"""

buffer = b"";

print( "Enter several lines of text followed by EOF character - Ctrl+Z")
while 1:
    data = bytes( sys.stdin.readline(), 'UTF-8' ) # data chunk, e.g. from a TCP socket
    if not data:
        break
    buffer += data

print( "Data received:\r\n", buffer )

print( "\r\n\r\nAttempting to split the buffer using the first empty line:\r\n" )
header, page = buffer.split(b"\n\n", 1)      # use with console test
#header, body = buffer.split(b"\r\n\r\n", 1) # use with TCP socket and HTTP protocol test
print( "Header:\r\n",  str(header, 'UTF-8') )
print( "Page:\r\n",    str(page,   'UTF-8') )
