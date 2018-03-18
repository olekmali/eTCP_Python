""" Simple HTTP server -- MicroPython Documentation """

def httpd_pins():
    import machine
    pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

    html_header = "HTTP/1.0 200 OK\r\nServer: uPython on ESP8266\r\nConnection: close\r\nExpires: 0\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
    png_header  = "HTTP/1.0 200 OK\r\nServer: uPython on ESP8266\r\nConnection: close\r\nExpires: 0\r\nContent-Type: image/png\r\n\r\n"
    html_file1 = """<!DOCTYPE html>
    <html>
        <head> <title>ESP8266 Pins</title> </head>
        <body> <h1>ESP8266 Pins</h1>
            <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
        </body>
    </html>
    """

    import socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('r')
        request = str( cl_file.readline(), 'UTF-8' )
        file    = request.split(' ')[1]
        # print('request line', request)
        print('request file', file)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
        response = html_file1 % '\n'.join(rows)
        cl.send( bytes( html_header, 'UTF-8' ))
        cl.send( bytes( response, 'UTF-8' ))
        cl.close()
        print('served')

""" To test run:
import web_server
web_server.httpd_pins()
"""
