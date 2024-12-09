'''
Takes a players username parameter for who gets to place their ships first (decided by main()). 
Prompts for where they want to place their ships (Carrier, Battleship, Cruiser, Submarine, Destroyer).
Checks if the placement is valid (not out of bounds, not overlapping with other ships, not diagonal).
If the placement is valid, the ship is placed on the board. Stores the information in the player's board (dictionary) for later query by main().
'''

### Import Matplotlib (for board visualization)
import matplotlib.pyplot as plt

### Function to visualize the board
def visualize_board(board):
    plt.figure(figsize=(10, 10))
    
    ### Plot grid lines
    for i in range(1, 12):
        plt.axhline(y=i, color='gray', linestyle='-', alpha=0.3)
        plt.axvline(x=i, color='gray', linestyle='-', alpha=0.3)
    
    ### Set colors and labels for ships
    colors = {'C': 'gray', 'B': 'blue', 'R': 'green', 'S': 'red', 'D': 'purple', ' ': 'white'}
    labels = {'C': 'Carrier', 'B': 'Battleship', 'R': 'Cruiser', 'S': 'Submarine', 'D': 'Destroyer'}
    
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

### Function to place ships on the board
def place_ships(player):
    print(player + ", place your ships.")
    ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    ship_lengths = [5, 4, 3, 3, 2]
    ship_codes = {'Carrier': 'C', 'Battleship': 'B', 'Cruiser': 'R', 'Submarine': 'S', 'Destroyer': 'D'}
    
    ### Initialize the board (10x10 grid, in a list of lists)
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
                    if any(temp_board[array_row][array_col + j] != " " for j in range(ship_lengths[i])):
                        print("Ship overlaps with another ship. Try again.")
                        continue
                    for j in range(ship_lengths[i]):
                        temp_board[array_row][array_col + j] = ship_codes[ships[i]]
                
                ### Check if ship is already placed in the selected location
                elif orientation == "V":
                    if array_row + ship_lengths[i] > 10:  ### Check if ship is out of bounds
                        print("Ship is out of bounds. Try again.")
                        continue
                    if any(temp_board[array_row + j][array_col] != " " for j in range(ship_lengths[i])):
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

### Test the function (this will stay a comment unless being used by the developer)
player = "Rinzler"
place_ships(player)