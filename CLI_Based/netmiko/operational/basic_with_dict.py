from netmiko import Netmiko

## Netmiko

# connect using a disctionary
csr = {
    'device_type': 'cisco_ios',
    'host':   'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876'
}

net_connect = Netmiko(**csr)
print("Connected successfully")
print(dir(net_connect))
# sh_output = net_connect.send_command("show run")
# print(sh_output)
print(net_connect.find_prompt())
print(net_connect.check_config_mode())
# print(net_connect.check_enable_mode())
net_connect.config_mode()
print(net_connect.check_config_mode())
print(net_connect.find_prompt())
net_connect.disconnect()