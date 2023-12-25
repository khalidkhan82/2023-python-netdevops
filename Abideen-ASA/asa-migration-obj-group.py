lines = []

with open("glfd-pre-upgrade.txt", mode='r') as asa_config:
    lines = asa_config.readlines()

nat_host_list = []
nat_subnet_list = []
obj_group_list = []
nested_obj_group_list = []
CMD_NAT_OBJECT_NETWORK = "object network nat83-"
CMD_NAT_HOST = "host "
CMD_NAT_SUBNET = "subnet "
cmd_third_line = "nat "
cmd_network_object = "network-object"

for (i, line) in enumerate(lines):
    if line.startswith("static"):
        if "255.255.255.255" in line:
            nat_host_list.append(line.split())
        else:
            nat_subnet_list.append(line.split())

nat_objects_list = nat_host_list + nat_subnet_list

for (j, line) in enumerate(lines):
    if line.startswith("object-group"):
        nested_obj_group_list.append(" ".join(lines[j].split()))
        n = j + 1
        to_find_obj = "network-object"
        to_find_acl = "access-list"
        for to_find_obj in lines[n]:
            if to_find_acl not in lines[n]:
                obj_group_list.append(" ".join(lines[n].split()))
                n += 1
                continue
            else:
                break

for nat_object in nat_objects_list:
    # print(nat_object[2])
    for (i, obj_group) in enumerate(obj_group_list):
        if nat_object[2] in obj_group:
        # if nat_object[2] in obj_group and nat_object[2] != nat_object[3]:
            obj_group_list.insert(i-1, nat_object[3])
            break

with open("asa-obj-and-group-converted.txt", mode='a') as output_file:
    for line in nat_objects_list:
        if "255.255.255.255" in line:
            output_file.writelines(f'{CMD_NAT_OBJECT_NETWORK}{line[3]}\n\t{CMD_NAT_HOST}{line[3]}'
                                   f'\n\t{cmd_third_line}{line[1]} {line[0]} '
                                   f'{line[2]}\n')
        else:
            output_file.writelines(f'{CMD_NAT_OBJECT_NETWORK}{line[3]}\n\t{CMD_NAT_SUBNET}{line[3]}'
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

