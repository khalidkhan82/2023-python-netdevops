from simple_term_menu import TerminalMenu
import yaml

with open('hosts.yaml', 'r') as host_file:
    inventory = yaml.safe_load(host_file)

#print(inventory['CGH']['Core'])

def device_selector():
    # define all the options for location and create the associated menue
    opt_location = inventory['location']
    menu_location = TerminalMenu(opt_location, title="Select the location of the device")
    menu_entry_index = menu_location.show()
    #print(menu_entry_index)

    # define options for device type and create the associated menue
    opt_device_type = inventory['device_type']
    menu_device_type = TerminalMenu(opt_device_type, title=" Select the device type")
    menu_index_device_type = menu_device_type.show()
    #print(f"{inventory['device_type']}{['menu_index_device_type'}]")

    # define options for the Core Switches
    opt_switches = inventory[f'{opt_location[menu_entry_index]}'][f'{opt_device_type[menu_index_device_type]}']
    menu_switches = TerminalMenu(opt_switches, title="Select your switch switch")
    menu_index_switches = menu_switches.show()

    # define options for the Core Switches
    #opt_pr_mgmt_switches = ["lon-vpr-mgmt01", "lon-vpr-mtmt02"]
    #menu_pr_mgmt_switches = TerminalMenu(opt_pr_mgmt_switches, title="Select core switch")

    

    #if menu_entry_index == 0:


if __name__ == "__main__":
    device_selector()