# 1. [X] main: endless loop: askP1ForInput(), draw(), askP2ForInput(), draw() --- global board
# 2. improve draw
#   a. [X] spaces
#   b. actual board
# 3. [X] refactor to askForInput(character) with character being 'x' or 'o'
# 4. [X] introduce counter, break loop when 9
# 5. [X]create a game class with the board being a member, main is only 2 lines: game = Game() \ game.play()
# 6. [X]do not allow overwriting any mark
# 7. [X]handle all kinds of exceptions separately, with useful error messages

# [X]delete board param, use self.board

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

    def play(self):
        counter = 0
        while counter <= 9:
            self.askForInput("X")
            self.draw()
            self.askForInput("Y")
            self.draw()
            counter += 1


def main():
    g=Game(4)
    g.play()

if __name__ == "__main__":
    main()

