import random

def main():
    print("Welcome to Battleship!")
    input("Press Enter to start the game.")
    
    player_1 = input("Enter a username (default player 1): ")
    if player_1 == "":
        player_1 = "player_1"
    else:
        player_1 = player_1
    player_2 = input("Enter a username (default player 2): ")
    if player_2 == "":
        player_2 = "player_2"
    else:
        player_2 = player_2
        
    chooser = random.choice([player_1, player_2])
    print(f"{chooser} goes first to choose heads or tails.")
    choice = input(f"{chooser}, do you want to be Heads or Tails: ")
    while choice != "Heads" and choice != "Tails":
        choice = input("Invalid choice. Please enter Heads or Tails: ")
    coin_flip = random.choice(["Heads", "Tails"])
    print(f"The coin landed on {coin_flip}")
    if coin_flip == choice:
        print(f"{chooser} goes first!")
        place_ships(chooser)
    else:
        if chooser == player_1:
            chooser = player_2
        else:
            chooser = player_1
        print(f"{chooser} goes first!")
        place_ships(chooser)
        
main()
    