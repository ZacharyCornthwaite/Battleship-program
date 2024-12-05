#Zachary Cornthwaite
#Logan Harris
# 12/9/24
# Battleship game
# This is a simple battleship game that we created. It is a two player game where each player has a board with ships on it that they placed. The players take turns to hit the ships on the opponent's board. The player who hits all the ships first wins the game.

import time
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

def update_status(player_1_board, player_2_board, player_1_score, player_2_score):
    """
    It will update the status of the game after each player's turn. It will display the boards and scores of both players.
    """
    print("Player 1's Board:")
    print(player_1_board)
    print("Player 2's Board:")
    print(player_2_board)
    print(f"Player 1's Score: {player_1_score}")
    print(f"Player 2's Score: {player_2_score}")

def start_timer(duration):
    """
    Its a timer that will start when the player's turn starts and will end after 15 seconds. We wanted to add our own spin on the battship game with putting some pressure on each to not take to much time on their turn.
    """
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        remaining_time = end_time - time.time()
        print(f"Time left: {remaining_time:.2f} seconds", end='\r')
        time.sleep(1)
    print("\nTime's up!")

def player_turn(player_name):
    print(f"{player_name}'s turn. You have 15 seconds.")
    
    # Start the 15-second timer
    start_timer(15)
    
    # Simulate player's turn (replace this with actual game logic)
    turn_time = random.uniform(1, 15)  # counts the time it takes you to make a move and in the end it will help calculate the average time it took you.
    print(f"{player_name} completed the turn in {turn_time:.2f} seconds")
    
    return turn_time

def create_scatter_plot_with_logo():
    # Create some random data for the scatter plot
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    area = (30 * np.random.rand(50))**2  # 0 to 15 point radii

    # Create the scatter plot
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)

    # Add the Washington State University logo
    logo = mpimg.imread('C:/Users/zacha/OneDrive/Desktop/Python Projects/wsu_logo.png')
    plt.imshow(logo, aspect='auto', extent=[0.6, 1.0, 0.6, 1.0], zorder=-1)

    # Add the names
    plt.text(0.5, 1.05, 'Zachary Cornthwaite and Logan Harris', fontsize=12, ha='center', transform=plt.gca().transAxes)

    # Hide axes
    plt.axis('off')

    # Show the plot
    plt.show()

def create_plot_with_logo_and_names():
    # Add the Washington State University logo
    logo = mpimg.imread('C:/Users/zacha/OneDrive/Desktop/Python Projects/wsu_logo.png')
    plt.imshow(logo, aspect='auto', extent=[0.6, 1.0, 0.6, 1.0], zorder=-1)

    # Add the names
    plt.text(0.5, 1.05, 'Zachary Cornthwaite and Logan Harris', fontsize=12, ha='center', transform=plt.gca().transAxes)

    # Hide axes
    plt.axis('off')

    # Show the plot
    plt.show()

def calculate_score(board): 
    """
    It calculates the score of the player based on the number of ships hit.
    """
    return sum(cell == 2 for row in board for cell in row)

def count_ships_left(board):
    """
    It counts the number of ships left on the board.
    """
    return sum(cell == 1 for row in board for cell in row)

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
    
    player_1_turn_times = player_turn(player_1)
    player_2_turn_times = player_turn(player_2)
    
    game_over = False
    while not game_over:
        """
        a loop so that the game continues until one of the players wins. 
        """
        for player, opponent_board, turn_times in [(player_1, player_2_board, player_1_turn_times), (player_2, player_1_board, player_2_turn_times)]:
            valid_turn, row, col, elapsed_time = player_turn(player, opponent_board)
            turn_times.append(elapsed_time)
            if not valid_turn:
                game_over = True
                break
            if check_hit(opponent_board, row, col):
                print(f"{player} hit a ship at ({row}, {col})!")
            else:
                print(f"{player} missed at ({row}, {col}).")
            print_board(opponent_board)
            time.sleep(5)
            player_1_score = calculate_score(player_1_board)
            # Calculates the score and keeps it updated. 
            player_2_score = calculate_score(player_2_board)
            update_status(player_1_board, player_2_board, player_1_score, player_2_score)
            if player_1_score == sum([5, 4, 3, 3, 2]) or player_2_score == sum([5, 4, 3, 3, 2]):
                game_over = True
                break
            
        print("\nFinal Scoreboard:")
    update_status(player_1_board, player_2_board, player_1_score, player_2_score)
    
    player_1_ships_left = count_ships_left(player_1_board) 
    # Coutns the number of ships left so it will continue the game until all the ships left. 
    player_2_ships_left = count_ships_left(player_2_board)
    
    player_1_avg_time = sum(player_1_turn_times) / len(player_1_turn_times) if player_1_turn_times else 0
    # Calculates the average time it took you to make a move.
    player_2_avg_time = sum(player_2_turn_times) / len(player_2_turn_times) if player_2_turn_times else 0
    
    if player_1_score > player_2_score:
        print(f"{player_1} wins!")
        print(f"Average turn time: {player_1_avg_time:.2f} seconds")
        print(f"Ships left: {player_1_ships_left}")
    elif player_2_score > player_1_score:
        print(f"{player_2} wins!")
        print(f"Average turn time: {player_2_avg_time:.2f} seconds")
        print(f"Ships left: {player_2_ships_left}")
    else:
        print("It's a tie!")
        print(f"{player_1}'s average turn time: {player_1_avg_time:.2f} seconds")
        print(f"{player_1}'s ships left: {player_1_ships_left}")
        print(f"{player_2}'s average turn time: {player_2_avg_time:.2f} seconds")
        print(f"{player_2}'s ships left: {player_2_ships_left}")

    # Show end credits
    create_plot_with_logo_and_names()

if __name__ == "__main__":
    main()
