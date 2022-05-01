from gameclass import Game

ticTacToe = Game()

# opening instructions
print("Welcome to Tic Tac Toe!")
print("You will play using a grid.")
print("You will enter a row number then a column number to place your move")
print("Grid positon numbers are as follow with (ROW-COLUMN) format:")
print('|(1-1)|(1-2)|(1-3)|')
print('|(2-1)|(2-2)|(2-3)|')
print('|(3-1)|(3-2)|(3-3)|\n')
ready = input("Press Y to play or N to quit: ")

while ready == "Y":

    # Print which players turn it is and draw the grid
    print("It is " + ticTacToe.turn + " turn: \n")
    ticTacToe.DrawGrid()

    # Get users move selection by row and column
    # I didnt validate user input so anything other than 1-3 entered will cause error 
    row = int(input("Row: "))
    col = int(input("column: "))
    print()

    # This can probably be better but basically if the desired coordinates are available
    # place the move. Otherwise tell user spot is taken and restart loop.
    # It doesnt switch turns until it gets past this part.
    if ticTacToe.Play(row, col) == True:
        ticTacToe.Play(row, col)
    else:
       print("Position is taken, Try again")
       continue

    # After the move is made, check if it caused a win.
    # If it did, print who won and ask if they wanna play again. reset board if yes
    # If user doesnt want to play again exit the while loop.
    # Again I havent validated input, anything other than 'Y' exits game
    if ticTacToe.CheckWinner(ticTacToe.turn) == ticTacToe.turn:
        ticTacToe.DrawGrid()
        print(ticTacToe.turn +  " has won!")
        ready = input("Would you like to play another game? Press Y/N: ")
        if ready.upper() == "Y":
            ticTacToe.NewGame()
            continue
        else:
            break

    # Check if game still has moves left. Switch turns before restarting loop
    elif ticTacToe.CheckWinner(ticTacToe.turn) == "N":
        ticTacToe.swapTurn(ticTacToe.turn)
        continue
    
    # If no more moves are left declare a tie and again prompt to play again
    elif ticTacToe.CheckWinner(ticTacToe.turn) == "T":
        ticTacToe.DrawGrid()
        print("Tie Game!")
        ready = input("Would you like to play another game? Press Y/N: ")
        if ready == "Y":
            ticTacToe.NewGame()
            continue
        else:
            break

print("Thanks for playing!")
input("Press any key to exit")