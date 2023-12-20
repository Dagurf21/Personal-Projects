# Formula number i takes li lines and its importance is mi

# Input
#   first line
#       n   l  
# n = number of formulas
# l = how many lines fit on the sheet

# n lines follow for each formula
# each line has li and mi
# li = number of lines for formula
# mi = importance of formula


number_of_formulas, max_lines = map(int, input().split())

problem_list = []
for _ in range(number_of_formulas):
    #line amount, importancee
    x = list(map(int, input().split()))
    problem_list.append(x)



print ( problem_list)
