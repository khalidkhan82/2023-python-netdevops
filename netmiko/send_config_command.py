from netmiko import ConnectHandler
from getpass import getpass


# we define our host using a dictionary
router = {
    'device_type': 'cisco_ios',
    'host':   'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876'
}

# create connectio object and store in a variable
net_connect = ConnectHandler(**router)

# with open("new_config.txt") as new_config:
#    config = new_config.read()

command = 'access-list 101 permit ip any any'
output = net_connect.send_config_set(command)
print(output)

output = net_connect.save_config ()
print("Saving the config: " + output)

net_connect.disconnect()

