""" Demonstration of MQTT protocol """
# https://github.com/micropython/micropython-lib/tree/master/umqtt.simple

led = object()

def callback_function(topic, msg):
    # must proceed as quickly as possible and return back to wherever it was called from
    # otherwise, the MicroPython world will collapse
    global led
    print('Debug: ', (topic, msg))
    # with only one topic subscription there is no need to check for the topic 
    msg = str(msg, 'UTF-8')
    if msg.startswith('ESP8266-'):
        try:
            remote_id, io_part, state = msg.split(' ', 3)
            val = int(state)
            if val==0 or val==1:
                led.value(val)
                print('  led=', val)
            else:
                print('  parameter out of range: ', state)
        except:
            print('  invalid parameter(s)')

def mqtt_client(server):
    # setup the BUTton and LED
    global led
    import machine, ubinascii, utime
    machine_id = b'ESP8266-%s' % ubinascii.hexlify( machine.unique_id() )
    led = machine.Pin(2)
    led.init(machine.Pin.OUT)
    button = machine.Pin(0)
    button.init(machine.Pin.IN, machine.Pin.PULL_UP)
    # setup Mosquitto
    from umqtt.robust import MQTTClient
    mqttc = MQTTClient(machine_id, server)
    mqttc.connect()
    mqttc.set_last_will(b'test/bradley_edu', b'%s signoff 1' % ( machine_id ) )
    mqttc.set_callback(callback_function)
    mqttc.subscribe(b'test/#')

    # run Mosquitto
    butstate = button.value()
    while True:
        if button.value()!=butstate:
            butstate = button.value()
            mqttc.publish(b'test/bradley_edu', b'%s B0 %s' % ( machine_id , str(butstate) ) )
        mqttc.check_msg()  # this will check for messages and call the callback function if needed
        utime.sleep_ms(20) # time to allow the callback function to do its job to avoid calling multiple instances
    # we actually never quit but this is how shutdown should look like
    mqttc.disconnect()

# this will run main() if this code is pasted directly into Python console
if __name__ == "__main__":
    # mqtt_client('192.168.88.55')
    mqtt_client('iot.eclipse.org')
    # mqtt_client('test.mosquitto.org')