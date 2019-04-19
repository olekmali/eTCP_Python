""" Simple HTTP server -- MicroPython Documentation """

def httpd_pins():
    header = "HTTP/1.1 %s\r\nServer: uPython on ESP8266\r\nConnection: close\r\nExpires: 0\r\nContent-Type: %s\r\n\r\n"

    import machine
    pins = [machine.Pin(i) for i in (0, 2, 4, 5, 12, 13, 14, 15)]
    for p in pins:
        p.init(machine.Pin.IN, machine.Pin.PULL_UP)

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
        # read the reminder of the request to make a Web browser happy
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break

        if file == '/' or file == '/index.html':
            html_file1 = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""
            rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
            response = html_file1 % '\n'.join(rows)
            cl.send( bytes( ( header % ('200 OK','text/html; charset=UTF-8') ), 'UTF-8' ))
            cl.send( bytes( response, 'UTF-8' ))
        else:
            html_file2 = """<!DOCTYPE html>
<html>
    <head> <title>404 Not Found</title> </head>
    <body> <h1>Resource not found</h1>
        <p>Why don't you try <a href="/">here</a>?</p>
    </body>
</html>
"""
            cl.send( bytes( ( header % ('404 Not Found','text/html; charset=UTF-8') ), 'UTF-8' ))
            cl.send( bytes( html_file2, 'UTF-8' ))
        cl.close()
        print('served')

# this will run main() if this code is pasted directly into Python console
if __name__ == "__main__":
    import network
    wlan_st = network.WLAN(network.STA_IF)
    wlan_st.active(True)
    print( ("Connect to http://%s/" % wlan_st.ifconfig()[0]) )

    httpd_pins()

""" To test run:
copy this file to the board and then type
import web_server
web_server.httpd_pins()
"""
