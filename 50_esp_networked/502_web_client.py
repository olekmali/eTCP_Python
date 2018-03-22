""" Simple HTTP client -- MicroPython Documentation """

def http_get(url):
    import gc
    import socket
    proto, _, host, path = url.split('/', 3)
    buffer = b''
    try:
        if proto=='http:':
            s = socket.socket()
            s.connect( socket.getaddrinfo(host, 80)[0][-1] )
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
            s = socket.socket()
            s.connect( socket.getaddrinfo(host, 443)[0][-1] )
            try:
                ss = ussl.wrap_socket(s)
            except:
                raise('ssl_handshake_status: failed')
            gc.collect()
            ss.write(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\nConnection: close\r\n\r\n' % (path, host), 'utf8'))
            while True:
                gc.collect()
                data = ss.read()
                if data:
                    buffer = buffer + data 
                else:
                    break
            ss.close()
        else:
            raise('Unsupported protocol or malformed URL')
    except:
        buffer = b''
        # consider printing the exception error code or passing it up
        print('Error downloading web page /%s from %s using %s' % (path, host, proto))
    finally:
        pass
    return(buffer)

""" To test run:
import web_client
print( str( web_client.http_get('http://www.bradley.edu/'), 'utf8' ), end='')
# Warning! Large pages may run out of memory especially when using https
"""
