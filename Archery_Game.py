'''
Rules of Archery
1. Its a multiple player Game
2. There are multiple layers with different of each layer
3. There are number of chance
'''
class Player:
    def __init__(self, name, score, chances, chances_left):
        self.name = name
        self.score = score  
        self.chances = chances
        self.chances_left = chances_left
    
    def __str__(self):
        return f"player = {self.name}, player_score = {self.score}, player_number_of_chances_left = {self.chances_left}"

class Archery:
    def __init__(self):
        self.players = []
        self.rounds = int(input("How Many Rounds Would You Like To Play?: "))
        self.maximum_chances = int(input("How Many Chances Should Each Player Have?: "))
        People_Participating = input("Please Input People In List, Comma Separated: ")
        playerlist = People_Participating.strip().split(",")
        
        for name in playerlist:
            player = Player(name, 0, self.maximum_chances, self.maximum_chances)
            self.players.append(player)


        self.layers = {
            'Y': 10,
            'R': 8,
            'B': 6,
            'D': 0  
        }

    def print_player_data(self):
        for player in self.players:
            print(player)

    def print(self):
        self.print_player_data()
        print(f"Scoring: {self.layers}")
        print(self.maximum_chances)

    def shoot(self):
        for r in range(self.rounds):
            for player in self.players:
                for i in range(self.maximum_chances):
                    print(f"Player Name: {player.name}")
                    What_Color_Did_You_Shoot = input("Please Tell Us What Color You Shot: Yellow, Red, Black, Drop: ").upper()
                    Score = self.layers[What_Color_Did_You_Shoot]
                    player.score += Score
                    player.chances_left -= 1
                    print(f"Player Total Score: {player.score}")
                    print(f"Player's Chances Left: {player.chances_left}")
   

    def Winner(self):
        current_winning_score = -1
        current_winner = None
        for player in self.players:
            if player.score > current_winning_score:
                current_winning_score = player.score
                current_winner = player.name
        print(f"Current Top Score: {current_winning_score}")
        print(f"Winner: {current_winner}")


    def Loser(self):
        current_worst_score = 100
        current_worst_player = None
        for player in self.players:
            if player.score < current_worst_score:
                current_worst_score = player.score
                current_worst_player = player.name
        print(f"Current Bottom Score: {current_worst_score}")
        print(f"Current Bottom Scorer: {current_worst_player}")
            
            



print("OKAY")
archery = Archery()
archery.print()
print("!Note that Y = Yellow, R = Red, B = Black, D = Drop!")
archery.shoot()
archery.print()
archery.Winner()
archery.Loser()