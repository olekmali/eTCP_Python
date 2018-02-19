import socket
#import sys

"""
This program is modified from an example (c)Python Software Foundation
that was posted at https://docs.python.org/2/library/socketserver.html
"""

HOST, PORT = "localhost", 60000

data = raw_input("Please enter a line of text to send: ")
#print "Please enter a line of text to send: "
#data = sys.stdin.readline()

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
sock.sendto(data + "\n", (HOST, PORT))
received = sock.recv(2048)

print "Sent:     {}".format(data)
print "Received: {}".format(received)

#data = raw_input("Press ENTER to end the program")
