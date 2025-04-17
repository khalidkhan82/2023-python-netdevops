import csv
import yaml
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_napalm.plugins.tasks import napalm_get

# Load device details from YAML
def load_hosts_from_yaml(file_path="hosts.yaml"):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    return data["hosts"]

# Initialize Nornir dynamically with loaded hosts
def init_nornir(hosts_data):
    return InitNornir(inventory={"plugin": "DictInventory", "options": {"hosts": hosts_data}})

# Function to get device info
def get_device_info(task: Task):
    result = task.run(napalm_get, getters=["facts", "interfaces_ip"])
    
    facts = result.result["facts"]
    interfaces = result.result["interfaces_ip"]
    
    # Try management interface first, fallback to GigabitEthernet0/0
    ip_address = None
    for iface in ["Mgmt0", "Management1", "GigabitEthernet0/0"]:
        if iface in interfaces and "ipv4" in interfaces[iface]:
            ip_address = list(interfaces[iface]["ipv4"].keys())[0]
            break
    
    return Result(
        host=task.host,
        result={"Hostname": facts["hostname"], "Model": facts["model"], "IP Address": ip_address or "Not Found"},
    )

# Main function
def main():
    hosts_data = load_hosts_from_yaml()
    nr = init_nornir(hosts_data)
    results = nr.run(task=get_device_info)

    # Save to CSV
    output_file = "device_info.csv"
    with open(output_file, mode="w", newline="") as file:
        fieldnames = ["Hostname", "Model", "IP Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for host, result in results.items():
            if not result.failed:
                writer.writerow(result.result)

    print(f"Device info saved to {output_file}")

if __name__ == "__main__":
    main()