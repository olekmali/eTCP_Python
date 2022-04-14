import socket, ssl

HOST, PORT = "localhost", 1201
#HOST, PORT = "www.python.org", 443

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = True
ssl_context.verify_mode = ssl.CERT_REQUIRED

""" or try to do it your self from the scratch like below:
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ssl_context.verify_mode = ssl.CERT_REQUIRED # ssl.CERT_REQUIRED or ssl.CERT_OPTIONAL or ssl.CERT_NONE
    ssl_context.check_hostname = True
    ssl_context.load_default_certs()
"""

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_client = ssl_context.wrap_socket(client, server_hostname=HOST)
    ssl_client.connect( (HOST, PORT) )
    cert = ssl_client.getpeercert()
    print( cert )
    ###
    data = ssl_client.recv(1024)
    text = str( data, 'UTF-8' ).strip()
    print( text )
    ssl_client.sendall( bytes( "Automated Client\r\n", 'UTF-8' ))
    data = ssl_client.recv(1024)
    text = str( data, 'UTF-8' ).strip()
    print( text )
except:
    print( "Socket connection error!" )
finally:
    ssl_client.close()
