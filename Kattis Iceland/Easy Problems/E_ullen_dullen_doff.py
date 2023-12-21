friends = int(input())

friends_list = input().split()

while len(friends_list) < 13:
    friends_list.extend(friends_list)

print (friends_list[12])

