from netmiko import ConnectHandler

# we define our host using a dictionary
csr = {
    'device_type': 'cisco_ios',
    'host':   'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876'
}

# create connection object by sending the host dictionary as keyword arguments (**KWARGS)
# and store in a variable
net_connect = ConnectHandler(**csr)

multi_command = ['show int description', 'show ip route | begin Gateway', 'show ip int brief']

print ("connecting to the device " + csr['host'])

output_multi = net_connect.send_multiline (multi_command)
print(output_multi)

output = net_connect.save_config ()
print("Saving the config: " + output)

net_connect.disconnect()