class SudokuCSP:
    def __init__(self, board):
        # 0 represents an empty cell
        self.board = board
        self.size = 9

    def is_valid(self, row, col, num):
        """ Checks if placing 'num' at board[row][col] is valid (CSP Consistency) """
       
        for x in range(9):
            if self.board[row][x] == num:
                return False

        for x in range(9):
            if self.board[x][col] == num:
                return False

        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True

    def find_empty(self):
        """ Finds an unassigned variable (cell) """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def solve(self):
        """ Backtracking Search """
        empty_cell = self.find_empty()
        if not empty_cell:
            return True  # Goal state reached
        
        row, col = empty_cell


        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num  # Assign variable

                if self.solve():  # Recursive step
                    return True

                self.board[row][col] = 0  # Backtrack

        return False

    def print_board(self):
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(self.size):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                print(self.board[i][j], end=" ")
            print()


initial_grid = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0], # A
    [9, 0, 0, 3, 0, 5, 0, 0, 1], # B
    [0, 0, 1, 8, 0, 6, 4, 0, 0], # C
    [0, 0, 8, 1, 0, 2, 9, 0, 0], # D
    [7, 0, 0, 0, 0, 0, 0, 0, 8], # E
    [0, 0, 6, 7, 0, 8, 2, 0, 0], # F
    [0, 0, 2, 6, 0, 9, 5, 0, 0], # G
    [8, 0, 0, 2, 0, 3, 0, 0, 9], # H
    [0, 0, 5, 0, 1, 0, 3, 0, 0]  # I
]

sudoku = SudokuCSP(initial_grid)

print("Original Puzzle")
sudoku.print_board()

if sudoku.solve():
    print("\nSolved Puzzle")
    sudoku.print_board()
else:
    print("\nNo solution exists.")