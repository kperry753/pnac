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

pingLines = [
    {
        "command" : "ping", 
        "expect" : r"foo",
    },
    {
        "command" : "ip",
        "expect" : r""
    },
    {
        "command" : "8.8.8.8",
        "expect": r""
    },
    {
        "command" : "line4",
        "expect": r""
    },
    {
        "command" : "100",
        "expect": r""
    },
    {
        "command": "2",
        "expect": r""
    },
    {
        "command": "",
        "expect": r""
    },
    ]

output = ""
for line in pingLines:
    output += net_connect.send_command(pingLines.get("command"), expect_string = pingLines.get("expect"),strip_prompt=False, strip_command=False)    

print(output)
net_connect.disconnect()

