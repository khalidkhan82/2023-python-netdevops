# find-mac-address
from netmiko import ConnectHandler
from getpass import  getpass

CSR = {
    'device_type': 'cisco_ios',
    'host': '10.255.255.44',
    'username': 'khaldim',
    'password': getpass("Enter password:", ),
}

net_connect = ConnectHandler(**CSR)

mac_to_find = input("Enter the mac to find: ")
command_mac = "show mac address-table"
command_arp = "show arp"

mac_output = net_connect.send_command(command_mac, use_textfsm=True)
arp_output = net_connect.send_command(command_arp, use_textfsm=True)

print(mac_output)
print(arp_output)

net_connect.disconnect()
