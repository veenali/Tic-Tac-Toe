import random


def display_board(board):
    print(f''' 
    {board[7]}|{board[8]}|{board[9]}                               7 | 8 | 9
    ---+---+---                              ---+---+---
    {board[4]}|{board[5]}|{board[6]}              POSITIONS        4 | 5 | 6  
    ---+---+---                              ---+---+---         
    {board[1]}|{board[2]}|{board[3]}                               1 | 2 | 3 
    ''')


def valid_input():
    while True:
        pos = input("Enter position : ")
        if pos != " ":
            if pos.isalnum() != True:
                if int(pos) in range(1, 10):
                    pos = int(pos)
                    break
                print("Not a valid position")
        else:
            print("Thank you for playing the game :)")
            exit()
        return int(pos)


def valid_pos(board, turn):
    print(turn, "chance")
    while True:
        pos = valid_input()
        if board[pos] == "   ":
            board[pos] = turn
            break
        else:
            print(
                "Marker is already present in the given location. Please select a new location")
    display_board(board)


def check(board):
    check = 0
    # Row checking is done here
    if board[1] == board[2] == board[3] != "   " or board[4] == board[5] == board[6] != "   " or board[7] == board[8] == board[9] != "   ":
        check = 1
    # Column checking is done here
    elif board[1] == board[4] == board[7] != "   " or board[2] == board[5] == board[8] != "   " or board[3] == board[6] == board[9] != "   ":
        check = 1
    # Diagonal elements are checked here
    elif board[1] == board[5] == board[9] != "   " or board[3] == board[5] == board[7] != "   ":
        check = 1
    return check


def user_Input(board, symbol):
    sym1, sym2 = symbol[random.randint(0, 1)]
    print(sym1, " is going first")
    display_board(board)
    for i in range(9):
        if i % 2 == 0:
            turn = " "+sym1+" "
            valid_pos(board, turn)
        else:
            turn = " "+sym2+" "
            valid_pos(board, turn)
        if i >= 4:
            if check(board):
                print(turn, "Won :)")
                break
        if i == 8:
            print("No one won. It was a Tie.")
    play_again()
    
def play_again():
    while True:
        again = input("Do you want to play again(Y/N) : ").upper()
        if again == "Y":
            main()
            break
        elif again == "N" or again == " ":
            exit()
        else:
            print("Invalid input. Enter again.")


def main():
    board = ["Nothing", "   ", "   ", "   ",
             "   ", "   ", "   ", "   ", "   ", "   "]
    symbol = [("X", "O"), ("O", "X")]
    while True:
        marker = input("Enter your marker(X/O) : ").upper()
        if marker == "X" or marker == "O":
            user_Input(board, symbol)
            break
        elif marker == " ":
            print("Successfully exited the game")
            exit()
        else:
            print("Wrong marker used. Try again.")
            
            

print(f'''\n    --------------------------------------------------------------------------------------------------------------
    | This is a Tic Tac toe game. The rules of this game are as follows:                                         |
    |                                                                                                            |      
    |     1) You have to first select a marker (X/O)                                                             | 
    |                                                                                                            |
    |     2) Then select a postion where you want to place your marker                                           |
    |                                                                                                            |
    |     3) If any of the row, column or diagonal element becomes same for any player that player wins the match|
    |                                                                                                            |   
    |     4) If you want to exit the game any time press [space] or type N                                       |
    |                                                                                                            |
    |  HAPPY GAMING :)                                                                                           |
    --------------------------------------------------------------------------------------------------------------\n''')
main()
