# TCP Time37 client
import socket

HOST, PORT = "time-c-g.nist.gov", 37
#HOST, PORT = "localhost", 37
ATTEMPTS = 3

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in range(ATTEMPTS):
    try:
        client.settimeout(2.0)
        client.connect( (HOST, PORT) )
        # number inside socket.recv(nnn) sets the maximum number of bytes to receive
        data = client.recv(4)
        if len(data)!=4:
            raise
        nettime = int.from_bytes(data, byteorder='big', signed=False)
        print( "Raw data: ", data ) # binary string
        print( "Net time: ", nettime )
        break
    except:
        print( "No response from the time server!" )
        if i<ATTEMPTS:
            print("retrying...")
    finally:
        client.close()
