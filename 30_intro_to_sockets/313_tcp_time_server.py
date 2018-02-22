# TCP Time37 server
import socket
import time
import sys

HOST, PORT = "", 37
count = 0

def handle_client(socket, addr):
    # print("Time requested from ", client_address)
    nettime = int( time.time() + 2208988800 )
    data = nettime.to_bytes( 4, byteorder='big', signed=False)
    # print("Current time ", nettime, data)
    socket.sendall( data )

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind( (HOST, PORT) )
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
        # print("Problems with handling a client")
        pass
    finally:
        client_socket.close()
