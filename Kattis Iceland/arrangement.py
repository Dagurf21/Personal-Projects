rooms = int(input())
teams = int(input())

for room in range(rooms):
    stars_per_line = min(teams, (teams + rooms - 1 - room) // (rooms - room))
    print("*" * stars_per_line)
    teams -= stars_per_line