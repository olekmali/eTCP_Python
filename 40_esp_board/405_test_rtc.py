import machine
import utime

# call time() at least once every less than 7 hours to prevent timer from overflowing
tovprevent = machine.Timer(-1)
tovprevent.init(period=(6*3600*1000), mode=machine.Timer.PERIODIC, callback=lambda t:utime.time() )
# tovprevent.init(period=(1000), mode=machine.Timer.PERIODIC, callback=lambda t:print(utime.time()) )


def time_test():
    but = machine.Pin(0)
    but.init(machine.Pin.IN, machine.Pin.PULL_UP)
    last = utime.time()
    state = but.value()
    while True:
        if state!=but.value():
            state = but.value()
            if state==0:
                pressed = utime.time()
                print( utime.ticks_diff(pressed, last) )
                last = pressed
            else:
                released = utime.time()
                duration = utime.ticks_diff( released, pressed)
                if duration>=2:
                    print("It was a long press of", duration, "seconds")
                else:
                    print("It was a short press")
        utime.sleep_ms(10) # for debouncing
    
