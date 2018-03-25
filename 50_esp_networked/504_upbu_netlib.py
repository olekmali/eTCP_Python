""" uPython for ESP* network scan library """

""" (C)2018 DrAM http://olek.matthewm.com.pl/
    - MIT License
    - use at your own risk
    - nothing guaranteed
    - give due credits respectively
"""

#global variables
wlan_ap = object()
wlan_st = object()

def init():
    global wlan_ap
    global wlan_st
    import network
    #
    wlan_ap = network.WLAN(network.AP_IF)
    wlan_ap.active(True)
    #
    wlan_st = network.WLAN(network.STA_IF)
    wlan_st.active(True)
    wlan_st.disconnect()


def scan():
    global wlan_ap
    global wlan_st

    list = []
    aplist = wlan_st.scan()
    for entry in aplist:
        ssid = entry[0]
        if ssid.startswith('MicroPython') or ssid.startswith('ESP_'):
            list.append(ssid)
    return(list)


def get_AP():
    global wlan_ap
    return(wlan_ap)


def get_STA():
    global wlan_st
    return(wlan_st)

