sith = input()

a = int(input())
b = int(input())
c = int(input())

absolute = abs(a - b)
notabs = a - b

if absolute == notabs:
    print ("VEIT EKKI")
elif c == abs(a - b):
    print ("SITH")
else:
    print ("JEDI")