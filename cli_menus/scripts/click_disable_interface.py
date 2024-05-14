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

def int_status(net_connect, int):
    output = net_connect.send_command(f'show interface {int} description')
    print(output)
    return output

@click.command()
@click.option("--interface", prompt="Enter the interface")
def config_interface(interface):
    with ConnectHandler(**device) as net_connect:
        net_connect.enable()
        status = int_status(net_connect, interface)
        print(status)
        if 'up' in status:
            shut = [f'interface {interface}', 'shut']
            output = net_connect.send_config_set(shut)
        else:
            no_shut = [f'interface {interface}', 'no shut']
            output = net_connect.send_config_set(no_shut)

if __name__ == '__main__':
    config_interface()