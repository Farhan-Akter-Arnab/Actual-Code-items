theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
board_keys = []
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+--+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+--+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn, Mr. " + turn + ". Move to which place? (1-9)")
        move = input()
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("The place is already occupied. Try again to choose another place.")
            continue
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** Mr. " + turn + " has won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** Mr. " + turn + " has won. ****")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** Mr. " + turn + " has won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** Mr. " + turn + " has won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** Mr. " + turn + " has won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** Mr. " + turn + " has won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** Mr. " + turn + " has won. ****")
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** Mr. " + turn + " has won. ****")
                break
        if count == 8:
            print("All boxes have been occupied.")
            print("\nGame Over.\n")
            print("**** It's a Tie! ****")
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("Do you want to play again? (y/n): ").lower()
    if restart == 'y':
        for key in board_keys:
            theBoard[key] = ' '
        game()
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe! This is a two-player game where players are human-to-human.")
    print("To play, enter the number corresponding to the position on the board. The first box is at the top left corner and the ninth box is at the bottom right corner.")
    print("As per the rules of the game, 'X' will play first.")
    game()