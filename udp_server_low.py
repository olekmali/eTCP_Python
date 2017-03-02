import socket

HOST, PORT = "", 60000

# Create a socket (SOCK_DGRAM is the socket type to use for UDP sockets)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

# serve forever
while 1:
    try:
        data, client_address = server.recvfrom(2048)
        data = data.decode()
        
        print format(client_address) + " has just contacted us with the following message: " + data
        data = data.upper()

        server.sendto(data.encode(), client_address)
    finally:
        # pass means NOOP, an emptuy instruction that may be required by the language syntax
        pass
