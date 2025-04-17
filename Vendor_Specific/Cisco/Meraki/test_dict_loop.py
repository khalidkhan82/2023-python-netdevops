students = {"cambridge": ["khalid", "zuqqi", "shahbaz", "Abideen", "Shami"], "birmingham": ["zuqqi", "Shami", "Ahsan", "Naveed"], 
            "Bradford": ["Abideen", "Noman", "Naveed", "Shahaz", "Ahsan"]}

for list in students.values():
    print(len(list))


for city, friends in students.items():
    for friend in friends:
        for value in students.values():
            if friend not in value:
                value.append(friend)

#print(students)

for list in students.values():
    print(len(list))
