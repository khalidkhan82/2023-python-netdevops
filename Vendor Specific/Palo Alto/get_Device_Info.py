from panos.firewall import Firewall
from panos import network
import xml.etree.ElementTree as ET

fw = Firewall("192.168.1.155", api_username="apiadmin", api_password="Admin123")
response = fw.op("show system info")
hostname = response.find(".//hostname").text
ip = response.find(".//ip-address").text
new_hostname = "PA-FW01"
fw.add(new_hostname)
print(hostname, ip)