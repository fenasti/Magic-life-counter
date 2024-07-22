class Player:
    """Define the name and the life points amount of each player"""
    def __init__(self, name, life_points):
        self.name = name
        self.life_points = life_points

    def adjust_life(self, amount):
        self.life_points += amount
        

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
    
def adjust_life(player1, player2):
    while True:
        get_new_score = input("\nEnter action (e.g., 'Player1 -3' to subtract 3 life points from Player1 or 'exit' to quit): \n")
        if get_new_score.lower() == "exit":
            break

        try:
            name, new_score = get_new_score.split()
            new_score = int(new_score)
        except ValueError:
            print("Invalid input. Please enter the action in the correct format.")
            continue

        if name.lower() == player1.name.lower():
            player1.adjust_life(new_score)
        elif name.lower() == player2.name.lower():
            player2.adjust_life(new_score)
        else:
            print(f"No player found with the name {name}.")
            continue

        print("\nUpdated Life Points:")
        print(player1.life_points)
        print(player2.life_points)

            



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

   # p1score = player1.life_points
   # p2score = player2.life_points
   # p1name = player1.name
   # p2name = player2.name

   # player_one = [p1name, p1score]
   # player_two = [p2name, p2score]
    adjust_life(player1, player2)


main()