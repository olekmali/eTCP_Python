""" Simple HTTP client -- MicroPython Documentation """

def http_get(url):
    import socket
    proto, _, host, path = url.split('/', 3)
    buffer = b''
    try:
        if proto=='http:':
            addr = socket.getaddrinfo(host, 80)[0][-1]
            s = socket.socket()
            s.connect(addr)
            s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\nConnection: close\r\n\r\n' % (path, host), 'utf8'))
            while True:
                data = s.recv(100)
                if data:
                    buffer = buffer + data 
                else:
                    break
            s.close()
        elif proto=='https:':
            import ussl
            # See http://docs.micropython.org/en/v1.9.3/esp8266/library/ussl.html
            addr = socket.getaddrinfo(host, 443)[0][-1]
            s = socket.socket()
            try:
                ss = ussl.wrap_socket(s)
            except:
                raise('ssl_handshake_status: failed')
            ss.connect(addr)
            ss.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\nConnection: close\r\n\r\n' % (path, host), 'utf8'))
            while True:
                data = ss.recv(100)
                if data:
                    buffer = buffer + data 
                else:
                    break
            ss.close()
        else:
            raise('Unsupported protocol or malformed URL')
    except exc:
        buffer = b''
        # consider printing the exception error code or passing it up
        sys.print_exception(exc)
    finally:
        pass
    return(buffer)

""" To test run:
import web_client
print( str( web_client.http_get('http://www.bradley.edu/'), 'utf8' ), end='')
print( str( web_client.http_get('https://www.bradley.edu/'), 'utf8' ), end='')  # this fails due to unsupported SLL protocol
"""
