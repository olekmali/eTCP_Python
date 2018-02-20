import socket

HOST, PORT = "localhost", 1200

text = str( input("Please enter a line of text to send: ") ).strip()

# SOCK_DGRAM is the socket type to use for UDP sockets
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setblocking(2.0)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
client.sendto( bytes( text + "\n", 'UTF-8' ), (HOST, PORT) )
back, addr = client.recvfrom(2048)
back = str( back, 'UTF-8' )

print( "Sent:     {}", format(text) )
print( "Received: {}", format(back) )

#data = input("Press ENTER to end the program")
