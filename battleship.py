# Write a method that takes a field for well-known board game "Battleship" as an argument and returns
# true if it has a valid disposition of ships, false otherwise.
# Argument is guaranteed to be 10*10 two-dimension array.
# Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
# Battleship (also Battleships or Sea Battle) is a guessing game for two players.
# Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's
# forces by targetting individual cells on his field.
# The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version.
# In this kata we will use Soviet/Russian version of the game.
# Before the game begins, players set up the board and place the ships accordingly to the following rules:
#           - There must be single battleship (size of 4 cells), 2 cruisers (size 3),
#             3 destroyers (size 2) and 4 submarines (size 1).
#             Any additional ships are not allowed, as well as missing ships.
#           - Each ship must be a straight line, except for submarines, which are just single cell.
#           - The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner
def p(i, j, field):
    if j == 0 and i == 0:
        if field[i + 1][j + 1] == 1:
            return False
        else:
            return True
    elif i == 0 and 0 < j < 9:
        if field[i + 1][j + 1] == 1:
            return False
        elif field[i + 1][j - 1] == 1:
            return False
        else:
            return True
    elif i == 0 and j == 9:
        if field[i + 1][j - 1] == 1:
            return False
        else:
            return True
    elif 0 < i < 9 and j == 0:
        if field[i - 1][j + 1] == 1:
            return False
        elif field[i + 1][j + 1] == 1:
            return False
        else:
            return True
    elif 0 < i < 9 and 0 < j < 9:
        if field[i + 1][j + 1] == 1:
            return False
        elif field[i - 1][j + 1] == 1:
            return False
        elif field[i - 1][j - 1] == 1:
            return False
        elif field[i + 1][j - 1] == 1:
            return False
        else:
            return True
    elif i == 9 and j == 0:
        if field[i - 1][j + 1] == 1:
            return False
        else:
            return True
    elif i == 9 and j == 9:
        if field[i - 1][j - 1] == 1:
            return False
        else:
            return True
    elif 0 < i < 9 and j == 9:
        if field[i - 1][j - 1] == 1:
            return False
        elif field[i + 1][j - 1] == 1:
            return False
        else:
            return True
    elif i == 9 and 0 < j < 9:
        if field[i - 1][j - 1] == 1:
            return False
        elif field[i - 1][j + 1] == 1:
            return False
        else:
            return True


def validate_battlefield(field):
    kol = 0
    kol_k = [0, 0, 0, 0]
    # 1 - link, 2 -cruiser, 3 - destroyers, 4 - submarine
    for i in range(10):
        kol_1 = 0
        kol_2 = 0
        for j in range(10):
            if field[i][j] == 1:
                kol_1 += 1
                kol += 1
            else:
                if kol_1 > 4:
                    return False
                if kol_1 > 0 and kol_1 < 5:
                    kol_k[kol_1 - 1] += 1
                kol_1 = 0
                flag1 = False

        for j in range(10):
            if field[j][i] == 1:
                kol_2 += 1
            else:
                if kol_2 > 4:
                    return False
                if kol_2 > 0 and kol_2 < 5:
                    kol_k[kol_2 - 1] += 1
                kol_2 = 0
                flag2 = False

    if kol_k[1] > 3 or kol_k[2] > 2 or kol_k[3] > 1:
        return False
    if kol > 20 or kol < 20:
        return False
    kol_T = 0
    for i in range(10):
        for j in range(10):
            flag = False
            if field[i][j] == 1:
                if(p(i, j, field)):
                    kol_T += 1
            else:
                flag = False
    if kol_T == 20:
        return True
    else:
        return False

field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(validate_battlefield(field))
