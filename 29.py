class Game(object):

    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def draw(self):
        for j in range(0, self.size):
            print(" ---" * self.size)
            print("| ", end="")
            for i in range(0, self.size):
                print(self.board[j][i], "|", end=" ")

            print("")
        print(" ---" * self.size)
        print("")


    def askForInput(self, mark):
        while True:
            try:
                inputString=input("%s, it is your turn! Type the row and column (1-3) where you would like to put your %s in this format: r,c.:" % (mark, mark) )
                inputList=inputString.split(",")

                r = int(inputList[0])
                c = int(inputList[1])
                if  len(inputList) != 2:
                    print("Ohh, tooo many numbers")
                elif r < 1 or c < 1:
                    print ("Ohh, your numbers should be between 1 and 3")
                elif self.board[r - 1][c - 1] == 0:
                    self.board[r - 1][c - 1] = mark
                    break
                else:
                    print("Ohh, this field is already marked.")
            except ValueError as ve:
                print("Ohh, a ValueError")
            except IndexError as ie:
                print("Ohh, an IndexError, please check if your numbers are <= 3")
            except NameError as ne:
                print("Ohh, a NameError")
            # except Exception as e:
            #     print("Ohh, exception: " + str(e))

    def winCheck(self):
        horizontal=self.horizontalWin(self.board)
        if horizontal != NOBODY_WINS:
            return horizontal

        vertical=self.verticalWin(self.board)
        if vertical != NOBODY_WINS:
            return vertical

        diagonal=self.diagonalWin(self.board)
        if diagonal != NOBODY_WINS:
            return diagonal

        return NOBODY_WINS

    def play(self):
        counter = 0
        while True:
            self.askForInput("X")
            self.draw()

            winCheckValue=self.winCheck()
            if winCheckValue==FIRST_WINS:
                print(FIRST_WINS)
                break
            elif winCheckValue==SECOND_WINS:
                print(SECOND_WINS)
                break
            counter += 1

            if counter >= 9:
                print("Draw")
                break

            self.askForInput("Y")
            self.draw()
            self.winCheck()
            winCheckValue = self.winCheck()
            if winCheckValue == FIRST_WINS:
                print(FIRST_WINS)
                break
            elif winCheckValue == SECOND_WINS:
                print(SECOND_WINS)
                break
            counter += 1


    def numberToWinner(self,mark):
        if mark == 'X':
            return FIRST_WINS
        elif mark == 'Y':
            return SECOND_WINS
        else:
            raise ValueError("Unexpected winner")

    def all_same(self,items):
        return all(x == items[0] for x in items)

    def horizontalWin(self,board):
        N = len(board)

        for j in range(0, N):
            rowList = []
            for i in range(0, N):
                rowList.append(board[j][i])

            if (self.all_same(rowList)) and rowList[0] != 0:
                return self.numberToWinner(rowList[0])

        return NOBODY_WINS

    def verticalWin(self,board):
        N = len(board)

        for i in range(0, N):
            rowList = []
            for j in range(0, N):
                rowList.append(board[j][i])

            if (self.all_same(rowList)) and rowList[0] != 0:
                return self.numberToWinner(rowList[0])

        return NOBODY_WINS

    def diagonalWin(self,board):
        N = len(board)
        rowList = []
        for i in range(0, N):
            rowList.append(board[i][i])

        if (self.all_same(rowList)) and rowList[0] != 0:
            return self.numberToWinner(rowList[0])

        rowList = []
        for i in range(0, N):
            rowList.append(board[i][N - 1 - i])

        if (self.all_same(rowList)) and rowList[0] != 0:
            return self.numberToWinner(rowList[0])

        return NOBODY_WINS

FIRST_WINS = "First player wins"
SECOND_WINS = "Second player wins"
NOBODY_WINS = "Nobody won"



def main():
    g=Game(3)
    g.play()

if __name__ == "__main__":
    main()

