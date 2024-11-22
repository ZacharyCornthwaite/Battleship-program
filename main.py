import time
import random
import matplotlib.pyplot as plt
import numpy as np

def update_status(player_1_board, player_2_board, player_1_score, player_2_score):
    print("Player 1's Board:")
    print(player_1_board)
    print("Player 2's Board:")
    print(player_2_board)
    print(f"Player 1's Score: {player_1_score}")
    print(f"Player 2's Score: {player_2_score}")

def calculate_score(board):
    return sum(cell == 2 for row in board for cell in row)

def main():
    print("Welcome to Battleship!")
    input("Press Enter to start the game.")
    
    player_1 = input("Enter a username (default player 1): ")
    if player_1 == "":
        player_1 = "player_1"
    player_2 = input("Enter a username (default player 2): ")
    if player_2 == "":
        player_2 = "player_2"
        
    chooser = random.choice([player_1, player_2])
    print(f"{chooser} goes first to choose heads or tails.")
    choice = input(f"{chooser}, do you want to be Heads or Tails: ").title()
    while choice != "Heads" and choice != "Tails":
        choice = input("Invalid choice. Please enter Heads or Tails: ").title()
    coin_flip = random.choice(["Heads", "Tails"])
    print(f"The coin landed on {coin_flip}")

    player_1_board = [[0] * 10 for _ in range(10)]
    player_2_board = [[0] * 10 for _ in range(10)]
    
    place_ships(player_1_board, player_1)
    place_ships(player_2_board, player_2)
    
    player_1_score = calculate_score(player_1_board)
    player_2_score = calculate_score(player_2_board)
    
    update_status(player_1_board, player_2_board, player_1_score, player_2_score)
    
    game_over = False
    while not game_over:
        for player, opponent_board in [(player_1, player_2_board), (player_2, player_1_board)]:
            valid_turn, row, col, hit = player_turn(player, opponent_board)
            if not valid_turn:
                game_over = True
                break
            if hit:
                print(f"{player} hit a ship at ({row}, {col})!")
            else:
                print(f"{player} missed at ({row}, {col}).")
            print_board(opponent_board)
            time.sleep(5)
            player_1_score = calculate_score(player_1_board)
            player_2_score = calculate_score(player_2_board)
            update_status(player_1_board, player_2_board, player_1_score, player_2_score)
            if player_1_score == sum([5, 4, 3, 3, 2]) or player_2_score == sum([5, 4, 3, 3, 2]):
                game_over = True
                break

    print("\nFinal Scoreboard:")
    update_status(player_1_board, player_2_board, player_1_score, player_2_score)
    if player_1_score > player_2_score:
        print(f"{player_1} wins!")
    elif player_2_score > player_1_score:
        print(f"{player_2} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
