from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "global_delay_factor": 4,
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show lldp neighbors detail")
print(output)
