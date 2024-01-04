"""
QUESTION 1: 
Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
Write a function to help Bob locate the card.
"""

# How to solve the problem ?
# 1. State the problem clearly
# 2. Come up with some example inputs & outputs TRY TO COVER ALL EDGE CASES
# 3. Come up with a correct solution for the problem
# 4. Implement the solution and test it using example inputs
# 5. Analyze the algorithms complexity and identify inefficiencies
# 6. apply the right technique to overcome the inefficiency. Repeat steps 3 to 6

# Problem
"""
we need to write a program to find the position of a give number in a list of numbers arranged in decreasing order
We also need to minimize the number of times we access elements from the list
"""

# Input 1,2 Output 3
"""
1. Cards : A list of number sorted in decreadsing order e.x. [13, 11, 10, 7, 4, 3, 1, 0]
2. Query : A number, whose position in the array is to obe determined. e.x. 7
3. Position : The position of the query in the list card e.x. 3 in the above case
"""

# 3. Come up with correct solution
"""
    1. create a variable <position> with the value 0
    2. check wether the numer at index position in cards equals query
    3. if it does position is the answer and can be returned from the function
    4. if not, increment the value of position by 1 and repeat steps 2 to 5 till we reach the last position
    5. if te number was not found return -1
    
"""

def locate_car(cards, query):
    # First position
    position = 0




#Example inputs
tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
         {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
         {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
         {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
         {'input': {'cards': [6], 'query': 6}, 'output': 0},
         {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
         {'input': {'cards': [], 'query': 7}, 'output': -1},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}]

print (locate_car(**tests["input"]) == tests["output"])

