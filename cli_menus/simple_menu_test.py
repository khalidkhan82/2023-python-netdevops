from simple_term_menu import TerminalMenu

def main():
    main_options = ["entry 1", "entry 2", "entry 3"]
    first_options = ["entry a", "entry b", "entry b"]
    second_options = ["entry a", "entry b", "entry b"]
    third_options = ["entry a", "entry b", "entry b"]
    main_terminal_menu = TerminalMenu(main_options, title="Main Options")
    menu_entry_index = main_terminal_menu.show()
    print(menu_entry_index)
    if menu_entry_index == 0:
        first_terminal_menu = TerminalMenu(first_options, title="First Options")
        first_menu_entry_index = first_terminal_menu.show()
        print(f"You have selected {first_options[first_menu_entry_index]} in {main_options[menu_entry_index]}!")
    elif menu_entry_index == 1:
        second_terminal_menu = TerminalMenu(second_options, title="Second Options")  
        second_menu_entry_index = second_terminal_menu.show()
        print(f"You have selected {second_options[second_menu_entry_index]} in {main_options[menu_entry_index]}!")
    elif menu_entry_index == 3:
        third_terminal_menu = TerminalMenu(third_options, title="Third Options")      
        third_menu_entry_index = third_terminal_menu.show()                          
        print(f"You have selected {third_options[third_menu_entry_index]} in {main_options[menu_entry_index]}!")

if __name__ == "__main__":
    main()