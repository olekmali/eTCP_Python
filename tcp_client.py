import socket

"""
This program is modified from an example (c)Python Software Foundation
that was posted at https://docs.python.org/2/library/socketserver.html
"""

HOST, PORT = "localhost", 60000

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    data = sock.recv(1024).strip()
    print data
    sock.sendall("Automated Client\r\n")
    data = sock.recv(1024).strip()
    print data
except:
    print "Socket connection error!"
finally:
    sock.close()
