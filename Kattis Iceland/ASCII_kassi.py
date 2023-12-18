size = int(input())
top = ""

for _ in range(size):
    top += "-"

print (f"+{top}+")
for x in range(size):
    print( "|" + " " * size + "|" )
print (f"+{top}+")

