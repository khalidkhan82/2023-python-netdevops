import requests
import json
from urllib3.exceptions import InsecureRequestWarning   #Suppress HTTPS warnings
from urllib3 import disable_warnings

url = "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/ietf-interfaces:interfaces"
auth = ('developer', 'lastorangerestoreball8876')

# Suppress HTTPS warnings
# requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback11",
    "description": "Configured by RESTCONF",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "11.11.11.1",
          "netmask": "255.255.255.0"
        }
      ]
    }
  }
})
headers = {
  'Authorization': 'Basic ZGV2ZWxvcGVyOmxhc3RvcmFuZ2VyZXN0b3JlYmFsbDg4NzY=',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)