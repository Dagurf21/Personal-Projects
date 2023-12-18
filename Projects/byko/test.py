import csv

# Specify the path to your CSV file
csv_file_path = 'Dagurf21/Personal-Projects/Projects/byko/csvfile.csv'

# Open the CSV file
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the CSV data into a list of lists
    data = [row for row in csv_reader]

# Print the data
for row in data:
    print(row)
