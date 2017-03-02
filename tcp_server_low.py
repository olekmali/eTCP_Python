import socket

HOST, PORT = "", 60000

count = 0


# Create a socket (SOCK_STREAM means a TCP socket)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

# serve forever
while 1:
    try:
        request, client_address = server.accept()
        count = count + 1;

        request.sendall("Welcome to the server.\r\nWhat is your name please?\r\n")

        # string.strip removes all leading and trailing white space inclduing \r\n
        # number inside socket.recv(nnn) sets the maximum number of bytes to receive
        name = request.recv(1024).strip()
        print name + " has just contacted us from " + format(client_address)
        
        # observe the conversion from an integer number to string
        data = "Nice to meet you " + name + ".\r\nYou are the " + str(count) + "th  person who stopped by today\r\n"
        request.sendall(data)
    finally:
        request.close()

