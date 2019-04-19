# NTP time query - will throw an exception if time cannot be obtained
# Source: https://github.com/micropython/micropython/blob/master/ports/esp8266/modules/ntptime.py

# (date(2000, 1, 1) - date(1900, 1, 1)).days * 24*60*60
NTP_DELTA = 3155673600
host = "pool.ntp.org"
timezone = int(0*3600)

def time():
    import usocket
    import ustruct
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1b
    addr = usocket.getaddrinfo(host, 123)[0][-1]
    s = usocket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    s.sendto(NTP_QUERY, addr)
    msg = s.recv(48)
    s.close()
    val = ustruct.unpack("!I", msg[40:44])[0]
    return val - NTP_DELTA

# There's currently no timezone support in MicroPython, so
# utime.localtime() will return UTC time (as if it was .gmtime())
def settime():
    t = time()
    import machine
    import utime
    tm = utime.localtime(t)
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    machine.RTC().datetime(tm)

def settimezone(tz):
    timezone = int (tz*3600)

def settime_wzone():
    t = time() + timezone
    import machine
    import utime
    tm = utime.localtime(t)
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    machine.RTC().datetime(tm)

def settime_wzone_safe():
    try:
        settime_wzone()
    except:
        pass

