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

# Alternative ways to print
# print(f"{net_connect.find_prompt()}{command}")
# print(f'{net_connect.send_command(command, use_textfsm=True)}')

# non-structured output without using textfsm. This output is similar to the one on CLI. 
# This is easier to read but difficult to access, reference for further manipulation.
output_unstructured = net_connect.send_command (command)
print (f'Unsctructured result - same output as on the CLI \n\r {output_unstructured} \n\r ')

# to use textfsm, in the send_command function call add 'use_textfsm=True'
# send_command will return the result in a structured form as a list/dic which 
# is easier to access and reference for further manipulation as we can see below
# We're storing the result in the variable 'output_structured' which in this case is a list.
output_structured = net_connect.send_command (command, use_textfsm=True)
print (f'Structured result - easier to access and reference \n\r {output_structured} \n\r ')

# Structured out can now be easily accessed or referenced for further actions/manipulation. 
# In this case, we are accessing the interfaces whose 'status' is 'admin down'
not_connected_interfaces = [item['intf'] for item in output_structured if item['status'] in 'administratively down' ]
print(f'\n\r The following interfaces are down \n\r {not_connected_interfaces}')

net_connect.disconnect()