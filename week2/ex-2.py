from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "global_delay_factor": 4,
}

time = datetime.now()

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())








time1 = datetime.now()
output = net_connect.send_command("show lldp neighbors detail")
print(output)
time2 = datetime.now()

time3 = datetime.now()
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
print(output)
time4 = datetime.now()

print('\n',time1,'\n',time2)

print('\n',time3,'\n',time4)
