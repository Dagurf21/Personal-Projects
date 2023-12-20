a = int(input())
b = int(input())

num_of_dots = a * b

temp = ""
for x in range(b):
    inp = input()
    temp += inp


counter = temp.count(".")
print (counter / num_of_dots)