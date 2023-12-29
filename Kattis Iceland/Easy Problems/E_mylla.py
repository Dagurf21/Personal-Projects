first_line = input()
second_line = input()
third_line = input()

left_side = first_line[0] + second_line[0] + third_line[0]
middle_side = first_line[1] + second_line[1] + third_line[1]
right_side = first_line[2] + second_line[2] + third_line[2]

middle_down = first_line[0] + second_line[1] + third_line[2]
other_middle_down = first_line[2] + second_line[1] + third_line[0]

if first_line == "OOO":
    print ("Jebb")

elif second_line == "OOO":
    print ("Jebb")

elif third_line == "OOO":
    print ("Jebb")

elif left_side == "OOO":
    print ("Jebb")

elif middle_side == "OOO":
    print ("Jebb")

elif right_side == "OOO":
    print ("Jebb")

elif middle_down == "OOO":
    print ("Jebb")

elif other_middle_down == "OOO":
    print ("Jebb")

else:
    print ("Neibb")