from simple_term_menu import TerminalMenu


def device_selector():
    # define all the options for location and create the associated menue
    opt_location = ["PR", "CGH", "Bristol", "EDN"]
    menu_location = TerminalMenu(opt_location, title="Select the location of the device")
    menu_entry_index = menu_location.show()
    print(menu_entry_index)

    # define options for device type and create the associated menue
    opt_device_type = ["Core", "Distribution", "Access", "Management"]
    menu_device_type = TerminalMenu(opt_device_type, title=" Select the device type")
    print(menu_device_type)

    # define options for the Core Switches
    opt_pr_core_switches = ["lon-vpr-csw01", "lon-vpr-csw02", "lon-vpr-csw03"]
    menu_pr_core_switches = TerminalMenu(opt_pr_core_switches, title="Select core switch")

    # define options for the Core Switches
    opt_pr_mgmt_switches = ["lon-vpr-mgmt01", "lon-vpr-mtmt02"]
    menu_pr_mgmt_switches = TerminalMenu(opt_pr_mgmt_switches, title="Select core switch")

    

    #if menu_entry_index == 0:


if __name__ == "__main__":
    device_selector()