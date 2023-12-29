##############################################
#       misunderstood the description        #
#          dont want to keep going           #
##############################################

num_of_people, first, second = map(int, input().split())

first_list = list(map(str, input().split()))
second_list = list(map(str, input().split()))

first_first_list = []
for x in range(first):
    name = input()
    first_first_list.append(name)

second_second_list = []
for x in range(second):
    name = input()
    second_second_list.append(name)

if first_list[0] == first_first_list[0]:
    print ("left")

elif first_list[-1] == first_first_list[-1]:
    print ("right")

if second_list[0] == second_second_list[0]:
    print ("left")
elif second_list[-1] == second_second_list[-1]:
    print ("right")
