class Player:
    """Define the name and the life points amount of each player"""
    def __init__(self, name, life_points):
        self.name = name
        self.life_points = life_points

def get_players_data():

    def get_initial_life_points():
        while True:
            game_mode = input("Enter game mode (Standard or Commander): ").lower()
            if game_mode == "standard":
                return 20
            elif game_mode == "commander":
                return 40
            else:
                print("Invalid mode, choose 'Standard' or 'Commander'.")

    game_mode = get_initial_life_points()

    player1_name = input("Enter the name of Player 1: \n")
    player2_name = input("Enter the name of Player 2: \n")
    
    player1 = Player(player1_name, game_mode)
    player2 = Player(player2_name, game_mode)

    return player1, player2
    
def adjust_life(p1, p2):
    while True:
        get_new_score = input("\nEnter action (e.g., 'Player1 -3' to subtract 3 life points from Player1 or 'exit' to quit): \n")
        if get_new_score.lower() == "exit":
            break
        else:
            name, new_score = get_new_score.split()
            print(new_score)



def roll_dice():
    pass

def main():
    print("Welcome to the Magic: The Gathering life points counter!")
    print("Instructions:")
    print("1. Choose game mode, Standard or Commander.")
    print("2. Define each player names.")
    print("3. Roll a dice to find out who starts.")

    player1, player2 = get_players_data()
    print("*********************************")
    print("\nPlayer Data:")
    print(player1.name, player1.life_points)
    print(player2.name, player2.life_points)
    p1score = player1.life_points
    p2score = player2.life_points
    new_score = adjust_life(p1score, p2score)


main()