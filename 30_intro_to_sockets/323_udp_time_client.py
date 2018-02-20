import socket

HOST, PORT = "time-c-g.nist.gov", 37

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setblocking(2.0)
client.sendto( bytes(), (HOST, PORT) )
back, addr = client.recvfrom(2048)

nettime = int.from_bytes(back, byteorder='big', signed=False)

print( "Raw data: ", back ) # binary string
print( "Net time: ", nettime )
