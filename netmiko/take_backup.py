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

output = net_connect.send_command ('show run')
save_file = open(router["host"] + "_backup", 'w')
save_file.write(output)

print("Saving the config: ")

net_connect.disconnect()