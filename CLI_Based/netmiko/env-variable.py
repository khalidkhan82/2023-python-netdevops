from netmiko import ConnectHandler
import os

# connect using a dictionary
csr = {
    'device_type': 'cisco_ios',
    'host':   'sandbox-iosxe-recomm-1.cisco.com',
    'username': os.environ.get('USERNAME'),
    'password': os.environ.get('PASSWORD')
}

# region Print statements
print(csr['username'])
print(csr['password'])
# endregion

# we will save the command that we want to execute on the host in a variable
command = "show ip int br"

# Will automatically 'disconnect()'
with ConnectHandler(**csr) as net_connect:
    output = net_connect.send_command(command)
    # two separate print statements for easier understanding
    print(net_connect.find_prompt())
    print(output)
    # single print statement, better approach
    # print(f"{net_connect.find_prompt()}\n\r{output}")

    net_connect.