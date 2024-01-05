from netmiko import ConnectHandler
from getpass import getpass

# connect using a disctionary
csr = {
    'device_type': 'cisco_ios',
    'host':   'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876'
}

# Open connection using the 'with' Contextmanager. Connection Will automatically 'disconnect()' when the execution
# of the Contextmanager is complete. 
with ConnectHandler(**csr) as net_connect:
    print(net_connect.find_prompt())
    # Call 'enable()' method to elevate privileges
    net_connect.enable()
    print(net_connect.find_prompt())