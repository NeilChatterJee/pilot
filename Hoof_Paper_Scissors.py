import random
def Hoof_Paper_Scissors():
    symbols = ["Rock", "Paper", "Scissors"]
    number_of_games_played = input("How many times have you played?")
    number_of_symbols = input("How many symbols are you going to play?")
    for number_of_games_played < 3000:
        player_1_input = input("Choose Rock, Paper, Or Scissors: ")
        player_1_input2 = input("Choose Rock, Paper, Or Scissors: ")
        player_2_input = input("Choose Rock, Paper, Or Scissors: ")
        player_2_input2 = input("Choose Rock, Paper, Or Scissors: ")
        player_1_final_choice = input(f"Choose between {player_1_input} and {player_1_input2}")
        player_2_final_choice = input(f"Choose between {player_2_input} and {player_2_input2}")
        if player_1_final_choice == "Rock" and player_2_final_choice == "Paper":
            print("The Winner Is Player 1")