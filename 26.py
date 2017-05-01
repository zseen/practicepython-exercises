import unittest

firstWins="First player wins"
secondWins="Second player wins"
noneWins="Nobody won"

def horizontalWin(game):
    if game[0][0]==game[0][1]==game[0][2]==1 or game[1][0]==game[1][1]==game[1][2]==1 or game[2][0]==game[2][1]==game[2][2]==1:
        return firstWins
    elif game[0][0]==game[0][1]==game[0][2]==2 or game[1][0]==game[1][1]==game[1][2]==2 or game[2][0]==game[2][1]==game[2][2]==2:
        return secondWins
    else:
        return noneWins

def verticalWin(game):
    if game[0][0]==game[1][0]==game[2][0]==1 or game[0][1]==game[1][1]==game[2][1]==1 or game[0][2]==game[1][2]==game[2][2]==1:
        return firstWins

    elif game[0][0]==game[1][0]==game[2][0]==2 or game[0][1]==game[1][1]==game[2][1]==2 or game[0][2]==game[1][2]==game[2][2]==2:
        return secondWins
    else:
        return noneWins

def diagonalWin(game):
    if game[0][0]==game[1][1]==game[2][2]==1:
        return firstWins
    elif game[0][0] == game[1][1] == game[2][2] == 2:
        return secondWins

    if game[0][2]==game[1][1]==game[2][0]==1:
        return firstWins
    elif game[0][2] == game[1][1] == game[2][0] == 2:
        return secondWins
    else:
        return noneWins

def main():
    game = [[2, 1, 1],
            [1, 2, 2],
            [1, 2, 2]]

    if horizontalWin(game)== firstWins or verticalWin(game)== firstWins or diagonalWin(game) == firstWins:
        print ("The first player won")
    elif horizontalWin(game)== secondWins or verticalWin(game)== secondWins or diagonalWin(game) == secondWins:
        print ("The second player won")
    else:
        print ("No one won")

class TestWinChecking(unittest.TestCase):

    def test_HorizontalWin_FirstLineAllOnes_FirstPlayerWins(self):
        game = [[1, 1, 1],
                [0, 0, 0],
                [0, 0, 0]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == firstWins)

    def test_HorizontalWin_SecondLineAllOnes_FirstPlayerWins(self):
        game = [[0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == firstWins)

    def test_HorizontalWin_ThirdLineAllOnes_FirstPlayerWins(self):
        game = [[0, 0, 0],
                [0, 0, 0],
                [1, 1, 1]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == firstWins)

    def test_NoWins_RandomLines_NoOneWins(self):
        game = [[0, 1, 0],
                [2, 0, 0],
                [1, 2, 1]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == noneWins)

    def test_HorizontalWin_ThirdLineAllTwos_SecondPlayerWins(self):
        game = [[0, 0, 0],
                [0, 0, 0],
                [2, 2, 2]]
        horizWinResult = horizontalWin(game)
        self.assertTrue(horizWinResult == secondWins)

if __name__=="__main__":
    unittest.main()
