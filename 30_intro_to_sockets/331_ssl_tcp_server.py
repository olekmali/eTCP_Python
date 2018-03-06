import socket, ssl

HOST, PORT = "localhost", 1201

count = 0


def deal_with_client(request, client_address):
    global count    # indicate that there is no new local variable called count
    count = count + 1;

    request.sendall( bytes( "Welcome to the server.\r\nWhat is your name please?\r\n", 'UTF-8' ) )
    request.setblocking(True)
    name = str( request.recv(1024), 'UTF-8' ).strip()
    print( name , " has just contacted us from " , client_address )
    data = "Nice to meet you " + name + ".\r\nYou are the " + str(count) + "th person who stopped by today\r\n"
    request.sendall( bytes( data, 'UTF-8' ) )
    # finished with client


ssl_context = ssl.create_default_context(purpose=Purpose.SERVER_AUTH)
ssl_context.load_cert_chain(certfile="331_cert.pem", keyfile="331_cert.pem")
""" The self-signed certificate was created by running:
    openssl req -new -x509 -days 3650 -nodes -out cert.pem -keyout cert.pem
"""

server_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_scoket.bind( (HOST, PORT) )
server_scoket.listen(1)

while True:
    client, fromaddr = server_scoket.accept()
    try:
        ssl_client = ssl_context.wrap_socket(client, server_side=True)
        try:
            deal_with_client(ssl_client, fromaddr)
        except:
            print( "Client connection error" )
        finally:
            ssl_client.shutdown(socket.SHUT_RDWR)
            ssl_client.close()
    except:
        print( "Client TLS connection error" )
