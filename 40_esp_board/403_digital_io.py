"""
    copy-paste function(s) into your board
    or
    copy this example as a file file_name.py and then run
        import file_name
        file_name.shimmer()
        Ctrl+C
        file_name.blink()
        Ctrl+C
        file_name.toggle()
        Ctrl+C
"""

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
    but = machine.Pin(14)
    but.init(machine.Pin.IN, machine.Pin.PULL_UP)
    state = but.value()
    while True:
        if but.value()!=state:
            state = but.value()
            time.sleep_ms(10) # for debouncing
            if state==0:
                led.value(not led.value())
    pwm.deinit()
