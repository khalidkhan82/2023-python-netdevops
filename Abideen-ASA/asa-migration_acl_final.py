with open("glfd-pre-upgrade.txt", mode='r') as asa_config:
    lines = asa_config.readlines()

object_list = []
nat_objects = []
acl_list = []
object_dict = {}
cmd_first_line = "object network obj-"
cmd_second_line_host = "host "
cmd_second_line_subnet = "subnet "
cmd_third_line = "nat "
acl_list_join = []

with open("asa-acl-converted.txt", mode='a') as output_file:
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
            nat_objects.append(line.split())

with open("asa-acl-converted.txt", mode='a') as output_file:
    for (i, line) in enumerate(lines):
        if line.startswith("access-list ") and "remark" not in line:
            acl_list = line.split()
            for obj in nat_objects:
                nat_ip = obj[2]
                real_ip = obj[3]
                for (j, item) in enumerate(acl_list):
                    if item == nat_ip:
                        # print(j)
                        # print(acl_list)
                        acl_list[j] = real_ip
                        # print(acl_list)
                        # print(acl_list[j], nat_ip, real_ip)
                        acl_list_join = " ".join(acl_list)
                        output_file.writelines(acl_list_join)
                        output_file.writelines('\n')
                        continue
                    else:
                        pass

