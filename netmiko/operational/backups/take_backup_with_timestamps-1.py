from netmiko import ConnectHandler
from getpass import getpass
import time
import datetime

# obtain time at the runtime and save in a variable
current_time = datetime.datetime.now().replace(microsecond=0)

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
save_file = open("./output_files/" + router["host"] + "_backup" + str(current_time), 'w')
save_file.write(output)

print("Saving the config: ")

net_connect.disconnect()0