def who_lost_bet(num_rounds_to_win, game_results):
    arnar_wins = 0
    hannes_wins = 0
    for result in game_results:
        if result == 'A':
            arnar_wins += 1
        else:
            hannes_wins += 1
        if arnar_wins == num_rounds_to_win:
            return "Hannes"
        elif hannes_wins == num_rounds_to_win:
            return "Arnar"

    

# Get input from user
num_rounds_to_win = int(input(""))
game_results = input("")

# Print the result
print(who_lost_bet(num_rounds_to_win, game_results))

