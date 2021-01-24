from netmiko import ConnectHandler
from getpass import getpass
import sys

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    #"session_log": 'my_session.txt'
}

device2 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    #"session_log": 'my_session.txt'
}


#Reference code for later, shouldn't need
#net_connect = ConnectHandler(routers)
#print(net_connect.find_prompt())


#This code will create an ssh session for each router
routers = [device1,device2]
for router in routers:
    net_connect = ConnectHandler(**router)
    print(net_connect.find_prompt())
    net_connect.disconnect()

net_connect = ConnectHandler(**device1)
output = net_connect.send_command("show version")

with open('shversion-output-example.txt', 'w') as file:
    file.write(output)


net_connect.disconnect()
