""" machine to machine messaging via infrastructure """
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

def msg_send(remote_addr, message):
    import socket
    udpc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # we let Python figure out which network interface to use - no bind
    udpc.sendto(message, remote_addr)
    udpc.close()

def test(local_ip, remote_ip):
    import socket
    # we can open the server on all network interfaces or only one defined by a non-zero IP
    local_addr  = socket.getaddrinfo(local_ip,  473)[0][-1]
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
                msg_send(remote_addr, 'pressed')
        msg = msg_check()
        if len(msg)>0:
            print('received: ', msg)
    # end of the forever test loop

if __name__ == "__main__":
    import network
    # local_ip = network.WLAN(network.STA_IF).ifconfig()[0]
    local_ip = '0.0.0.0'
    to_ip    = '192.168.4.2'
    test(local_ip, to_ip)
""" all ESPs connected to infrastructure
import network
network.WLAN(network.AP_IF).active(False)
network.WLAN(network.STA_IF).active(True)
network.WLAN(network.STA_IF).ifconfig()[0]
"""
