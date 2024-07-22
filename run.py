import random

class Player:
    """Define the name and the life points amount of each player"""
    def __init__(self, name, life_points):
        self.name = name
        self.life_points = life_points

    def adjust_life(self, amount):
        self.life_points += amount
        
def print_ascii_art():
    art = """
         .AMMMMMMMMMMA.          
       .AV. :::.:.:.::MA.        
      A' :..        : .:`A       
     A'..              . `A.     
    A' :.    :::::::::  : :`A    
    M  .    :::.:.:.:::  . .M    
    M  :   ::.:.....::.:   .M    
    V : :.::.:........:.:  :V    
   A  A:    ..:...:...:.   A A   
  .V  MA:.....:M.::.::. .:AM.M   
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A  
:M .  .`VMMMMMMV.:A `VMMMMV .:M: 
 V.:.  ..`VMMMV.:AM..`VMV' .: V  
  V.  .:. .....:AMMA. . .:. .V   
   VMM...: ...:.MMMM.: .: MMV    
       `VM: . ..M.:M..:::M'      
         `M::. .:.... .::M       
          M:.  :. .... ..M       
 VK       V:  M:. M. :M .V       
          `V.:M.. M. :M.V'
    """
    print(art)



def get_players_data():

    def get_initial_life_points():
        while True:
            game_mode = input("Enter game mode (Standard or Commander):\n").lower()
            print()
            if game_mode == "standard":
                return 20
            elif game_mode == "commander":
                return 40
            else:
                print("Invalid mode, choose 'Standard' or 'Commander'.")
                

    game_mode = get_initial_life_points()

    player1_name = input("Enter the name of Player 1: \n")
    print()
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
            if player1.life_points <= 0:
                print(f"{player2.name} won!")
                break
        elif name.lower() == player2.name.lower():
            player2.adjust_life(new_score)
            if player2.life_points <= 0:
                print(f"{player1.name} won!")
                break
        else:
            print(f"No player found with the name {name}.")
            continue

        print("\nUpdated Life Points:")
        print(f"{player1.name} is {player1.life_points}lp")
        print(f"{player2.name} is {player2.life_points}lp")

def roll_dice(name1, name2):
    input("Press Enter to roll the dice and determine who starts...\n")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice rolls... {name1} rolled {dice1}, {name2} rolled {dice2}")
    while dice1 == dice2:
        print("It's a tie! Rolling the dice again...")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"New rolls... {name1} rolled {dice1}, {name2} rolled {dice2}")
            

def main():
    print("Welcome to the Magic: The Gathering life points counter!")
    print_ascii_art()
    print("Instructions:")
    print("1. Choose game mode, Standard (20lp) or Commander (40lp).")
    print("2. Define each player names.")
    print("3. Roll a dice to find out who starts.")
    print()
    player1, player2 = get_players_data()
    print()
    print("**************************************")
    print("\nPlayers Data:")
    print(f"{player1.name} starts with {player1.life_points}lp")
    print(f"{player2.name} starts with {player2.life_points}lp")
    print()
    print("**************************************")
    print()
    roll_dice(player1.name, player2.name)
    adjust_life(player1, player2)

main()