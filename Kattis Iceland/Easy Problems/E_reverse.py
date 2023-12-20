num = int(input())

listi = []
for x in range(num):
    inp = int(input())
    listi.append(inp)

listi.reverse()
for x in listi:
    print(x)