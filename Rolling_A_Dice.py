import random
dice_values = [1,2,3,4,5,6]

def two_player_dice_game():
    roll_number_holder_1 = 1
    roll_number_holder_2 = 1
    player_1_score = 0
    player_2_score = 0
    print("Player 1 First!")
    for i in range(5):
        Player_1_roll_1 = random.choice(dice_values)
        print(f"You Rolled: {Player_1_roll_1}")
        Player_1_roll_2 = random.choice(dice_values)
        print(f"You Rolled: {Player_1_roll_2}")
        player_1_score += Player_1_roll_1 + Player_1_roll_2
        if Player_1_roll_1 == Player_1_roll_2:
            print("You Rolled Doubles! + 5 Points!")
            player_1_score += 5
        print(f"Roll {roll_number_holder_1}: {player_1_score}")
        roll_number_holder_1 += 1
    print("----------------------------------------")
    print("Now Player 2!")
    for i in range(5):
            Player_2_roll_1 = random.choice(dice_values)
            print(f"You Rolled: {Player_2_roll_1}")
            Player_2_roll_2 = random.choice(dice_values)
            print(f"You Rolled: {Player_2_roll_2}")
            player_2_score += Player_2_roll_1 + Player_2_roll_2
            if Player_2_roll_1 == Player_2_roll_2:
                print("You Rolled Doubles! + 5 Points!")
                player_2_score += 5
            print(f"Roll {roll_number_holder_2}: {player_2_score}")
            roll_number_holder_2 += 1
    print(f"Player 1 Final Score: {player_1_score}")
    print(f"Player 2 Final Score: {player_2_score}")
    if player_1_score > player_2_score:
        print(f"Player 1 is the WINNER with a score of {player_1_score}")
        print(f"Player 2 is the LOSER with a score of {player_2_score}")
    else:
        print(f"Player 2 is the WINNER with a score of {player_2_score}")
        print(f"Player 1 is the LOSER with a score of {player_1_score}")


two_player_dice_game()