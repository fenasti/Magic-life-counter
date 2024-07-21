class Player:
    """Define the name and the life points amount of each player"""
    def __init__(self, name, life_points):
        self.name = name
        self.life_points = life_points

def get_players_data():
    print("Welcome to the Magic: The Gathering life points counter!")
    print("Instructions:")
    print("1. Choose game mode, Standard or Comander.")
    print("2. Define each player names.")
    print("3. Roll a dice to find out who starts.")

    life_points = 0
    game_mode = input("Enter game mode:").lower()
    while if game_mode == "standard":
            life_points = 20
            break
        elif game_mode == "comander":
            life_points = 40
            break
        else:
            print("Invalid mode, choose 'Standard' or 'Comander'.")



    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    
    player1 = Player(player1_name, game_mode)
    player2 = Player(player2_name, game_mode)

    players = [player1, player2]
    

def adjust_life():
    pass

def roll_dice():
    pass

def main():

    



        break
        


main()