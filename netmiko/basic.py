from netmiko import ConnectHandler
from getpass import getpass

# connect without a dictionary
net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="sandbox-iosxe-recomm-1.cisco.com",
    username="developer",
    password="lastorangerestoreball8876",
)

command = "show ip int br"
output = net_connect.send_command (command)
print(f"{net_connect.find_prompt()}{output}")

net_connect.disconnect()