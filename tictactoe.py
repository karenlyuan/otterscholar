from tkinter import *
from tkinter import messagebox
import random

# root = Tk()
# root.title("Tic-Tac-Toe")
# root.geometry("400x450")

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

# # button clicked function
# def bclick(b):
#     pass

# # buttons on board
# b1 = Button(root, text = " ", font = ("Helvetica", 15), height = 3, width = 6, bg = "SystemButtonFace", command = Lambda: b_click(b1))

def printBoard(board):
    print('-' * 12)
    print('\n')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\n')
    print('-' * 12)

def selectSign():
    """
    The function allows the user to select to play 
    as 'X' or 'O'. 
    returns userSign and computerSign
    """
    userSign = ""
    computerSign = ""

    while (userSign != "X") and (userSign != "O"):
        userSign = input("Do you want to be 'X' or 'O'?\n").upper()
        if (userSign != "X") and (userSign != "O"):
            print("That is an invalid choice.")
        elif userSign == "X":
            print("You are X")
            computerSign = "O"
        else:
            print("You are O")
            computerSign = "X"

    return userSign, computerSign

def spaceIsFree(position):
    if board[position] == " ":
        return True
    else:
        return False
    
def checkForDraw():
    for key in board.keys():
        if board[key] == " ":
            return False
    return True

def checkForWin():
    if (board[1] == board[2] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position) == True:
        board[position] = letter
        printBoard(board)
        if checkForWin():
            if letter == bot:
                print('You lost!')
                exit()
            else:
                print('You win!')
                exit()
        
        if checkForDraw():
            print("Draw!")
            exit()

        return
            
    else:
        print("That position has been filled.")
        position = int(input("Enter new position: "))
        print()
        insertLetter(letter, position)
    
        return


def playerMove():
    position = input("Enter the position number 1-9 for '" + player + "': ")
    if position.isdigit():
        position = int(position)
        if 1 <= position <= 9:
            insertLetter(player, position)
            return
        else:
            print("That is an invalid option.\n")
            playerMove()
    else:
        print("That is an invalid option. Please enter an integer from 1-9.\n")
        playerMove()

    
def botMove():
    position = random.randint(1,9)
    if spaceIsFree(position) == True:
        print()
        insertLetter(bot, position)
        return
    else:
        botMove()


print("Welcome to Tic-Tac-Toe!\n")
printBoard(board)
player, bot = selectSign()

while not checkForWin():
    playerMove()
    botMove()

# root.mainloop()


