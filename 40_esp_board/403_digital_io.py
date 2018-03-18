""" Testing digital IO pin access in MicroPython """

def shimmer():
    import time
    from machine import Pin, PWM
    pwm0 = PWM(Pin(2))
    pwm0.freq(1000)
    while True:
        for x in range (0, 1023):
            pwm0.duty(x)
            time.sleep_ms(10)
    pwm.deinit()

def blink():
    import time
    import machine
    led = machine.Pin(2)
    led.init(machine.Pin.OUT)
    while True:
        led.value(1)
        time.sleep_ms(250)
        led.value(0)
        time.sleep_ms(250)
    pwm.deinit()


def toggle():
    """
        requires a wire connected to pin 14 (D5) to be periodically connected to GND or a real button
    """
    import time
    import machine
    led = machine.Pin(2)
    led.init(machine.Pin.OUT)
    ledstate = 0
    led.value(ledstate)
    but = machine.Pin(0)
    but.init(machine.Pin.IN, machine.Pin.PULL_UP)
    butstate = but.value()
    while True:
        if but.value()!=butstate:
            butstate = but.value()
            time.sleep_ms(10) # for debouncing
            if butstate==0:
                ledstate = not ledstate
                led.value(ledstate)
                # Warning! Pin.value() behavior is undefined on output pins!
                # It just happens that it does work on ESP8266 (platform dependent)
                # led.value(not led.value())
    pwm.deinit()


"""
copy-paste function(s) into your board
or
copy this example as a file test_io.py and then run
    import test_io
    test_io.shimmer()
    Ctrl+C
    test_io.blink()
    Ctrl+C
    test_io.toggle()
    Ctrl+C
Note: there is no way to re-import the code after the file is changed, the board must be reset
"""
