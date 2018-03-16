def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    buffer = b''
    while True:
        data = s.recv(100)
        if data:
            buffer = buffer + data 
        else:
            break
    s.close()
    return(buffer)

print(str(http_get('http://www.bradley.edu/'), 'utf8'), end='')
