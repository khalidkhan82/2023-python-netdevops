with open("glfd-dcnfw-1a.txt", mode='r') as asa_config:
    lines = asa_config.readlines()

object_list = []
object_dict = {}
cmd_first_line = "object network nat83-"
cmd_second_line_host = "host "
cmd_second_line_subnet = "subnet "
cmd_third_line = "nat "

with open("asa-nat-dcnfw-1a.txt", mode='w') as output_file:
    for (i, line) in enumerate(lines):
        if line.startswith("static"):
            object_list = line.split()
            if object_list[5] in "255.255.255.255":
                output_file.writelines(f'{cmd_first_line}{object_list[3]}\n\t{cmd_second_line_host}{object_list[3]}\n\t'
                                       f'{cmd_third_line}{object_list[1]} {object_list[0]} {object_list[2]}\n')
            else:
                output_file.writelines(f'{cmd_first_line}{object_list[3]}\n\t{cmd_second_line_subnet}{object_list[3]} '
                                       f'{object_list[5]}\n\t{cmd_third_line}{object_list[1]} {object_list[0]} '
                                       f'{object_list[2]}\n')