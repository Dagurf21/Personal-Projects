amount = int(input())

input_list = input().split()

some_str = ""

for x in input_list: 
    char = x[0]
    if char.isupper():
        some_str += char

print (some_str)