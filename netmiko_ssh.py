from netmiko import ConnectHandler

switch1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.72',
    'username': 'mkphung1',
    'password': 'cisco'
}

switch2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.82',
    'username': 'mkphung1',
    'password': 'cisco'
}

switch3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.83',
    'username': 'mkphung1',
    'password': 'cisco'
}

all_devices = [switch1, switch2, switch3]

with open('commands.txt') as f:
    lines = f.read().splitlines()
# print(lines)

for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print(output)
