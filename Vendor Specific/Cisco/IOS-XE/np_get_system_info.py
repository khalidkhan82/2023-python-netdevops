import napalm
from netmiko import ConnectHandler
from box import Box

host = {
    "hostname": "192.168.1.153",
    "username": "admin",
    "password": "Admin123",
    "timeout": 90,
    "optional_args": {
        "global_delay_factor": 4,
        "secret": "Admin123"
    }
}

#facts = Box({})

driver = napalm.get_network_driver("ios")

device = driver(**host)

device.open()

facts = Box(device.get_facts())
facts.new_value = "test"

version = device.cli(['show version'])

print(facts.new_value)
#print(facts.keys()) # ['uptime', 'vendor', 'os_version', 'serial_number', 'model', 'hostname', 'fqdn', 'interface_list']
#print(version)

device.close()