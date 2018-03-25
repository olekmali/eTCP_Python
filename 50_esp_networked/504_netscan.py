""" scan,  list and connect one-by one to every ESP board in the proximity """
wireless = object()

def init():
    global wireless
    # set up wireless scan and connection
    import upbu_netlib
    upbu_netlib.init()
    wireless = upbu_netlib.get_STA()

def netscan():
    import upbu_netlib
    import utime
    global wireless
    print('Scanning for uP Access Points:')
    for ssid in upbu_netlib.scan():
        print('  Attempting connection to ', ssid)
        wireless.connect(ssid,'micropythoN')
        cnt = 0
        while cnt<5000 and not wireless.isconnected():
            utime.sleep_ms(1)
            cnt = cnt+1
        if wireless.isconnected():
            ifstats = wireless.ifconfig()
            print( "    Connected to %s %s as %s after %s ms" % ( ssid, ifstats[3], ifstats[0], cnt ) )
            # --> if needed insert a command to send data without any loop/wait time
        else:
            print( "    Connection to %s failed" % (ssid) )
        wireless.disconnect()
    print('Scan complete')


def test():
    init()
    # set up button
    from machine import Pin
    button = Pin(0)
    button.init(Pin.IN, Pin.PULL_UP)
    butstate = button.value()
    while True:
        if button.value()!=butstate:
            butstate = button.value()
            if butstate==0:
                netscan()
        # --> if needed insert a command to check for any already received data without any loop/wait time
        # --> if needed insert a command to act on any received data without any loop/wait time
    # end of the forever test loop

# this will run main() if this code is pasted directly into Python console
if __name__ == "__main__":
    test()
