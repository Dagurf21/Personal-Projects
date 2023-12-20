# Read the input data
num_problems = int(input())
num_teams = int(input())
problem_names = input().split()
    
# Initialize points for each problem
points_for_problem = [0] * num_problems

# Read points for each team
for _ in range(num_teams):
    points = list(map(int, input().split()))
    for i in range(num_problems):
        points_for_problem[i] += points[i]

# Find the problem with the maximum total points
max_points = max(points_for_problem)
max_problem = problem_names[points_for_problem.index(max_points)]

# Print the name of the problem with the highest total points
print(max_problem)