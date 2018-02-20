import socket

HOST, PORT = "", 1200

# Create a socket (SOCK_DGRAM is the socket type to use for UDP sockets)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

# serve forever
while 1:
    try:
        data, client_address = server.recvfrom(2048)
        text = str( data, 'UTF-8')
        
        print( client_address , " has just contacted us with the following message: " + text )
        text = text.upper()

        server.sendto( bytes( text, 'UTF-8') , client_address)
    finally:
        # pass means NOOP, an empty instruction that may be required by the language syntax
        pass
