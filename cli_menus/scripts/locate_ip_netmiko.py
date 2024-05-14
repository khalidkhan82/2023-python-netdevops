from netmiko import ConnectHandler

# Define device details
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.201',         # IP address of the device
    'username': 'admin',
    'password': 'admin',   # Enter your device password here
    'secret': 'admin'    # Enter your enable password here if needed
}

# Connect to the device
net_connect = ConnectHandler(**device)
net_connect.enable()  # Enter privileged exec mode if needed

# Function to find interface for given IP address
def find_interface_for_ip(ip_address):
    interface = None  # Default value if IP address is not found
    # Send command to get ARP table
    arp_table_output = net_connect.send_command('show ip arp')

    # Parse ARP table to find MAC address for given IP
    for line in arp_table_output.splitlines():
        if ip_address in line:
            mac_address = line.split()[3]  # Extract MAC address
            interface = line.split()[5]
            return mac_address, interface
            break

    # Send command to get MAC address table
    # mac_table_output = net_connect.send_command('show mac address-table')

    # Parse MAC address table to find interface for MAC address
    #for line in mac_table_output.splitlines():
    #    if mac_address in line:
    #        interface = line.split()[1]  # Extract interface
    #        break
    #    return interface

# Define the IP address you want to search for
search_ip = '10.10.1.2'  # Replace with the IP address you want to search for

# Call the function to find the interface for the given IP address
mac_address, interface = find_interface_for_ip(search_ip)
if interface:
    print(f"The IP address {search_ip} is seen on interface {interface} with MAC address {mac_address}")
else:
    print(f"The IP address {search_ip} is not found in ARP or MAC address table.")

# Disconnect from the device
net_connect.disconnect()
