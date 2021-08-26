import json
from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.122.72', 'mkphung1', 'cisco')
device.open()

output = device.get_facts()
print(json.dumps(output, indent=4))

output = device.get_interfaces()
print(json.dumps(output, indent=4))

output = device.get_interfaces_counters()
print(json.dumps(output, indent=4))
