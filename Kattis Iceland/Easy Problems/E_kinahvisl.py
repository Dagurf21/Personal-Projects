init_str = input()
final_str = input()

res = 1
for count, init_char in enumerate(init_str):
    if init_char == final_str[count]:
        pass
    else:
        res += 1

print (res)
