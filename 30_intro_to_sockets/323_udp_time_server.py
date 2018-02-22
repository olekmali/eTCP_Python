# UDP Time37 server
import socket
import time
import sys

HOST, PORT = "", 37

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
except OSError as msg:
    print("could not open the server socket")
    sys.exit(1)

# serve forever
while 1:
    try:
        data, client_address = server.recvfrom(2048)
        # print("Time requested from ", client_address)
        nettime = int( time.time() + 2208988800 )
        data = nettime.to_bytes( 4, byteorder='big', signed=False)
        # print("Current time ", nettime, data)
        server.sendto( data , client_address)
    except:
        pass
    finally:
        pass
