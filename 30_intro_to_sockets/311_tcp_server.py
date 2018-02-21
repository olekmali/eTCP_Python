# TCP server example for IPv4
import socket
"""
This program is modified from an example (c)Python Software Foundation
that was posted at https://docs.python.org/3/library/socket.html
"""

HOST, PORT = "", 1200
count = 0

def handle_client(socket, addr):
    # make sure that the global variable count is used 
    # instead of creating a temporary local variable with the same name
    global count
    count = count + 1;

    try:
        socket.sendall( bytes( "Welcome to the server.\r\nWhat is your name please?\r\n", 'UTF-8' ) )
        # We are talking to humans -- don't just read data that already arrived, wait for the reply
        socket.setblocking(True)
        socket.settimeout(10.0)
        # string.strip removes all leading and trailing white space including \r\n
        # number inside socket.recv(nnn) sets the maximum number of bytes to receive
        name = str( socket.recv(1024), 'UTF-8' ).strip()
        print( name , " has just contacted us from " , addr )
        # prepare the reply
        data = "Nice to meet you " + name + ".\r\nYou are the " + str(count) + "th person who stopped by today. Bye now!\r\n"
        socket.sendall( bytes( data, 'UTF-8' ) )
    except socket.Timeouterror:
        socket.sendall( bytes( "You are not very talkative today. Bye now!\r\n", 'UTF-8' ) )
    # Note that we only handled the timeout exception. Anything else will be passed to the place this function was called

try:
    # Create a socket (SOCK_STREAM means a TCP socket)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to a particular port number (and perhaps to a network interface - HOST)
    server.bind( (HOST, PORT) )
    # Start the server
    server.listen(1)
except OSError as msg:
    server.close()
    print("could not open the server socket")
    sys.exit(1)

# serve forever
while 1:
    try:
        client_socket, client_address = server.accept()
        handle_client(client_socket, client_address)
    except:
        pass
    finally:
        client_socket.close()
