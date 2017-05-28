from enum import Enum


class Game(object):

    class WinState(Enum):
        FIRST_WINS = "First player wins"
        SECOND_WINS = "Second player wins"
        NOBODY_WINS = "Nobody wins"

    def __init__(self, size):
        self.size = size
        self.numFields = self.size ** 2

        self.board = None
        self.counter = None

    def play(self):
        self.__resetBoard()
        while True:
            if self.__turnAndCheckGameOver('X'):
                break

            if self.__turnAndCheckGameOver('Y'):
                break

    # Private methods

    def __resetBoard(self):
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.counter = 0

    def __turnAndCheckGameOver(self, mark):
        self.__askForInput(mark)
        self.__drawBoard()
        if self.__isGameOver():
            return True

        self.counter += 1
        if self.counter >= self.numFields:
            print("Draw")
            return True

    def __drawBoard(self):
        for j in range(0, self.size):
            print(" ---" * self.size)
            print("| ", end="")
            for i in range(0, self.size):
                print(self.board[j][i], "|", end=" ")

            print("")
        print(" ---" * self.size)
        print("")

    def __askForInput(self, mark):
        while True:
            try:
                inputString = input("%s, it is your turn! Type the row and column (1-3)"
                                    " where you would like to put your %s in this format: r,c.:" % (mark, mark))
                inputList = inputString.split(",")

                r = int(inputList[0])
                c = int(inputList[1])
                if len(inputList) != 2:
                    print("Ohh, too many numbers.")
                elif r < 1 or c < 1:
                    print("Ohh, your numbers should positive integers.")
                elif self.board[r - 1][c - 1] == 0:
                    self.board[r - 1][c - 1] = mark
                    break
                else:
                    print("Ohh, this field is already marked.")
            except ValueError as ve:
                print("Ohh, a ValueError: " + str(ve))
            except IndexError:
                print("Ohh, an IndexError, please check if your numbers are <= %s" % str(self.size))
            except NameError as ne:
                print("Ohh, a NameError: " + str(ne))
            except Exception as e:
                print("Ohh, Exception: " + str(e))

    def __winCheck(self):
        horizontal = self.__horizontalWin()
        if horizontal != Game.WinState.NOBODY_WINS:
            return horizontal

        vertical = self.__verticalWin()
        if vertical != Game.WinState.NOBODY_WINS:
            return vertical

        return self.__diagonalWin()

    def __isGameOver(self):
        if self.__winCheck() == Game.WinState.FIRST_WINS:
            print(Game.WinState.FIRST_WINS.value)
            return True

        if self.__winCheck() == Game.WinState.SECOND_WINS:
            print(Game.WinState.SECOND_WINS.value)
            return True

        return False

    @staticmethod
    def __markToWinner(mark):
        if mark == 'X':
            return Game.WinState.FIRST_WINS
        elif mark == 'Y':
            return Game.WinState.SECOND_WINS
        else:
            raise ValueError("Unexpected winner")
        
    @staticmethod
    def __allSame(items):
        return all(x == items[0] for x in items)

    def __horizontalWin(self):
        N = len(self.board)

        for j in range(0, N):
            rowList = []
            for i in range(0, N):
                rowList.append(self.board[j][i])

            if (Game.__allSame(rowList)) and rowList[0] != 0:
                return Game.__markToWinner(rowList[0])

        return Game.WinState.NOBODY_WINS

    def __verticalWin(self):
        N = len(self.board)

        for i in range(0, N):
            columnList = []
            for j in range(0, N):
                columnList.append(self.board[j][i])

            if (Game.__allSame(columnList)) and columnList[0] != 0:
                return Game.__markToWinner(columnList[0])

        return Game.WinState.NOBODY_WINS

    def __diagonalWin(self):
        N = len(self.board)
        mainDiagonalList = []
        for i in range(0, N):
            mainDiagonalList.append(self.board[i][i])

        if (Game.__allSame(mainDiagonalList)) and mainDiagonalList[0] != 0:
            return Game.__markToWinner(mainDiagonalList[0])

        secondaryDiagonalList = []
        for i in range(0, N):
            secondaryDiagonalList.append(self.board[i][N - 1 - i])

        if (Game.__allSame(secondaryDiagonalList)) and secondaryDiagonalList[0] != 0:
            return Game.__markToWinner(secondaryDiagonalList[0])

        return Game.WinState.NOBODY_WINS


def main():
    g = Game(3)
    g.play()

if __name__ == "__main__":
    main()

