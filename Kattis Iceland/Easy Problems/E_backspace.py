original_string = input()
new_string = []

for char in original_string:
    if char == "<":
        if new_string:
            new_string.pop()
    else:
        new_string.append(char)

result_string = "".join(new_string)
print(result_string)
