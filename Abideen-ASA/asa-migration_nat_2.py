with open("glfd-pre-upgrade.txt", mode='r') as asa_config:
    lines = asa_config.readlines()

object_list = []
object_dict = {}
cmd_first_line = "object network obj-"
cmd_second_line = "nat "

with open("asa-converted_2.txt", mode='w') as output_file:
    for (i, line) in enumerate(lines):
        #if "object-group" in line:
        #if "object network" in line:
        if line.startswith("static"):
            #print(f'The line number is: {i}')
            #print(line)
            object_list=line.split()
            output_file.writelines(f'{cmd_first_line}{object_list[3]}\n\t{cmd_second_line}'
                                   f'{object_list[1]} {object_list[0]} {object_list[2]}\n')
            #object_dict["type"] = object_list[0]
            #object_dict["src_dst_int"] = object_list[1]
            #object_dict["dst"] = object_list[2]
            #object_dict["src"] = object_list[3]
            #print(object_dict)
            #print(f'{CMD_NAT_OBJECT_NETWORK}{object_dict["src"]}\n\t{cmd_second_line}{object_dict["src_dst_int"]}'
            #      f' static {object_dict["dst"]}')
            #output_file.writelines(f'{CMD_NAT_OBJECT_NETWORK}{object_dict["src"]}\n\t{cmd_second_line}'
            #                       f'{object_dict["src_dst_int"]} static {object_dict["dst"]}\n')

output_file.close()