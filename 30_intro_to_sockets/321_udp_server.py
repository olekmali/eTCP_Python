# UDP server example for IPv4
import socket
import sys

HOST, PORT = "", 1200

try:
    # Create a socket (SOCK_DGRAM is the socket type to use for UDP sockets)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to a particular port number (and perhaps to a network interface - HOST)
    server.bind((HOST, PORT))
except OSError as msg:
    print("could not open the server socket")
    sys.exit(1)

# serve forever
while True:
    try:
        data, client_address = server.recvfrom(2048)
        text = str( data, 'UTF-8')
        print( client_address , " has just contacted us with the following message: " + text )
        text = text.upper()
        server.sendto( bytes( text, 'UTF-8') , client_address)
    except:
        # We handle any potential errors here instead of stopping the program
        # pass means NOOP, an empty instruction that may be required by the language syntax
        pass
    finally:
        pass
