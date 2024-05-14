from napalm import get_network_driver

# Define device details
device = {
    'hostname': '192.168.1.201', # IP address of the device         
    'username': 'admin',
    'password': 'admin',   # Enter your device password here
    'optional_args': {'secret': 'admin'} # enable mode password
}

optional_arg = {'secret': 'admin'}

# specify the device driver to be used and create a NetworkDriver object
driver = get_network_driver('ios')
#net_connect = driver(hostname="192.168.1.201", username="admin", password="admin", optional_args=optional_arg)

# create a connection object by using the NetworkDriver object and passing the host info
net_connect = driver(**device)

# Function to find interface for given IP address
def find_interface_for_ip(ip_address):
    interface = None  # Default value if IP address is not found
    # open the connection
    net_connect.open()
    # Send command to get ARP table
    arp_table_output = net_connect.get_arp_table()

    # Parse ARP table to find MAC address for given IP
    for interface in arp_table_output:
        if interface['ip'] == ip_address:
            return interface['ip'], interface['mac']
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
interface, mac_address = find_interface_for_ip(search_ip)
if interface:
    print(f"The IP address {search_ip} is seen on interface {interface} with MAC address {mac_address}")
else:
    print(f"The IP address {search_ip} is not found in ARP or MAC address table.")

# close the connection
print(id(net_connect))
net_connect.close()
print(id(net_connect))
