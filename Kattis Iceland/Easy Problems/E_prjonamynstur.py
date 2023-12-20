lines, char_amount = map(int, input().split())

str_inp = ""
for _ in range(lines):
    str_inp += input()

yarn = 0

for char in str_inp:
    if char == ".":
        yarn += 20
    elif char == "O":
        yarn += 10
    elif char == "/" or char == "\\":
        yarn += 25
    elif char == "A":
        yarn += 35
    elif char == "^":
        yarn += 5
    elif char == "v":
        yarn += 22

print (yarn)
