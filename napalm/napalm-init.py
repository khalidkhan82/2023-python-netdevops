# 1. Import modules - napalm
# 2. Define host(s) with a dictionary
# 3. Instantiate the object of class NetworkDriver
# 4. Create a variable of type NetwokDriver object by passing the host dictionary as
# keyword (using **KWARGS)
# 5. Open the connection to the device using the 'open' method of the 
# NetworkDriver variable crrated in step 4.
# 6. Send commands to the device using the various available methods
# 7. Close the connection to the device using the 'close' method.


# 1. Import modules - napalm
import napalm


driver_iosxr = napalm.get_network_driver("ios-xr")

CSR = {

    'hostname': 'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876',
    'timeout': 90
}

device_ios = driver_iosxr(**CSR)
device_ios.open()
facts = device_ios.get_facts()
version = device_ios.cli(['show version'])
print(facts)
print(version)