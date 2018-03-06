import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('malilab', 'dram-portable-lab-key')

def shimmer():
    import time
    from machine import Pin, PWM
    pwm0 = PWM(Pin(2))
    pwm0.freq(1000)
    while True:
        for x in range (0, 1023):
            pwm0.duty(x)
            time.sleep_ms(10)
     