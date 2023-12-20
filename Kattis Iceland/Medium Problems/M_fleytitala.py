distance = float(input())
bounces = int(input())

total_distance = distance * (1 - (1/2)**(bounces + 1)) / (1 - 1/2)

print (total_distance)