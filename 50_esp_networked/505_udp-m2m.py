""" machine to machine messaging via intermittent connections """
udps = object()

def init(local_addr):
    # The server socket needs to be set up and ready waiting for any incoming messages 
    # even when we are not checking at the very moment. One thread - we don't wait and listen!
    global udps
    import socket
    udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udps.bind(local_addr)
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
    return(message)

def msg_send(local_addr, remote_addr, message):
    import network
    st =network.WLAN(network.STA_IF);
    while not st.isconnected():
        st.connect()
    ap =network.WLAN(network.AP_IF);
    save_status = ap.active()
    ap.active(False)
    import socket
    udpc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpc.bind(local_addr)
    udpc.sendto(message, remote_addr)
    udpc.close()
    ap.active(save_status)

def test(local_ip, from_ip, remote_ip):
    import socket
    # we can open the server on all network interfaces or only one defined by a non-zero IP
    local_addr  = socket.getaddrinfo(local_ip,  473)[0][-1]
    # we can decide to send the messages from a particular network interface
    from_addr   = socket.getaddrinfo(from_ip,     0)[0][-1]
    init(local_addr)
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
                remote_addr = socket.getaddrinfo(remote_ip, 473)[0][-1]
                msg_send(from_addr, remote_addr, 'pressed')
        msg = msg_check()
        if len(msg)>0:
            print('received: ', msg)
    # end of the forever test loop

if __name__ == "__main__":
    import network
    # ESP station  to ESP access point
    network.WLAN(network.AP_IF).active(True)
    network.WLAN(network.STA_IF).active(True)
    local_ip = network.WLAN(network.AP_IF).ifconfig()[0]
    from_ip  = network.WLAN(network.STA_IF).ifconfig()[0]
    to_ip    = network.WLAN(network.STA_IF).ifconfig()[2]
    print("My IP on the remote WiFi is %s and the destination IP is %s" % (from_ip, to_ip) )
    print("My IP on my own WiFi is %s" % local_ip)
    if to_ip == local_ip:
        print("I will be temporarily switching off my own access point when transmitting because of the IP conflict")
        # Note: in this software version we are switching it off anyway regardless of the conflict or not
    test(local_ip, from_ip, to_ip)
