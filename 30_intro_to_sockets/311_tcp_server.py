import socket
"""
This program is modified from an example (c)Python Software Foundation
that was posted at https://docs.python.org/3/library/socket.html
"""

HOST, PORT = "", 1200

count = 0

# Create a socket (SOCK_STREAM means a TCP socket)
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind( (HOST, PORT) )
    server.listen(1)
except OSError as msg:
    server.close()
    print('could not open socket')
    sys.exit(1)

# serve forever
while 1:
    try:
        request, client_address = server.accept()
        count = count + 1;

        request.sendall( bytes( "Welcome to the server.\r\nWhat is your name please?\r\n", 'UTF-8' ) )
        request.setblocking(True)
        # string.strip removes all leading and trailing white space including \r\n
        # number inside socket.recv(nnn) sets the maximum number of bytes to receive
        name = str( request.recv(1024), 'UTF-8' ).strip()
        print( name , " has just contacted us from " , client_address )
        
        data = "Nice to meet you " + name + ".\r\nYou are the " + str(count) + "th person who stopped by today\r\n"
        request.sendall( bytes( data, 'UTF-8' ) )
    finally:
        request.close()

