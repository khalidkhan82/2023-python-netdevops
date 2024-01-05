import napalm
from tabulate import tabulate


driver_iosxr = napalm.get_network_driver("ios")

CSR = {

    'hostname': 'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876',
    'timeout': 90
}

device_ios = driver_iosxr(**CSR)
device_ios.open()
mac_table = device_ios.get_mac_address_table()
arp_output = device_ios.get_arp_table()
arp_table = [["interface", "mac", "ip", "age"]]
for output in arp_output:
    #print(output.keys())
    arp_table.append([output["interface"], output["mac"],
                      output["ip"], output["age"]])

#print(arp_table)
print(tabulate(arp_table, headers="firstrow"))
#print(mac_table,"\n", arp_table)