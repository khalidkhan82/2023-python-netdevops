from netmiko import ConnectHandler

device = {"device_type": "cisco_ios", 
          "host": "192.168.1.103",
          "username": "admin",
          "password": "admin",
          "secret": "admin"
          }

net_connect = ConnectHandler(**device)
net_connect.enable()
command = "show run"
print(net_connect.send_command(command))

#print(net_connect.find_prompt())

