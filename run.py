class Player:
    """Define the name and the life points amount of each player"""
    def __init__(self, name, life_points):
        self.name = name
        self.life_points = life_points

def adjust_life():
    pass

def roll_dice():
    pass

def main():

    run_game = True

    while run_game:
        print("Welcome to the Magic: The Gathering life points counter!")
        print("Instructions:")
        print("1. Choose game mode, Standard or Comander.")
        print("2. Define each player names.")
        print("3. Roll a dice to find out who starts.")


        game_mode = input("Enter game mode:").lower()
        if game_mode == "standard":
            life_points = 20
            return life_points
        elif game_mode == "comander":
            life_points = 40
            return life_points
        else:
            print("Invalid mode, choose 'Standard' or 'Comander'.")
            


        player1_name = input("Enter the name of Player 1: ")
        player2_name = input("Enter the name of Player 2: ")
        
        player1 = Player(player1_name, game_mode)
        player2 = Player(player2_name, game_mode)

        players = [player1, player2]



        break
        


main()