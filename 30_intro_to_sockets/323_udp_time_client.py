# UDP Time37 client
import socket

HOST, PORT = "time-c-g.nist.gov", 37
#HOST, PORT = "localhost", 37
ATTEMPTS = 3

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(ATTEMPTS):
    try:
        client.setblocking(2.0)
        client.sendto( bytes(), (HOST, PORT) )
        back, addr = client.recvfrom(4)
        nettime = int.from_bytes(back, byteorder='big', signed=False)
        print( "Raw data: ", back ) # binary string
        print( "Net time: ", nettime )
        break
    except:
        print( "No response from the time server!" )
        if i<ATTEMPTS:
            print("retrying...")
