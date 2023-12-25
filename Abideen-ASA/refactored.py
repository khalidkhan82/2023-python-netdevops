def read_file(file_name):
    with open(file_name, mode='r') as file:
        return file.readlines()

def write_file(file_name, content):
    with open(file_name, mode='a') as file:
        file.writelines(content)

def process_static_lines(lines):
    nat_host_list = []
    nat_subnet_list = []
    for line in lines:
        if line.startswith("static"):
            if "255.255.255.255" in line:
                nat_host_list.append(line.split())
            else:
                nat_subnet_list.append(line.split())
    return nat_host_list + nat_subnet_list

def process_object_group_lines(lines):
    obj_group_list = []
    nested_obj_group_list = []
    for i, line in enumerate(lines):
        if line.startswith("object-group"):
            nested_obj_group_list.append(" ".join(line.split()))
            n = i + 1
            to_find_obj = "network-object"
            to_find_acl = "access-list"
            while n < len(lines) and to_find_obj in lines[n]:
                if to_find_acl not in lines[n]:
                    obj_group_list.append(" ".join(lines[n].split()))
                    n += 1
                else:
                    break
    return obj_group_list, nested_obj_group_list

def refactor_code():
    lines = read_file("glfd-pre-upgrade.txt")
    nat_objects_list = process_static_lines(lines)
    obj_group_list, nested_obj_group_list = process_object_group_lines(lines)

    cmd_first_line = "object network nat83-"
    cmd_second_line_host = "host "
    cmd_second_line_subnet = "subnet "
    cmd_third_line = "nat "
    cmd_network_object = "network-object"

    with open("asa-obj-and-group-converted.txt", mode='a') as output_file:
        for line in nat_objects_list:
            if "255.255.255.255" in line:
                output_file.writelines(f'{cmd_first_line}{line[3]}\n\t{cmd_second_line_host}{line[3]}'
                                       f'\n\t{cmd_third_line}{line[1]} {line[0]} '
                                       f'{line[2]}\n')
            else:
                output_file.writelines(f'{cmd_first_line}{line[3]}\n\t{cmd_second_line_subnet}{line[3]}'
                                       f'\n\t{cmd_third_line}{line[1]} {line[0]} '
                                       f'{line[2]}\n')

        for line in obj_group_list:
            if "object-group" in line:
                output_file.writelines(line)
                output_file.writelines('\n')
            elif "description" in line or "network-object" in line:
                output_file.writelines('\t')
                output_file.writelines(line)
                output_file.writelines('\n')

refactor_code()