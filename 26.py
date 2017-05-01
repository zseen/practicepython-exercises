import unittest

FIRST_WINS= "First player wins"
SECOND_WINS= "Second player wins"
NOBODY_WINS= "Nobody won"

def numberToWinner(number):
    if number == 1:
        return FIRST_WINS
    elif number == 2:
        return SECOND_WINS
    else:
        raise ValueError("Unexpected winner")

def all_same(items):
    return all(x == items[0] for x in items)

def horizontalWin(game):
    N = len(game)

    for j in range(0, N):
        rowList = []
        for i in range(0, N):
            rowList.append(game[j][i])

        if(all_same(rowList)) and rowList[0] != 0:
            return numberToWinner(rowList[0])

    return NOBODY_WINS

def verticalWin(game):
    N = len(game)

    for i in range(0, N):
        rowList = []
        for j in range(0, N):
            rowList.append(game[j][i])

        if (all_same(rowList)) and rowList[0] != 0:
            return numberToWinner(rowList[0])

    return NOBODY_WINS

def diagonalWin(game):
    N = len(game)


    rowList = []
    for i in range(0, N):
        rowList.append(game[i][i])

    if (all_same(rowList)) and rowList[0] != 0:
        return numberToWinner(rowList[0])


    rowList = []
    for i in range(0, N):
        rowList.append(game[i][N-1-i])

    if (all_same(rowList)) and rowList[0] != 0:
        return numberToWinner(rowList[0])

    return NOBODY_WINS



def main():
    game = [[2, 1, 1],
            [1, 2, 2],
            [1, 2, 2]]

    if horizontalWin(game)== FIRST_WINS or verticalWin(game)== FIRST_WINS or diagonalWin(game) == FIRST_WINS:
        print ("The first player won")
    elif horizontalWin(game)== SECOND_WINS or verticalWin(game)== SECOND_WINS or diagonalWin(game) == SECOND_WINS:
        print ("The second player won")
    else:
        print ("No one won")

class TestWinChecking(unittest.TestCase):

    # ---- Horizontal win ----

    def test_HorizontalWin_FirstLineAllOnes_FirstPlayerWins(self):
        game = [[1, 1, 1],
                [0, 0, 0],
                [0, 0, 0]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == FIRST_WINS)

    def test_HorizontalWin_SecondLineAllOnes_FirstPlayerWins(self):
        game = [[0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == FIRST_WINS)

    def test_HorizontalWin_ThirdLineAllOnes_FirstPlayerWins(self):
        game = [[0, 0, 0],
                [0, 0, 0],
                [1, 1, 1]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == FIRST_WINS)

    def test_NoWins_RandomLines_NoOneWins(self):
        game = [[0, 1, 0],
                [2, 0, 0],
                [1, 2, 1]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == NOBODY_WINS)

    def test_HorizontalWin_ThirdLineAllTwos_SecondPlayerWins(self):
        game = [[0, 0, 0],
                [0, 0, 0],
                [2, 2, 2]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == SECOND_WINS)

    # ---- Vertical win ----

    def test_VerticalWin_FirstColumnAllOnes_FirstPlayerWins(self):
        game = [[1, 0, 0],
                [1, 0, 0],
                [1, 2, 2]]
        verticWinResult = verticalWin(game)
        self.assertTrue(verticWinResult == FIRST_WINS)

    def test_VerticalWin_SecondColumnAllOnes_FirstPlayerWins(self):
        game = [[2, 1, 0],
                [0, 1, 0],
                [0, 1, 2]]
        verticWinResult = verticalWin(game)
        self.assertTrue(verticWinResult == FIRST_WINS)

    def test_VerticalWin_ThirdColumnAllTwos_SecondPlayerWins(self):
        game = [[2, 1, 2],
                [0, 0, 2],
                [0, 1, 2]]
        verticWinResult = verticalWin(game)
        self.assertTrue(verticWinResult == SECOND_WINS)

    def test_VerticalWin_RandomLines_NoOneWins(self):
        game = [[2, 1, 2],
                [0, 0, 1],
                [0, 1, 2]]
        verticWinResult = verticalWin(game)
        self.assertTrue(verticWinResult == NOBODY_WINS)

    def test_VerticalWin_ThirdColumnAllOnes_FirstPlayerWins(self):
        game = [[2, 1, 1],
                [0, 0, 1],
                [0, 1, 1]]
        verticWinResult = verticalWin(game)
        self.assertTrue(verticWinResult == FIRST_WINS)

    # ---- Diagonal win ----

    def test_DiagonalWin_FirstUpperCornerOnes_FirstPlayerWins(self):
        game = [[1, 0, 2],
                [0, 1, 1],
                [0, 1, 1]]
        diagWinResult = diagonalWin(game)
        self.assertTrue(diagWinResult == FIRST_WINS)

    def test_DiagonalWin_FirstUpperCornerTwos_SecondPlayerWins(self):
        game = [[2, 0, 2],
                [0, 2, 1],
                [0, 1, 2]]
        diagWinResult = diagonalWin(game)
        self.assertTrue(diagWinResult == SECOND_WINS)

    def test_DiagonalWin_SecondUpperCornerOnes_FirstPlayerWins(self):
        game = [[2, 0, 1],
                [0, 1, 1],
                [1, 1, 2]]
        diagWinResult = diagonalWin(game)
        self.assertTrue(diagWinResult == FIRST_WINS)

    def test_DiagonalWin_SecondUpperCornerTwos_SecondPlayerWins(self):
        game = [[2, 0, 2],
                [0, 2, 1],
                [2, 1, 1]]
        diagWinResult = diagonalWin(game)
        self.assertTrue(diagWinResult == SECOND_WINS)



    def test_DiagonalWin_RandomLines_NoOneWins(self):
        game = [[2, 0, 1],
                [0, 0, 1],
                [1, 1, 2]]
        diagWinResult = diagonalWin(game)
        self.assertTrue(diagWinResult == NOBODY_WINS)








if __name__=="__main__":
    unittest.main()
