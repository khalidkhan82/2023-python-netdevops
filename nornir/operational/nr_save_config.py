from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.plugins.tasks import netmiko_save_config

nr = InitNornir(
    config_file="2023-python-netdevops/nornir/config.yaml", dry_run=True
)

results = nr.run(
    task=netmiko_save_config, confirm = True, confirm_response = "yes"
)
print_result(results)
