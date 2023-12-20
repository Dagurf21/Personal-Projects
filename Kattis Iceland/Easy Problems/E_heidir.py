
wind_speed = int(input()) 
num_of_roads = int(input())

listi = []
for x in range(num_of_roads):
    temp = []
    name, wind = map(str, input().split())
    wind = int(wind)
    temp.append(name)
    temp.append(wind)
    listi.append(temp)

for road in listi:
    if road[1] >= wind_speed:
        print (road[0], "opin")
    else:
        print (road[0], "lokud")