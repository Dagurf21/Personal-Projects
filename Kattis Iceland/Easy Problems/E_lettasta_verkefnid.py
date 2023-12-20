n, m = map(int, input().split())
problem_names = input().split()

max_points = 0
max_problem = ""


for i in range(m):
    points = list(map(int, input().split()))
    total_points = sum(points)

    if total_points > max_points:
        max_points = total_points
        max_problem = problem_names[points.index(max(points))]

print(max_problem)