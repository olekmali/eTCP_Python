import machine
tim  = machine.Timer(-1)
# call localtime() at leiast once every 7 hours to prevent timer from overflowing
tim.init(period=(6*3600*1000), mode=machine.Timer.PERIODIC, callback=lambda t:localtime() )

# call nptime.utime.time() (module nptime.py) periodically to correct poor accuracy of the built-in RTC
tim.init(period=(3600*1000), mode=machine.Timer.PERIODIC, callback=lambda t:nptime.utime.time() )
