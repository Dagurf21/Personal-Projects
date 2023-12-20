n = int(input())
tik_tikkers = {}

for _ in range(n):
    name, views = input().split()
    views = int(views)

    if name in tik_tikkers:
        tik_tikkers[name] += views
    else:
        tik_tikkers[name] = views

popular = max(tik_tikkers, key=tik_tikkers.get)

print (popular)