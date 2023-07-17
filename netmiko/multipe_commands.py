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

multi_command = ['show int status', 'show ip route', 'show ip int brief']

print ("connecting to the device " + router['host'])

output_multi = net_connect.send_multiline (multi_command)
print(output_multi)

output = net_connect.save_config ()
print("Saving the config: " + output)

net_connect.disconnect()