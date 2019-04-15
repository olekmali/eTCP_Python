t1 = object()
t2 = object()
t3 = object()

def timer_test():
    import machine
    global t1
    global t2
    global t3
    t1 = machine.Timer(-1)
    t2 = machine.Timer(-1)
    t3 = machine.Timer(-1)
    t1.init(period=5000, mode=machine.Timer.ONE_SHOT, callback=lambda t:print(1, end=' ') )
    t2.init(period=2000, mode=machine.Timer.PERIODIC, callback=lambda t:print(2, end=' ') )
    t3.init(period=1500, mode=machine.Timer.PERIODIC, callback=lambda t:print(3, end=' ') )

def timer_test_stop():
    t1.deinit()
    t2.deinit()
    t3.deinit()

# to run type:
#   timer_test()
#
# to stop while running type without looking at the console:
#   timer_test_stop()
