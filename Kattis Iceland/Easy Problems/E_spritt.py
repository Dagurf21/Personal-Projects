classrooms, bottles = map(int, input().split())

summa = 0
for _ in range(classrooms):
    x = int(input())
    summa += x

if summa <= bottles:
    print ("Jebb")
else:
    print ("Neibb")