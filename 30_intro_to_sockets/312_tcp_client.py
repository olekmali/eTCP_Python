# TCP client example for IPv4
import socket
"""
This program is modified from an example (c)Python Software Foundation
that was posted at https://docs.python.org/2/library/socketserver.html
"""

HOST, PORT = "localhost", 1200

# Create a socket (SOCK_STREAM means a TCP socket)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server and send data
try:
    client.connect( (HOST, PORT) )
    data = client.recv(1024)
    text = str( data, 'UTF-8' ).strip()
    print( text )
    client.sendall( bytes( "Automated Client\r\n", 'UTF-8' ))
    data = client.recv(1024)
    text = str( data, 'UTF-8' ).strip()
    print( text )
except:
    print( "Socket connection error!" )
finally:
    client.close()
