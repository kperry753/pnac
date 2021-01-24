from netmiko import ConnectHandler
from getpass import getpass
'''
cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}
'''
cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",       
    "password": getpass(),       
    "device_type": "cisco_ios",  
}

net_connect = ConnectHandler(**cisco4)
print(net_connect.find_prompt())

commands = [
    "ping",
    "ip",
    "8.8.8.8",
    "5",
    "100",
    "2",
    "",
    "",
    ]

output = ""
for command in commands:
    output += net_connect.send_command_timing(command,strip_prompt=False, strip_command=False)    

print(output)
net_connect.disconnect()

