def selectSign():
    while (userSign != "X") and (userSign != "O"):
        userSign = input("Do you want to be 'X' or 'O'?")
        if userSign == "X":
            computerSign == "O"
        else:
            computerSign == "X"

    return userSign, computerSign
        
if main == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    userSign = ""
    computerSign = ""
    user = selectSign()