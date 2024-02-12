from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host=input("host:"),
    username=input("username:"),
    password=getpass(),
)

print(net_connect.find_prompt())
net_connect.disconnect()