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

pingLines = {
    1: {
        "command" : "ping", 
        "expect" : r"foo",
    },
    2: {
        "command" : "ip",
        "expect" : r"word"
    },
    3: {
        "command" : "8.8.8.8",
        "expect": r"word"
    },
    4: {
        "command" : "line4",
        "expect": r"word"
    },
    5: {
        "command" : "100",
        "expect": r"word"
    },
    6: {
        "command": "2",
        "expect": r"word"
    },
    7: {
        "command": "3",
        "expect": r"puncline"
    },
    }

output = ""
for key, value in iter(sorted(pingLines.items())):
    #output += net_connect.send_command(command, expect_string = expect,strip_prompt=False, strip_command=False)    
    print(key)
    print(value)

print(output)
net_connect.disconnect()

