# 1. main: endless loop: askP1ForInput(), draw(), askP2ForInput(), draw() --- global board
# 2. improve draw
#   a. spaces
#   b. actual board
# 3. refactor to askForInput(character) with character being 'x' or 'o'
# 4. introduce counter, break loop when 9
# 5. create a game class with the board being a member, main is only 2 lines: game = Game() \ game.play()

def askP1ForInput(board):
    inputP1=input("P1, it is your turn! Type the row and column (1-3) where you would like to put your X in this format: r,c.:")
    inputP1List=inputP1.split(",")

    r = int(inputP1List[0])
    c = int(inputP1List[1])

    board[r - 1][c - 1] = "X"

def askP2ForInput(board):
    inputP2=input("P2, it is your turn! Type the row and column (1-3) where you would like to put your Y in this format: r,c.:")
    inputP2List = inputP2.split(",")

    r = int(inputP2List[0])
    c = int(inputP2List[1])

    board[r - 1][c - 1] = "Y"

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
        askP1ForInput(board)
        draw(board)
        askP2ForInput(board)
        draw(board)
        counter=counter+1

if __name__=="__main__":
    main()

