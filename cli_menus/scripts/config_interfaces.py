from netmiko import ConnectHandler
import click

interfaces = ['Gi0/0', 'Gi0/1', 'Gi0/2', 'Gi0/3']

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.201',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin',
}

with ConnectHandler(**device) as net_connect:
    for int in interfaces:
        commands = [f'interface {int}', f'description this-port-is-{int}', 'no shut']
        net_connect.enable()
        output = net_connect.send_config_set(commands)
        print(output)
