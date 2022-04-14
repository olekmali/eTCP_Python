""" Demonstration of MQTT protocol - monitor only """
# https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
# http://www.steves-internet-guide.com/into-mqtt-python-client/

def callback_function_umqtt(topic, msg):
    print('Received: ', (topic, msg))

def callback_function_PahoMQTT(client, userdata, message):
    print('Received: ', ( message.topic, str(message.payload.decode("utf-8")) ) )

def mqtt_client(server):
    # ESP8266: import ubinascii, utime
    import time
    machine_id = b'ESP8266-999999'

    # setup Mosquitto
    # on Python3:
    # pip install paho-mqtt
    from paho.mqtt.client import Client as MQTTClient
    mqttc = MQTTClient(machine_id, server)
    mqttc.connect(server)
    mqttc.on_message = callback_function_PahoMQTT
    mqttc.subscribe('test/#')
    mqttc.loop_start()
    while True:
        time.sleep(1)
    mqttc.loop_stop()
    
    # ESP8266: 
    # from umqtt.robust import MQTTClient
    # mqttc.connect()
    # mqttc.set_callback(_umqtt)
    # mqttc.subscribe(b'test/#')
    # run Mosquitto
    # while True:
    #     mqttc.check_msg()
    #     utime.sleep_ms(20)
    # mqttc.disconnect()

# this will run main() if this code is pasted directly into Python console
if __name__ == "__main__":
    # mqtt_client('192.168.88.55')
    # mqtt_client('iot.eclipse.org')
    mqtt_client('test.mosquitto.org')