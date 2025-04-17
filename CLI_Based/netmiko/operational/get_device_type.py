from netmiko import ConnectHandler
from napalm import get_network_driver

# Define device list
devices = [
    {"device_type": "cisco_ios", "host": "10.32.255.41", "username": "khalidm", "password": "ButterCheese23!", "secret": "ButterCheese23!"},
]

# Function to get device type
def get_device_type(device):
    try:
        # Netmiko connection
        conn = ConnectHandler(**device)
        conn.enable()
        output = conn.send_command("show version", use_textfsm=True)
        conn.disconnect()

        # Napalm parsing
        driver = get_network_driver(device["device_type"].split("_")[1])
        napalm_device = driver(device["host"], device["username"], device["password"])
        napalm_device.open()
        facts = napalm_device.get_facts()
        napalm_device.close()

        return {"hostname": facts["hostname"], "model": facts["model"], "vendor": facts["vendor"]}
    
    except Exception as e:
        return {"error": str(e)}

# Get results for all devices
for dev in devices:
    print(get_device_type(dev))