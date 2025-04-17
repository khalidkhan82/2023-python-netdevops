from netmiko import ConnectHandler
from getpass import getpass

# connect without a dictionary
net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="10.10.20.21",
    username="cisco",
    password="cisco",
)

command = "show ip int br"
output = net_connect.send_command (command)
print(f"{net_connect.find_prompt()}{output}")

net_connect.disconnect()