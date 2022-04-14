""" HTTP server that runs in parallel with other task """

import socket
httpd_socket = object()

import machine
pin_led = object()
pin_but = object()
butstate= 1

def hardware_init():
    global pin_led
    global pin_but
    global butstate
    pin_led = machine.Pin(2, machine.Pin.OUT)
    pin_led.value(0)
    pin_but = machine.Pin(0)
    pin_but.init(machine.Pin.IN, machine.Pin.PULL_UP)
    butstate = pin_but.value()

def hardware_update():
    global pin_led
    global pin_but
    global butstate
    if pin_but.value()!=butstate:
        butstate = pin_but.value()
        if butstate==0:
            pin_led.value(not pin_led.value())

def httpd_init():
    global httpd_socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    httpd_socket = socket.socket()
    httpd_socket.bind( addr )
    httpd_socket.listen(1)
    httpd_socket.settimeout(0.1)

def httpd_deinit():
    global httpd_socket
    httpd_socket.close()

def httpd_service():
    import upbu_urllib
    global httpd_socket
    global pin_led
    try: 
        # print('waiting for accept')
        cl, addr = httpd_socket.accept()
        led_status = not pin_led.value()
    except:
        # print('wait timeout')
        return

    header = "HTTP/1.1 %s\r\nServer: uPython on ESP8266\r\nConnection: close\r\nExpires: 0\r\nContent-Type: %s\r\n\r\n"
    form   = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 LED</title> </head>
    <body> <h1>ESP8266 LED</h1>
        <form action="/">
        LED = 
        <input type="text" name="led" value="%s"></input>
        <input type="submit" value="Submit">
        </form>
        <br /><a href="/">Check the current status</a>
    </body>
</html>
"""
    error = """<!DOCTYPE html>
<html>
    <head> <title>%s</title> </head>
    <body> <h1>%s</h1>
        <p>Why don't you try <a href="/">here</a>?</p>
    </body>
</html>
"""

    # print('client connected from', addr)
    cl_file = cl.makefile('r')
    # read the first request line
    request = str( cl_file.readline(), 'UTF-8' )
    # extract the http request parameter
    request = request.split(' ')[1]
    # note: in this design we ignore the method [0] and assume that it is GET
    #       we could have checked that and rendered 405 Method not allowed error
    # parse the requested URL and potential parameters
    file, values = upbu_urllib.parse_url(request)
    # read the reminder of the request to make a Web browser happy
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break

    if file == '/' or file == '/index.html':
        # access a parameter only if it exists in the list made from the http request
        if 'led' in values:
            try:
                # always typecast the parameter to the desired type and check its range
                # and be prepared to catch any unexpected behavior and abort the process
                led_par = int(values['led'])
                if led_par>=0 and led_par<=1:
                    led_status = led_par
                    led_feedback = str(led_status)
                else:
                    led_feedback = 'enter 0 or 1'
            except:
                led_feedback = 'enter integer here'
        else:
            led_feedback = str(led_status)

        # action
        pin_led.value(not led_status)

        # Web server feedback
        cl.send( bytes( header % ('200 OK','text/html; charset=UTF-8'), 'UTF-8' ))
        cl.send( bytes( form % (led_feedback), 'UTF-8' ) )
    else:
        cl.send( bytes( header % ('404 Not Found','text/html; charset=UTF-8'), 'UTF-8' ))
        cl.send( bytes( error % ('404 Not Found','The requested service is not available'), 'UTF-8' ) )
    cl.close()
    # print('served')

if __name__ == "__main__":
    import network
    wlan_st = network.WLAN(network.STA_IF)
    wlan_st.active(True)
    print( ("Connect to http://%s/" % wlan_st.ifconfig()[0]) )

    import time
    hardware_init()
    try:
        httpd_socket.close() # in case previous run crashed
    except:
        pass
    httpd_init()
    while True:
        hardware_update()
        httpd_service()
        time.sleep_ms(10)


