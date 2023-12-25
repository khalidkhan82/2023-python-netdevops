import os
from ncclient import manager
from rich import print

if __name__ == "__main__":

    device = {
        "host": "sandbox-iosxe-recomm-1.cisco.com",
        "port": 830,
        "username": "developer",
        "password": "lastorangerestoreball8876",
        "hostkey_verify": False,
    }
    # device["password"] = os.environ["PYNET_PASSWORD"]

    with manager.connect(**device) as nconf:
        print(list(nconf.server_capabilities))