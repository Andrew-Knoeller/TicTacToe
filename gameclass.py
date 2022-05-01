class Game:

# Initialize the game board. 'X' will be first player.
# Decided to place '-' in board grids for user to be able to see whats going on easier.
    def __init__(self):
        self.grid = grid = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.turn = "X"

# Draw current grid.
    def DrawGrid(self):
        for row in self.grid:
            for col in row:
                print(col, end=" ")
            print()

# If an 'X" or "O" already exists return False.
# Else place the users move and switch players.
    def Play(self, row, col):
        if self.grid[row - 1][col - 1] == "X" or self.grid[row - 1][col - 1] == "O":
            return False
        else:
            self.grid[row - 1][col - 1] = self.turn
            return True

    def swapTurn(self, turn):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

# Check for winners, a tie, or if the game can continue.
    def CheckWinner(self, turn):

# Check the rows to see if player has won horizontally.
        for row in range(len(self.grid)):
            horizWin = True
            for col in range(len(self.grid)):
                if self.grid[row][col] != self.turn:
                    horizWin = False
                    break
            if horizWin:
                return self.turn
            
                

# Check the columns to see if player won vertically.
        for row in range(len(self.grid)):
            vertWin = True
            for col in range(len(self.grid)):
                if self.grid[col][row] != self.turn:
                    vertWin = False
                    break
            if vertWin:
                return self.turn

# Check grid for any diagonal wins.
# leftDiagWin means diagonal win starting in top left
        leftDiagWin = True
        for row in range(len(self.grid)):
            if self.grid[row][row] != self.turn:
                leftDiagWin = False
                break
        if leftDiagWin:
            return self.turn

# rightDiagWin meand diagonal win starting in top right
        rightDiagWin = True
        for row in range(len(self.grid)):
            if self.grid[row][len(self.grid) - 1 - row] != self.turn:
                rightDiagWin = False
                break
        if rightDiagWin:
            return self.turn

# Check if there are any open positions still left(N) and if not game is a tie(T).
        for row in self.grid:
            for col in row:
                if col == "-":
                    return "N"
        return "T"

 # Reset the game board.  
    def NewGame(self):
        self.grid = grid = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.turn = "X"
