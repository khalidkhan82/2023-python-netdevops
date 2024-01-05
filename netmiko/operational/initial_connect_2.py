from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="sandbox-iosxe-recomm-1.cisco.com",
    username="developer",
    password="lastorangerestoreball8876",
)

print(net_connect.find_prompt())
net_connect.disconnect()