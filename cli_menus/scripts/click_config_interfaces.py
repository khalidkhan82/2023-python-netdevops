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

@click.command()
@click.option("--interface", prompt="Enter the interface")
def config_interface(interface):
    with ConnectHandler(**device) as net_connect:
        commands = [f'interface {interface}', f'description new-click-this-port-is-{interface}', 'no shut']
        net_connect.enable()
        old_description = net_connect.send_command(f'show int {interface} description')
        print("the old_description is \n" + old_description)
        output = net_connect.send_config_set(commands)
        new_description = net_connect.send_command(f'show int {interface} description')
        print("The new_description is \n" + new_description)

if __name__ == '__main__':
    config_interface()