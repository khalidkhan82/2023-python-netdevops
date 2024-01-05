import napalm

import napalm


driver_iosxr = napalm.get_network_driver("ios")

CSR = {

    'hostname': 'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876',
    'timeout': 90
}

device_ios = driver_iosxr(**CSR)
device_ios.open()

print(device_ios.get_facts())









