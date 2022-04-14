""" machine to machine messaging via intermittent connections """

udps = object()

def init(listen_addr):
    # The server socket needs to be set up and ready waiting for any incoming messages 
    # even when we are not checking at the very moment. One thread - we don't wait and listen!
    global udps
    import socket
    udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udps.bind(listen_addr)
    udps.settimeout(0) # do not block this socket on read

def deinit():
    global udps
    udps.close()

def msg_check():
    global udps
    try:
        message, fr_addr = udps.recvfrom(10)
    except: # catch timeout exception
        message = ''
        fr_addr = ('',0)
    return(message, fr_addr)

def msg_send(destination_addr, message):
    # extra code for using both AP and STA
    import network
    st =network.WLAN(network.STA_IF);
    while not st.isconnected():
        st.connect()
    ap =network.WLAN(network.AP_IF);
    save_status = ap.active()
    ap.active(False)
    # extra code ends, more below
    import socket
    udpc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # we use bind on the client side to select a particular network interface
    udpc.sendto(message, destination_addr)
    udpc.close()
    # extra code for using both AP and STA
    ap.active(save_status)
    # extra code ends

def test():
    import network
    import socket
    import utime
    import upbu_netlib
    upbu_netlib.init()
    # we can open the server on all network interfaces or only one defined by a non-zero IP
    listen_ip   = network.WLAN(network.AP_IF).ifconfig()[0]
    listen_addr = socket.getaddrinfo(listen_ip, 473)[0][-1]
    init(listen_addr)
    # set up button
    from machine import Pin
    button = Pin(0)
    button.init(Pin.IN, Pin.PULL_UP)
    butstate = button.value()
    while True:
        if button.value()!=butstate:
            butstate = button.value()
            if butstate==0:
                # technically we can pick a different destination IP address each time
                print('Scanning for uP Access Points:')
                for ssid in upbu_netlib.scan():
                    print('  Attempting connection to ', ssid)
                    wireless = upbu_netlib.get_STA()
                    wireless.connect(ssid,'micropythoN')
                    cnt = 0
                    while cnt<5000 and not wireless.isconnected():
                        utime.sleep_ms(1)
                        cnt = cnt+1
                    if wireless.isconnected():
                        print('  Sending to ', ssid)
                        dest_ip   = network.WLAN(network.STA_IF).ifconfig()[2]
                        dest_addr = socket.getaddrinfo(dest_ip, 473)[0][-1]
                        msg_send(dest_addr, 'pressed')
                print('Scan complete')
        msg, frm = msg_check()
        if len(msg)>0:
            print('received: ', msg)
    # end of the forever test loop

if __name__ == "__main__":
    import network
    # ESP station  to ESP access point
    network.WLAN(network.AP_IF).active(True)
    network.WLAN(network.STA_IF).active(True)
    local_ip   = network.WLAN(network.AP_IF).ifconfig()[0]
    my_ip      = network.WLAN(network.STA_IF).ifconfig()[0]
    gateway_ip = network.WLAN(network.STA_IF).ifconfig()[2]
    print("My IP on the remote WiFi is %s and the gateway IP is %s" % (my_ip, gateway_ip) )
    print("My IP on my own WiFi AP is %s" % local_ip)
    print("I will be temporarily switching off my own access point when transmitting because of the potential IP conflict")
        # Note: in this software version we are switching it off anyway regardless of the conflict or not
    test()
