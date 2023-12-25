from netmiko import ConnectHandler
from getpass import getpass


# we define our host using a dictionary
router = {
    'device_type': 'cisco_ios',
    'host':   'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876'
}

# create connection object and store in a variable
net_connect = ConnectHandler(**router)

output = net_connect.send_config_from_file(config_file="new_config_2.txt")
print(output)

output = net_connect.save_config()
print("Saving the config: " + output)

net_connect.disconnect()