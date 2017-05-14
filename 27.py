# 1. [X] main: endless loop: askP1ForInput(), draw(), askP2ForInput(), draw() --- global board
# 2. improve draw
#   a. [X] spaces
#   b. actual board
# 3. [X] refactor to askForInput(character) with character being 'x' or 'o'
# 4. [X] introduce counter, break loop when 9
# 5. create a game class with the board being a member, main is only 2 lines: game = Game() \ game.play()
# 6. do not allow overwriting any mark
# 7. handle all kinds of exceptions separately, with useful error messages

def askForInput(board, mark):

    while True:
        try:
            inputString=input("%s, it is your turn! Type the row and column (1-3) where you would like to put your %s in this format: r,c.:" % (mark, mark) )
            inputList=inputString.split(",")

            r = int(inputList[0])
            c = int(inputList[1])
            if board[r - 1][c - 1] == 0:
                board[r - 1][c - 1] = mark
                break
            else:
                print("Ohh, this field is already marked.")
        except Exception as e:
            print("Ohh, exception: " + str(e))

def draw(board):
    N=3
    for j in range(0, N):
        for i in range(0, N):
            print(board[j][i], end=" ")

        print("")

def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    counter=0

    while counter<=9:
        askForInput(board, "X")
        draw(board)
        askForInput(board, "Y")
        draw(board)
        counter += 1

if __name__=="__main__":
    main()

