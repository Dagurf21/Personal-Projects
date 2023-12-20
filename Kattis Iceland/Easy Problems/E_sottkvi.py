# Read the first line of input to get n, d, and today
n, d, today = map(int, input().split())

# Initialize count of friends who can attend the party
count = 0

# Read each friend's quarantine day and check if they will be free on the birthday
for _ in range(n):
    q_day = int(input().strip())  # Read each friend's quarantine day
    if q_day <= d - today:  # Check if the friend is free on or before the birthday
        count += 1

# Print the count of friends who can attend the party
print(count)