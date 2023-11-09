"""WarBoat!!!"""
import random

##program to show the game board
def game_board(board):
    print(f'{board[0][0]:<2} {board[0][1]:<2} {board[0][2]:<2} '
          f'{board[0][3]:<2} {board[0][4]:<2} {board[0][5]:<2} '
          f'{board[0][6]:<2} {board[0][7]:<2} {board[0][8]:<2} '
          f'{board[0][9]:<2} {board[0][10]:<2}')
    print(f'{board[1][0]:<2} {board[1][1]:<2} {board[1][2]:<2} '
          f'{board[1][3]:<2} {board[1][4]:<2} {board[1][5]:<2} '
          f'{board[1][6]:<2} {board[1][7]:<2} {board[1][8]:<2} '
          f'{board[1][9]:<2} {board[1][10]:<2}')
    print(f'{board[2][0]:<2} {board[2][1]:<2} {board[2][2]:<2} '
          f'{board[2][3]:<2} {board[2][4]:<2} {board[2][5]:<2} '
          f'{board[2][6]:<2} {board[2][7]:<2} {board[2][8]:<2} '
          f'{board[2][9]:<2} {board[2][10]:<2}')
    print(f'{board[3][0]:<2} {board[3][1]:<2} {board[3][2]:<2} '
          f'{board[3][3]:<2} {board[3][4]:<2} {board[3][5]:<2} '
          f'{board[3][6]:<2} {board[3][7]:<2} {board[3][8]:<2} '
          f'{board[3][9]:<2} {board[3][10]:<2}')
    print(f'{board[4][0]:<2} {board[4][1]:<2} {board[4][2]:<2} '
          f'{board[4][3]:<2} {board[4][4]:<2} {board[4][5]:<2} '
          f'{board[4][6]:<2} {board[4][7]:<2} {board[4][8]:<2} '
          f'{board[4][9]:<2} {board[4][10]:<2}')
    print(f'{board[5][0]:<2} {board[5][1]:<2} {board[5][2]:<2} '
          f'{board[5][3]:<2} {board[5][4]:<2} {board[5][5]:<2} '
          f'{board[5][6]:<2} {board[5][7]:<2} {board[5][8]:<2} '
          f'{board[5][9]:<2} {board[5][10]:<2}')
    print(f'{board[6][0]:<2} {board[6][1]:<2} {board[6][2]:<2} '
          f'{board[6][3]:<2} {board[6][4]:<2} {board[6][5]:<2} '
          f'{board[6][6]:<2} {board[6][7]:<2} {board[6][8]:<2} '
          f'{board[6][9]:<2} {board[6][10]:<2}')
    print(f'{board[7][0]:<2} {board[7][1]:<2} {board[7][2]:<2} '
          f'{board[7][3]:<2} {board[7][4]:<2} {board[7][5]:<2} '
          f'{board[7][6]:<2} {board[7][7]:<2} {board[7][8]:<2} '
          f'{board[7][9]:<2} {board[7][10]:<2}')
    print(f'{board[8][0]:<2} {board[8][1]:<2} {board[8][2]:<2} '
          f'{board[8][3]:<2} {board[8][4]:<2} {board[8][5]:<2} '
          f'{board[8][6]:<2} {board[8][7]:<2} {board[8][8]:<2} '
          f'{board[8][9]:<2} {board[8][10]:<2}')
    print(f'{board[9][0]:<2} {board[9][1]:<2} {board[9][2]:<2} '
          f'{board[9][3]:<2} {board[9][4]:<2} {board[9][5]:<2} '
          f'{board[9][6]:<2} {board[9][7]:<2} {board[9][8]:<2} '
          f'{board[9][9]:<2} {board[9][10]:<2}')
    print(f'{board[10][0]:<2} {board[10][1]:<2} {board[10][2]:<2} '
          f'{board[10][3]:<2} {board[10][4]:<2} {board[10][5]:<2} '
          f'{board[10][6]:<2} {board[10][7]:<2} {board[10][8]:<2} '
          f'{board[10][9]:<2} {board[10][10]:<2}')

##function to allow player to place ships
def ship_place():
    ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    while ships:
        game_board(p_board)
        print(f'You have {len(ships)} ships remaining: {ships}')
        ship = input("Which ship would you like to place? ")
    ##Carrier ship
        if ship.capitalize() in ships:
            if ship.lower() == "carrier":
                placement = input("This ship is 5 spaces long. Would you like "
                                  "to place it horizontally(H) or "
                                  "vertically(V)? ")
                if placement.lower() == "h":
                    while True:
                        chosen_row = input("Which row would you like to place "
                                           "this ship in? ")
                        if chosen_row.capitalize() in rows and not(chosen_row == "0"):
                            row = rows.index(chosen_row.upper())
                            col = input("Which column would you like to place "
                                        "the leftmost end of this ship in? ")
                            if col in columns:
                                col = int(col)
                                if col < 7 and not(col == 0):
                                    unavailable = []
                                    for e in range(0,5):
                                        if p_board[row][col+e]:
                                           unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit inside "
                                          "the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Please try again.")
                    for e in range(5):
                        p_board[row][col] = "X"
                        col += 1
                    ships.pop(ships.index("Carrier"))
                elif placement.lower() == "v":
                    while True:
                        col = input("Which column would you like to place this"
                                    " ship in? ")
                        if col in columns:
                            col = int(col)
                            row_start = (input("Which row would you "
                                               "like to place the uppermost "
                                               "end of this ship in? "))
                            if row_start.capitalize() in rows and not(row_start == "0"):
                                row = rows.index(row_start.upper())
                                if row < 7:
                                    unavailable = []
                                    for e in range(0,5):
                                        if p_board[row + e][col]:
                                            unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit "
                                          "inside the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Try again.")
                    for e in range(5):
                        p_board[row][col] = "X"
                        row += 1
                    ships.pop(ships.index("Carrier"))
                else:
                    print("That wasn't an option. Please try again")
        
    ##Battleship
            elif ship.lower() == "battleship":
                placement = input("This ship is 4 spaces long. Would you like "
                                  "to place it horizontally(H) or "
                                  "vertically(V)? ")
                if placement.lower() == "h":
                    while True:
                        chosen_row = input("Which row would you like to place "
                                           "this ship in? ")
                        if chosen_row.capitalize() in rows and not(chosen_row == "0"):
                            row = rows.index(chosen_row.upper())
                            col = input("Which column would you like to "
                                        "place the leftmost end of "
                                        "this ship in? ")
                            if col in columns:
                                col = int(col)
                                if col < 8 and not(col == 0):
                                    unavailable = []
                                    for e in range(0,4):
                                        if p_board[row][col+e]:
                                           unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit "
                                          "inside the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Try again.")
                    for e in range(4):
                        p_board[row][col] = "X"
                        col += 1
                    ships.pop(ships.index("Battleship"))
                elif placement.lower() == "v":
                    while True:
                        col = input("Which column would you like to "
                                    "place this ship in? ")
                        if col in columns:
                            col = int(col)
                            row_start = (input("Which row would you "
                                               "like to place the uppermost "
                                               "end of this ship in? "))
                            if row_start.capitalize() in rows and not(row_start == "0"):
                                row = rows.index(row_start.upper())
                                if row < 8:
                                    unavailable = []
                                    for e in range(0,4):
                                        if p_board[row + e][col]:
                                            unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit "
                                          "inside the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Try again.")
                    for e in range(4):
                        p_board[row][col] = "X"
                        row += 1
                    ships.pop(ships.index("Battleship"))
                else:
                    print("That wasn't an option. Please try again")
    ##Cruiser
            elif ship.lower() == "cruiser":
                placement = input("This ship is 3 spaces long. Would you "
                                  "like to place it horizontally(H) or "
                                  "vertically(V)? ")
                if placement.lower() == "h":
                    while True:
                        chosen_row = input("Which row would you like to place "
                                           "this ship in? ")
                        if chosen_row.capitalize() in rows and not(chosen_row == "0"):
                            row = rows.index(chosen_row.upper())
                            col = input("Which column would you like to place "
                                        "the leftmost end of this ship in? ")
                            if col in columns:
                                col = int(col)
                                if col < 9 and not(col == 0):
                                    unavailable = []
                                    for e in range(0,3):
                                        if p_board[row][col+e]:
                                           unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit inside "
                                          "the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Try again.")
                    for e in range(3):
                        p_board[row][col] = "X"
                        col += 1
                    ships.pop(ships.index("Cruiser"))
                elif placement.lower() == "v":
                    while True:
                        col = input("Which column would you like to place "
                                    "this ship in? ")
                        if col in columns:
                            col = int(col)
                            row_start = (input("Which row would you like to "
                                               "place the uppermost end of "
                                               "this ship in? "))
                            if row_start.capitalize() in rows and not(row_start == "0"):
                                row = rows.index(row_start.upper())
                                if row < 9:
                                    unavailable = []
                                    for e in range(0,3):
                                        if p_board[row + e][col]:
                                            unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit inside "
                                          "the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Try again.")
                    for e in range(3):
                        p_board[row][col] = "X"
                        row += 1
                    ships.pop(ships.index("Cruiser"))
                else:
                    print("That wasn't an option. Please try again")
    ##Submarine
            elif ship.lower() == "submarine":
                placement = input("This ship is 3 spaces long. Would you like "
                                  "to place it horizontally(H) "
                                  "or vertically(V)? ")
                if placement.lower() == "h":
                    while True:
                        chosen_row = input("Which row would you like to place "
                                           "this ship in? ")
                        if chosen_row.capitalize() in rows and not(chosen_row == "0"):
                            row = rows.index(chosen_row.upper())
                            col = input("Which column would you like to place "
                                        "the leftmost end of this ship in? ")
                            if col in columns:
                                col = int(col)
                                if col < 9 and not(col == 0):
                                    unavailable = []
                                    for e in range(0,3):
                                        if p_board[row][col+e]:
                                           unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit inside "
                                          "the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Try again.")
                    for e in range(3):
                        p_board[row][col] = "X"
                        col += 1
                    ships.pop(ships.index("Submarine"))
                elif placement.lower() == "v":
                    while True:
                        col = input("Which column would you like to place this"
                                    " ship in? ")
                        if col in columns:
                            col = int(col)
                            row_start = (input("Which row would you like to "
                                               "place the uppermost end of "
                                               "this ship in? "))
                            if row_start.capitalize() in rows and not(row_start == "0"):
                                row = rows.index(row_start.upper())
                                if row < 9:
                                    unavailable = []
                                    for e in range(0,3):
                                        if p_board[row + e][col]:
                                            unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit inside "
                                          "the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Try again.")
                    for e in range(3):
                        p_board[row][col] = "X"
                        row += 1
                    ships.pop(ships.index("Submarine"))
                else:
                    print("That wasn't an option. Please try again")
    ##Destroyer
            elif ship.lower() == "destroyer":
                placement = input("This ship is 2 spaces long. Would you "
                                  "like to place it horizontally(H) "
                                  "or vertically(V)? ")
                if placement.lower() == "h":
                    while True:
                        chosen_row = input("Which row would you like to "
                                           "place this ship in? ")
                        if chosen_row.capitalize() in rows and not(chosen_row == "0"):
                            row = rows.index(chosen_row.upper())
                            col = input("Which column would you like to "
                                        "place the leftmost end of "
                                        "this ship in? ")
                            if col in columns:
                                col = int(col)
                                if col < 10 and not(col == 0):
                                    unavailable = []
                                    for e in range(0,2):
                                        if p_board[row][col+e]:
                                           unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit "
                                          "inside the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Try again.")
                    for e in range(2):
                        p_board[row][col] = "X"
                        col += 1
                    ships.pop(ships.index("Destroyer"))
                elif placement.lower() == "v":
                    while True:
                        col = input("Which column would you like to place "
                                    "this ship in? ")
                        if col in columns:
                            col = int(col)
                            row_start = (input("Which row would you like "
                                               "to place the uppermost end "
                                               "of this ship in? "))
                            if row_start.capitalize() in rows and not(row_start == "0"):
                                row = rows.index(row_start.upper())
                                if row < 10:
                                    unavailable = []
                                    for e in range(0,2):
                                        if p_board[row + e][col]:
                                            unavailable.append(e)
                                    if unavailable:
                                        print("There is already a ship there.")
                                    else:
                                        break
                                else:
                                    print("That placement doesn't fit inside "
                                          "the board.")
                            else:
                                print("That isn't an option. Try again.")
                        else:
                            print("That isn't an option. Try again.")
                    for e in range(2):
                        p_board[row][col] = "X"
                        row += 1
                    ships.pop(ships.index("Destroyer"))
                else:
                    print("That wasn't an option. Please try again")
        else:
            print("That's not available. Please try again.")

##function to set up computer's board
def comp_board_place():
    ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    while ships:
        ship = random.choice(ships)
        if ship == "Carrier":
            placement = random.choice(["h", "v"])
            if placement == "h":
                while True:
                    chosen_row = random.choice(rows)
                    if not(chosen_row == 0):
                        row = rows.index(chosen_row)
                        col = random.choice([1, 2, 3, 4, 5, 6])
                        unavailable = []
                        for e in range(0,5):
                            if c_board[row][col+e]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(5):
                    c_board[row][col] = "X"
                    col += 1
                ships.pop(ships.index("Carrier"))
            elif placement == "v":
                while True:
                    col = int(random.choice(columns))
                    if not(col == 0):
                        row = random.choice([1, 2, 3, 4, 5, 6])
                        unavailable = []
                        for e in range(0,5):
                            if c_board[row + e][col]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(5):
                    c_board[row][col] = "X"
                    row += 1
                ships.pop(ships.index("Carrier"))
        elif ship == "Battleship":
            placement = random.choice(["h", "v"])
            if placement == "h":
                while True:
                    chosen_row = random.choice(rows)
                    if not(chosen_row == 0):
                        row = rows.index(chosen_row)
                        col = random.choice([1, 2, 3, 4, 5, 6, 7])
                        unavailable = []
                        for e in range(0,4):
                            if c_board[row][col+e]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(4):
                    c_board[row][col] = "X"
                    col += 1
                ships.pop(ships.index("Battleship"))
            elif placement == "v":
                while True:
                    col = int(random.choice(columns))
                    if not(col == 0):
                        row = random.choice([1, 2, 3, 4, 5, 6, 7])
                        unavailable = []
                        for e in range(0,4):
                            if c_board[row + e][col]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(4):
                    c_board[row][col] = "X"
                    row += 1
                ships.pop(ships.index("Battleship"))
        elif ship == "Cruiser":
            placement = random.choice(["h", "v"])
            if placement == "h":
                while True:
                    chosen_row = random.choice(rows)
                    if not(chosen_row == 0):
                        row = rows.index(chosen_row)
                        col = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
                        unavailable = []
                        for e in range(0,3):
                            if c_board[row][col+e]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(3):
                    c_board[row][col] = "X"
                    col += 1
                ships.pop(ships.index("Cruiser"))
            elif placement == "v":
                while True:
                    col = int(random.choice(columns))
                    if not(col == 0):
                        row = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
                        unavailable = []
                        for e in range(0,3):
                            if c_board[row + e][col]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(3):
                    c_board[row][col] = "X"
                    row += 1
                ships.pop(ships.index("Cruiser"))
        elif ship == "Submarine":
            placement = random.choice(["h", "v"])
            if placement == "h":
                while True:
                    chosen_row = random.choice(rows)
                    if not(chosen_row == 0):
                        row = rows.index(chosen_row)
                        col = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
                        unavailable = []
                        for e in range(0,3):
                            if c_board[row][col+e]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(3):
                    c_board[row][col] = "X"
                    col += 1
                ships.pop(ships.index("Submarine"))
            elif placement == "v":
                while True:
                    col = int(random.choice(columns))
                    if not(col == 0):
                        row = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
                        unavailable = []
                        for e in range(0,3):
                            if c_board[row + e][col]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(3):
                    c_board[row][col] = "X"
                    row += 1
                ships.pop(ships.index("Submarine"))
        elif ship == "Destroyer":
            placement = random.choice(["h", "v"])
            if placement == "h":
                while True:
                    chosen_row = random.choice(rows)
                    if not(chosen_row == 0):
                        row = rows.index(chosen_row)
                        col = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                        unavailable = []
                        for e in range(0,2):
                            if c_board[row][col+e]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(2):
                    c_board[row][col] = "X"
                    col += 1
                ships.pop(ships.index("Destroyer"))
            elif placement == "v":
                while True:
                    col = int(random.choice(columns))
                    if not(col == 0):
                        row = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                        unavailable = []
                        for e in range(0,2):
                            if c_board[row + e][col]:
                                unavailable.append(e)
                        if not unavailable:
                            break
                for e in range(2):
                    c_board[row][col] = "X"
                    row += 1
                ships.pop(ships.index("Destroyer"))


if __name__ == '__main__':
    p_board = [[0,1,2,3,4,5,6,7,8,9,10],['A',"","","","","","","","","",""],
               ['B',"","","","","","","","","",""],
               ['C',"","","","","","","","","",""],
               ['D',"","","","","","","","","",""],
               ['E',"","","","","","","","","",""],
               ['F',"","","","","","","","","",""],
               ['G',"","","","","","","","","",""],
               ['H',"","","","","","","","","",""],
               ['I',"","","","","","","","","",""],
               ['J',"","","","","","","","","",""]]
        ##has players ships on it

    c_board = [[0,1,2,3,4,5,6,7,8,9,10],['A',"","","","","","","","","",""],
               ['B',"","","","","","","","","",""],
               ['C',"","","","","","","","","",""],
               ['D',"","","","","","","","","",""],
               ['E',"","","","","","","","","",""],
               ['F',"","","","","","","","","",""],
               ['G',"","","","","","","","","",""],
               ['H',"","","","","","","","","",""],
               ['I',"","","","","","","","","",""],
               ['J',"","","","","","","","","",""]]
        ##has computer's ships on it
    
    rows = [0, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    columns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    
        ##these three are for the ship_place function - didn't want to put them
        ##inside the function incase we wanted them later
    
    comp_board_place()
    ship_place()
    
    ##Gameplay
