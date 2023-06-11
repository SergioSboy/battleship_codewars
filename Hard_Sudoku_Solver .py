# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# There are several difficulty of sudoku games, we can estimate the difficulty of a sudoku game based on how many cells are given of the 81 cells of the game.
#
# Easy sudoku generally have over 32 givens
# Medium sudoku have around 30–32 givens
# Hard sudoku have around 28–30 givens
# Very Hard sudoku have less than 28 givens
# Note: The minimum of givens required to create a unique (with no multiple solutions) sudoku game is 17.
#
# A hard sudoku game means that at start no cell will have a single candidates and thus require guessing and trial and error.
# A very hard will have several layers of multiple candidates for any empty cell.
#
# Task:
# Write a function that solves sudoku puzzles of any difficulty. The function will take a sudoku grid and it should return a 9x9 array with the proper answer for the puzzle.
#
# Or it should raise an error in cases of: invalid grid (not 9x9, cell with values not in the range 1~9); multiple solutions for the same puzzle or the puzzle is unsolvable
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def findEm(board):
#     for i in range(0,9):
#         for j in range(0,9):
#             if  board[i][j] == 0:
#                 return [i,j]
#     return None
#
# def valid(num,pos,board, size, box_size):
#     r, c = pos[0], pos[1]
#     # check rows
#     for i in range(0,9):
#         if board[i][c] == num and i != r:
#             return False
#     # check columns
#     for i in range(0,9):
#         if board[r][i] == num and i != c:
#             return False
#     # check box
#     boxRow = (r//3)*3
#     boxCol = (c//3)*3
#     for i in range(boxRow,boxRow+3):
#         for j in range(boxCol, boxCol+3):
#             if board[i][j] == num and i != r and j != c:
#                 return False
#     return True
#
# def solve(board,size, box_size):
#     currPos = findEm(board)
#     if currPos == None:
#         return True
#     for i in range(1,size+1):
#         currNum = i
#         isValid = valid(currNum, currPos, board, size, box_size)
#         if isValid:
#             x,y = currPos[0],currPos[1]
#             board[x][y] = currNum
#             if solve(board, size, box_size):
#                 return True
#             board[x][y] = 0
#
# def sudoku_solver(puzzle):
#     # Happy Coding!
#     board = puzzle
#     size = 9
#     box_size = 3
#     solve(board,size, box_size)
#     return board
# from itertools import product
# def solve_sudoku(puzzle):
#     for (row, col) in product(range(0,9), repeat = 2):
#         if puzzle[row][col] == 0:
#             for num in range(1,10):
#                 allowed = True
#                 for i in range(0,9):
#                     if puzzle[i][col]  == num or puzzle[row][i] == num:
#                         allowed = False; break
#                 for (i,j) in product(range(0,3),repeat = 2):
#                     if puzzle[row-row%3+i][col - col%3+j] == num:
#                         allowed = False; break
#                 if allowed:
#                     puzzle[row][col] =num
#                     if trial := solve_sudoku(puzzle):
#                         return trial
#                     else:
#                         puzzle[row][col] = 0
#             return False
#         return puzzle
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import copy
import math


def sudoku_solver(puzzle):
    sudoku = Sudoku()
    sudoku.setboard(puzzle)
    if not sudoku.valid:
        raise ValueError
    sudoku.solve()
    if len(sudoku.result_boards) != 1:
        raise ValueError
    return sudoku.result_boards[0]


class Sudoku:
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    units = []
    peers = []
    for i in range(81):
        units.append([])
        units[i].append([])
        r = int(i / 9)
        for c in range(9):
            units[i][0].append(r * 9 + c)
        units[i].append([])
        c = int(i % 9)
        for r in range(9):
            units[i][1].append(r * 9 + c)
        units[i].append([])
        br = int(int(i / 9) / 3)
        cr = int(int(i % 9) / 3)
        for r in range(br * 3, br * 3 + 3):
            for c in range(cr * 3, cr * 3 + 3):
                units[i][2].append(r * 9 + c)
        peers.append([])
        for unit in units[i]:
            for cell in unit:
                if cell not in peers[i]:
                    peers[i].append(cell)
        peers[i].remove(i)

    def __init__(self):
        self.mask = []
        self.valid = True
        self.solutions = []
        self.result_boards = []

    def setboard(self, board):
        self.mask = []
        self.valid = True
        self.solutions = []
        self.result_boards = []

        if not self.validate(board):
            self.valid = False

        self.mask = [0x1ff] * 81

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]:
                    if not self.set(r * 9 + c, board[r][c]):
                        self.valid = False
                        return

    def validate(self, board):
        if len(board) != 9:
            return False
        for r in range(len(board)):
            if len(board[r]) != 9:
                return False
        return True

    def mask_to_board(self, mask):
        board = []
        for r in range(9):
            board.append([0] * 9)
        for r in range(9):
            for c in range(9):
                if self.is_single_bit(mask[r * 9 + c]):
                    for d in self.digits:
                        if mask[r * 9 + c] & (1 << (d - 1)):
                            board[r][c] = d
        return board

    def clone(self):
        sudoku = Sudoku()
        sudoku.mask = copy.copy(self.mask)
        sudoku.valid = self.valid
        return sudoku

    def solve(self):
        self.solve_helper()

        for result in self.solutions:
            self.result_boards.append(self.mask_to_board(result))

    def solve_helper(self):
        cell = self.find_vacant_with_min_possibilities()
        if cell is None:
            self.add_solution(self.mask)
            return
        for d in self.digits:
            # skip if d is not allowed in this cell
            if not (self.mask[cell] & (1 << (d - 1))):
                continue
            sudoku = self.clone()
            if not sudoku.set(cell, d):
                continue
            sudoku.solve_helper()
            if len(sudoku.solutions) > 0:
                for solution in sudoku.solutions:
                    self.add_solution(solution)
            if len(self.solutions) >= 2:
                return
    def is_single_bit(self, m):
        return (m & (m - 1)) == 0

    def count_bits(self, m):
        count = 0
        while m:
            m &= (m - 1)
            count += 1
        return count
    def add_solution(self, mask):
        for result in self.solutions:
            if result == mask:
                return
        self.solutions.append(copy.deepcopy(mask))
    def find_vacant_with_min_possibilities(self):
        vacant_cnt = 0
        best_vacant_possibilities = 10
        best_vacant_i = 0
        for i in range(81):
            if best_vacant_possibilities == 2:
                break;
            if not self.is_single_bit(self.mask[i]):
                vacant_cnt += 1
                choices = self.count_bits(self.mask[i])

                if choices < best_vacant_possibilities:
                    best_vacant_possibilities = choices
                    best_vacant_i = i

        if (vacant_cnt == 0):
            return None

        return best_vacant_i
    def set(self, cell, d):
        other_values = [d2 for d2 in self.digits if d2 != d and self.mask[cell] & (1 << (d2 - 1))]
        for d2 in other_values:
            if not self.clear(cell, d2):
                return False
        return True
    def clear(self, cell, d):
        # if already cleared
        if not (self.mask[cell] & (1 << (d - 1))):
            return True
        self.mask[cell] &= ~(1 << (d - 1))
        if self.mask[cell] == 0:
            return False  # error: no value is allowed at this cell (Rule 3)
        elif self.is_single_bit(self.mask[cell]):
            val = int(math.log2(self.mask[cell])) + 1
            for cell2 in self.peers[cell]:
                if not self.clear(cell2, val):
                    return False
        for u in self.units[cell]:
            dplaces = [cell2 for cell2 in u if self.mask[cell2] & (1 << (d - 1))]
            if len(dplaces) == 0:
                return False  # error: no place for this value (Rule 4)
            elif len(dplaces) == 1:
                if not self.set(dplaces[0], d):
                    return False
        return True
# ------------------------------------------TEST------------------------------------------------------------------------------------------------------------------------------
puzzle = [
            [0, 0, 6, 1, 0, 0, 0, 0, 8],
            [0, 8, 0, 0, 9, 0, 0, 3, 0],
            [2, 0, 0, 0, 0, 5, 4, 0, 0],
            [4, 0, 0, 0, 0, 1, 8, 0, 0],
            [0, 3, 0, 0, 7, 0, 0, 4, 0],
            [0, 0, 7, 9, 0, 0, 0, 0, 3],
            [0, 0, 8, 4, 0, 0, 0, 0, 6],
            [0, 2, 0, 0, 5, 0, 0, 8, 0],
            [1, 0, 0, 0, 0, 2, 5, 0, 0]
        ]
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a = sudoku_solver(puzzle)
for i in range(9):
    print(a[i])