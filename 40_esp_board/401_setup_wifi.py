# Setup persistent WiFi:
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('malilab', 'dram-portable-lab-key')
wlan.ifconfig()

# Check WiFi status:
import network
wlan = network.WLAN(network.STA_IF)
wlan.ifconfig()

# Setup WebREPL:
import webrepl_setup
""" when prompted enter the password for file transfer """

# Start the WebREPL server
import webrepl
webrepl.start()
