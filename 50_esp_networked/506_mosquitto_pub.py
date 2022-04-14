""" Demonstration of MQTT protocol - inject random  messages """
# http://www.steves-internet-guide.com/into-mqtt-python-client/

def mqtt_client(server):
    import time as utime

    # setup Mosquitto
    # on Python3:
    # pip install paho-mqtt
    from paho.mqtt.client import Client as MQTTClient
    mqttc = MQTTClient(b'ESP8266-00000000', server)
    mqttc.connect(server)
    mqttc.loop_start()
    while True:
        import binascii as ubinascii
        import random
        # randomly inject invalid numbers with 'g'
        machine_id = 'ESP8266-%s' % (''.join( random.choices('0123456789abcdefg', k=6) ) )
        # randomly inject invalid state 'x'
        butstate   = str( ''.join(random.choices('01x') ) )
        mqttc.publish('test/bradley_edu', '%s B0 %s' % ( machine_id , str(butstate) ) )
        utime.sleep(2)
    mqttc.loop_stop()

# this will run main() if this code is pasted directly into Python console
if __name__ == "__main__":
    # mqtt_client('192.168.88.55')
    # mqtt_client('iot.eclipse.org')
    mqtt_client('test.mosquitto.org')