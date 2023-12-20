servers = int(input())

cpus = 0
memory = 0
hard_disk = 0

for x in range(servers):
    input_list = input().split()
    if input_list[0] == "J":
        cpus += 1
    if input_list[1] == "J":
        memory += 1
    if input_list[2] == "J":
        hard_disk += 1
temp_list = [cpus, memory, hard_disk]
print (min(temp_list))

