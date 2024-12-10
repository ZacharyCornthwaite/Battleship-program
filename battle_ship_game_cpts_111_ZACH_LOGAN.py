### Zachary Cornthwaite
### Logan Harris
### 12/9/24
### Battleship game
### This is a simple battleship game that we created. It is a two player game where each player has a board with ships on it that they placed. 
### The players take turns to hit the ships on the opponent's board. The player who hits all the ships first wins the game.


import matplotlib.pyplot as plt
import random
import time

'''
Void function that visualize the board using matplotlib. Creates a 10x10 board with grid lines and markers for ships. Creates a legend for the ship types/hits and misses. 
Takes a "board" input which is a 10x10 list of strings representing the board state. 
This function will be used to visualize the board after each ship placement and after each turn in the main game loop in main().
It also will be called by the place_ships() function to visualize the board after each ship placement.
'''
def visualize_board(board):
    plt.figure(figsize=(10, 10))
    
    ### Plot grid lines
    for i in range(1, 12):
        plt.axhline(y=i, color='gray', linestyle='-', alpha=0.3)
        plt.axvline(x=i, color='gray', linestyle='-', alpha=0.3)
    
    ### Set colors and labels for ships
    colors = {'C': 'gray', 'B': 'blue', 'R': 'green', 'S': 'red', 'D': 'purple', 
             ' ': 'white', 'H': 'yellow', 'M': 'black'}
    labels = {'C': 'Carrier', 'B': 'Battleship', 'R': 'Cruiser', 'S': 'Submarine', 
             'D': 'Destroyer', 'H': 'Hit', 'M': 'Miss'}
    
    ### Plot ships
    for i in range(10):
        for j in range(10):
            ship_type = board[i][j]
            plt.scatter(j + 1, i + 1, color=colors[ship_type], s=100)
    
    ### Create legend
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                                markerfacecolor=colors[key], markersize=10, 
                                label=labels[key]) 
                     for key in labels if key != ' ']
    plt.legend(handles=legend_elements, loc='upper right')
    
    ### Set axis limits and labels
    plt.xlim(0.5, 10.5)
    plt.ylim(10.5, 0.5)  ### Reverse the y-axis to match the board
    
    ### Set x-axis ticks (1-10)
    plt.xticks(range(1, 11))
    
    ### Set y-axis ticks (A-J)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    plt.yticks(range(1, 11), letters)
    
    ### Set x-axis label on top, similar to battleship board
    ax = plt.gca()
    ax.xaxis.set_label_position('top')
    ax.xaxis.tick_top()
    
    plt.xlabel('Number')
    plt.ylabel('Letter')
    plt.title('Battleship Board', pad=20)
    plt.show()

'''
Non-void function that returns "board" per the player parameter that is it given (determined by the coin_flip in main). Asks the player to create a board by placing their ships.
Shows the board after each placement and asks for confirmation. If the player is not satisfied with the placement, they can try again.
If the ship goes out of bounds or overlaps with another ship, the player is asked to try again. If any input is invalid, the player is asked to try again.
This function should only be called twice by main() to get the boards for both players at the start of the game.
'''
def place_ships(player):
    print(player + ", place your ships.")
    ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    ship_lengths = [5, 4, 3, 3, 2]
    ship_codes = {'Carrier': 'C', 'Battleship': 'B', 'Cruiser': 'R', 
                 'Submarine': 'S', 'Destroyer': 'D'}
    
    ### Initialize the board (10x10 grid)
    board = [[" " for _ in range(10)] for _ in range(10)]
    
    ### Dictionary to convert row letters to numbers
    letter_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 
                    'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    
    ### Place each ship
    for i in range(len(ships)):
        while True:
            print(f"\
Place your {ships[i]} ({ship_lengths[i]} spaces).")
            
            ### Create a temporary board for visualization
            temp_board = [row[:] for row in board]
            
            try:
                ### Get input in Battleship coordinates
                row_letter = input("Enter row (A-J): ").upper()
                col = int(input("Enter column (1-10): "))
                orientation = input("Enter orientation (H for horizontal, V for vertical): ").upper()
                
                ### Validate row letter
                if row_letter not in letter_to_num:
                    print("Invalid row. Please enter a letter A-J.")
                    continue
                
                ### Convert to array indices
                array_row = letter_to_num[row_letter]
                array_col = col - 1  ### Convert to 0-based index
                
                ### Validate column input
                if col < 1 or col > 10:
                    print("Invalid column. Please enter a number between 1 and 10.")
                    continue
                
                ### Check if ship is already placed in the selected location
                if orientation == "H":
                    if array_col + ship_lengths[i] > 10:
                        print("Ship is out of bounds. Try again.")
                        continue
                    if any(temp_board[array_row][array_col + j] != " " 
                          for j in range(ship_lengths[i])):
                        print("Ship overlaps with another ship. Try again.")
                        continue
                    for j in range(ship_lengths[i]):
                        temp_board[array_row][array_col + j] = ship_codes[ships[i]]
                
                elif orientation == "V":
                    if array_row + ship_lengths[i] > 10:
                        print("Ship is out of bounds. Try again.")
                        continue
                    if any(temp_board[array_row + j][array_col] != " " 
                          for j in range(ship_lengths[i])):
                        print("Ship overlaps with another ship. Try again.")
                        continue
                    for j in range(ship_lengths[i]):
                        temp_board[array_row + j][array_col] = ship_codes[ships[i]]
                
                else:
                    print("Invalid orientation. Try again.")
                    continue
                
                ### Visualize the board with the new ship placement
                visualize_board(temp_board)
                
                ### Ask for confirmation
                confirm = input("Is this placement acceptable? (Y/N): ").upper()
                if confirm == 'Y':
                    board = temp_board
                    break
                else:
                    print("Place your ship again.")
                    continue
                
            except ValueError:
                print("Invalid input. Please enter a letter (A-J) for row and number (1-10) for column.")
    
    print("\
Here is your final board placement:")
    visualize_board(board)
    return board


'''
Void function that takes the player, the opponent's board, and the tracking board as inputs. The player is asked to enter coordinates, and the function checks if the position was 
already fired upon. If the position was already fired upon, the player is asked to try again. If the position was not fired upon, the function checks if the position is a hit or a miss.
If it is a hit, the player is notified and the tracking board is updated with an 'H'. If it is a miss, the player is notified and the tracking board is updated with an 'M'.
Does not communicate which ship is sunk, only updates the board with H or M.
'''
def take_turn(player, opponent_board, tracking_board):
    print(f"\
{player}'s turn to fire!")
    print("\
Your tracking board (where you've fired):")
    visualize_board(tracking_board)
    
    while True:
        try:
            row_letter = input("Enter target row (A-J): ").upper() ### Targeting row
            col = int(input("Enter target column (1-10): ")) ### Targeting column
            
            ### Convert coordinates
            letter_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 
                           'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
            
            if row_letter not in letter_to_num: ### Error handling for invalid row
                print("Invalid row. Please enter a letter A-J.")
                continue
                
            array_row = letter_to_num[row_letter] ### Convert row letter to array index
            array_col = col - 1 ### Convert column number to 0-based index
            
            if col < 1 or col > 10: ### Error handling for invalid column
                print("Invalid column. Please enter a number between 1 and 10.")
                continue
                
            ### Check if this position was already fired upon
            if tracking_board[array_row][array_col] in ['H', 'M']:
                print("You've already fired at this position! Try again.")
                continue
                
            ### Check hit or miss
            if opponent_board[array_row][array_col] != ' ':
                print("\
HIT!")
                tracking_board[array_row][array_col] = 'H' ### Update tracking board with hit
                return True, (array_row, array_col)
            else:
                print("\
Miss!")
                tracking_board[array_row][array_col] = 'M' ### Update tracking board with miss
                return False, (array_row, array_col)
                
        except ValueError: ### Error handling for invalid input
            print("Invalid input. Please enter a letter (A-J) for row and number (1-10) for column.")


'''
Void function that takes the player and the tracking board as inputs. Prints the player's name and the tracking board. The tracking board shows the player's hits and misses.
Done at the end of each turn to show the player's progress. Prints a legend for the tracking board, calls the visualization function to show the board.
'''
def status_update(player, tracking_board):
    print(f"\
{player}'s Status Update:")
    visualize_board(tracking_board)
    print("Legend: H = Hit, M = Miss")


'''
Void time function to get the current time in seconds, with no inputs. Used to calculate the total game time at the end of the game. Editted due to the complexity of forcing a turn timer due to
the fact that matplotlib essentially "pauses" the game.
'''
def turn_time():
    return time.time()

'''
Non-void function that takes the board state and checks to see if a user won or not. Returns True if the game is over (all ships are sunk), and False if the game is not over.
Ran after each players turn. If the game is over, the game ends and the final scoreboard is printed.
'''
def check_game_over(board):
    ship_codes = {'C', 'B', 'R', 'S', 'D'}
    for row in board:
        for cell in row:
            if cell in ship_codes:
                return False
    return True

'''
Void function that takes the winner, player names, hits, and total time as inputs. Prints the final scoreboard at the end of the game. Ran by main() once the game is over 
by the check_game_over() function. Prints the winner, final statistics, and the total game time.
'''
def final_scoreboard(winner, p1_name, p2_name, p1_hits, p2_hits, total_time): ### Pretty self-explanatory function. Pritns out some headers and stats that are tracked by main().
    print("\
=== GAME OVER ===")
    print(f"\
Winner: {winner}!")
    print(f"\
Final Statistics:")
    print(f"{p1_name}'s hits: {p1_hits}")
    print(f"{p2_name}'s hits: {p2_hits}")
    print(f"Total game time: {int(total_time)} seconds")


'''
Main function. This is where the game is run. The game starts with a welcome message and a prompt to start the game. The players are asked to enter their names. Does a coin flip on who goes first.
Then, the players place their ships. The game then starts with the main game loop. The players take turns to hit the opponent's ships. The game ends when all ships are sunk.
Tracks the game statistics and prints the final scoreboard at the end of the game. The game also has an easter egg that can be found by the players.
'''
def main(): ### This is the ASCII art that is displayed at the start of the game.
    print("""
.-.   .-. .--. .-.    .--.  .--. .-..-. .--.   .-----. .--. 
: :.-.: :: .--': :   : .--': ,. :: `' :: .--'  `-. .-': ,. :
: :: :: :: `;  : :   : :   : :: :: .. :: `;      : :  : :: :
: `' `' ;: :__ : :__ : :__ : :; :: :; :: :__     : :  : :; :
 `.,`.,' `.__.':___.'`.__.'`.__.':_;:_;`.__.'    :_;  `.__.'
                                                            
                                                            
.---.  .--. .-----..-----..-.    .--.  .--. .-..-..-..---.  
: .; :: .; :`-. .-'`-. .-': :   : .--': .--': :; :: :: .; : 
:   .':    :  : :    : :  : :   : `;  `. `. :    :: ::  _.' 
: .; :: :: :  : :    : :  : :__ : :__  _`, :: :: :: :: :    
:___.':_;:_;  :_;    :_;  :___.'`.__.'`.__.':_;:_;:_;:_;    
""")
    print("Welcome to Battleship!")
    input("Press Enter to start the game.")
    
    ### Get player names
    player_1 = input("Enter a username (default player 1): ")
    if player_1 == "":
        player_1 = "player_1"
    player_2 = input("Enter a username (default player 2): ")
    if player_2 == "":
        player_2 = "player_2"
    
    ### Coin flip to determine who goes first
    chooser = random.choice([player_1, player_2])
    print(f"{chooser} goes first to choose heads or tails.")
    choice = input(f"{chooser}, do you want to be Heads or Tails: ").title()
    while choice not in ["Heads", "Tails"]: ### Error handling for invalid input
        choice = input("Invalid choice. Please enter Heads or Tails: ").title()
    
    coin_flip = random.choice(["Heads", "Tails"]) ### Random coin flip
    print(f"The coin landed on {coin_flip}")
    
    ### Determine first player based on coin flip
    current_player = player_1 if (chooser == player_1 and choice == coin_flip) or \
                               (chooser == player_2 and choice != coin_flip) else player_2
    other_player = player_2 if current_player == player_1 else player_1
    
    print(f"\n{current_player} will place their ships first.")
    
    ### Calls the place_ships function based on the winner of the coin flip.
    print(f"\n{current_player}, place your ships:")
    current_board = place_ships(current_player)
    input("\nPress Enter to clear screen for next player...")
    print("\n" * 50)  ### Clear the screen so next player will not be privy to ship placements.
    
    print(f"\n{other_player}, place your ships:") ### Other player places their ships.
    other_board = place_ships(other_player)
    
    ### Initialize tracking boards (where hits/misses are recorded). These are SEPERATE to the ship placement boards.
    current_tracking = [[" " for _ in range(10)] for _ in range(10)]
    other_tracking = [[" " for _ in range(10)] for _ in range(10)]
    
    ### Game statistics. These will be updated by the main function in the main game loop. Will be leveraged by the final stats function at the end of the game.
    current_hits = 0
    other_hits = 0
    game_start_time = turn_time()
    
    ### Function to check for easter egg. Only works if any player shoots in all 4 corners. These have to be the first 4 shots of the game.
    def check_easter_egg(tracking_board):
        corners = [(0,0), (0,9), (9,0), (9,9)]  # Top-left, top-right, bottom-left, bottom-right
        return all(tracking_board[row][col] in ['H', 'M'] for row, col in corners)
    
    ### Main game loop. Calls that take_turn function and turn_time (to time the game for final stats). Adds all hits and stats for final stats. Also checks for the easter egg.
    ### Calls Status_update to show the player's progress after each turn.
    while True:
        # Current player's turn
        turn_start = turn_time()
        hit, coords = take_turn(current_player, other_board, current_tracking)
        if hit:
            current_hits += 1
            # Update opponent's board to show hit
            row, col = coords
            other_board[row][col] = 'H'
        
        status_update(current_player, current_tracking)
        
        ### Check for easter egg after each turn
        if check_easter_egg(current_tracking):
            print("""
...................................................
...............................x.+.................
..............................x::x.................
.............................;X.x+.............;:..
.............................XXXXXXXXXXXX+xXX;.....
......................:+:.xXXXXXXXXXXXXXXXxXXXx+;..
...................+XXx.:XXXXXXXXXXXXXXXXXXxxxx+++.
................;XXXXX:.XXXXx;:...:;XXXXXX+........
..............+XXXXXXX.+XXX:.+XXXXX+:::xXX:........
..............xXXXXXXx.xXXx+XXXXx........++........
...........;XX...xXXXx.+XXXXXXX+..........:........
..........+XXX+..+XXXX.:XXXXXXX....................
.........+XXXXX+.+XXXX+.xXXXXXx....................
.........xXXXXXXXxXXXXx.+XXXXXx....................
........x..x;XXXXXXXXXX;.XXXXXX.............;......
.......;XXX..xXXXXXXXXXX.+XXXXX:.+..........x......
......:XXXX..xXXXXXXXXXX::XXXXXx.++.........X:.....
......XXXXXx.xXXXXXXXXXX;.XXXXXX::XX:......xX+.....
.....XXXXXXXXXXXX+XXXXXXx.xXXXXX;.XXXXXxxXXXXx.....
...;XXXXXXXXXXXXx.;XXXXXx.xXXXXXx..xXXXXXXXXX;.....
..xx+;:.XXXXXXXx..:XXXXX;.XXXXXXX...xXXXXXXXx......
.......:XXXXXX;.x;.XXXXx.;XXXXXXX;...:xXXXX:.......
.......+XXXXX.:XX;.;:...xXXXXXXXX;.................
......:XXXx..xXXXXXXXXXXXXXXXXXXX..................
......Xx;.:xXXXXXXXXXXXXXXXXXXXX:.X:...............
............:::;;++xXXXXXXXXXx;.;XX;...............
...................................................""")
            print("\nYou found an easter egg. GO COUGS! Created by Zachary Cornthwaite & Logan Harris")
            game_end_time = turn_time()
            final_scoreboard(current_player, player_1, player_2, 
                           current_hits if current_player == player_1 else other_hits,
                           other_hits if current_player == player_1 else current_hits,
                           game_end_time - game_start_time)
            break ### Breaks the loop (ends the game) if the easter egg is found. Whoever finds the easter egg wins.
        
        ### Check if game is over. If it is, breaks the main game loop (ends the game).
        if check_game_over(other_board):
            game_end_time = turn_time()
            final_scoreboard(current_player, player_1, player_2, 
                           current_hits if current_player == player_1 else other_hits,
                           other_hits if current_player == player_1 else current_hits,
                           game_end_time - game_start_time)
            break
        
        input("\nPress Enter to switch players...")
        print("\n" * 50)  # Clear screen
        
        ### Swap players after each turn.
        current_player, other_player = other_player, current_player
        current_board, other_board = other_board, current_board
        current_tracking, other_tracking = other_tracking, current_tracking
        current_hits, other_hits = other_hits, current_hits
    
if __name__ == "__main__":
    main()

input("Close the window (Input anything)") ### This is to keep the window open after the game ends. This is so the user can see the final stats and winner.