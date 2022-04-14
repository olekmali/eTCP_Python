# UDP client example for IPv4
import socket

HOST, PORT = "localhost", 1200

text = str( input("Please enter a line of text to send: ") ).strip()

# SOCK_DGRAM is the socket type to use for UDP sockets
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
client.sendto( bytes( text + "\n", 'UTF-8' ), (HOST, PORT) )
# servers are machines, they should reply in a blink of an eye much less than 2 seconds
# client.settimeout(None) # None means block/wait forever
client.settimeout(2.0)
back, addr = client.recvfrom(2048)
back = str( back, 'UTF-8' )

print( "Data Sent: ", format(text) )
print( "Received:  ", format(back) )
