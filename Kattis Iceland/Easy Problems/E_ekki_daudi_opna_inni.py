first_str = input()
second_str = input()

top_left = ""
bottom_left = ""
top_right = ""
bottom_right = ""

check_pipe = False
for char in first_str:
    if char == "|":
        check_pipe = True
    elif char != "|" and check_pipe == False:
        top_left += char
    else:
        top_right += char

check_pipe = False
for char in second_str:
    if char == "|":
        check_pipe = True
    elif char != "|" and check_pipe == False:
        bottom_left += char
    else:
        bottom_right += char



print (top_left + bottom_left, top_right + bottom_right)

        