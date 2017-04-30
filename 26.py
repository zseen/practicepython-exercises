# game = [[2, 1, 1],
# 	    [2, 1, 2],
# 	    [2, 2, 1]]
#
# firstWins="First player wins"
# secondWins="Second player wins"
# noneWins="Nobody won"

# def horizontalWin(game):
#     if game[0][0]==game[0][1]==game[0][2] or game[1][0]==game[1][1]==game[1][2] or game[2][0]==game[2][1]==game[2][2]:
#         if game[0][0] == 1 and game[0][1] == 1 and game[0][2] == 1:
#             return firstWins
#         elif game [1][0] == 1 and game[1][1] == 1 and game[1][2] == 1:
#             return firstWins
#         elif game [2][0] == 1 and game[2][1] == 1 and game[2][2] == 1:
#             return firstWins
#
#         elif game[0][0] == 2 and game[0][1] == 2 and game[0][2] == 2:
#             return secondWins
#         elif game [1][0] == 2 and game[1][1] == 2 and game[1][2] == 2:
#             return secondWins
#         elif game [2][0] == 2 and game[2][1] == 2 and game[2][2] == 2:
#             return secondWins
#     else:
#         return noneWins
#
# def verticalWin(game):
#     if game[0][0]==game[1][0]==game[2][0] or game[0][1]==game[1][1]==game[2][1] or game[0][2]==game[1][2]==game[2][2]:
#         if game [0][0] == 1 and game[1][0] == 1 and game[2][0] == 1:
#             return firstWins
#         elif game [0][1] == 1 and game[1][1] == 1 and game[2][1] == 1:
#             return firstWins
#         elif game [0][2]== 1 and game[1][2] == 1 and game[2][2] == 1:
#             return firstWins
#
#         elif game [0][0] == 2 and game[1][0] == 2 and game[2][0] == 2:
#             return secondWins
#         elif game [0][1] == 2 and game[1][1] == 2 and game[2][1] == 2:
#             return secondWins
#         elif game [0][2] == 2 and game[1][2] == 2 and game[2][2] == 2:
#             return secondWins
#     else:
#         return noneWins
#
# def diagonalWin(game):
#     if game[0][0]==game[1][1]==game[2][2]:
#         if game[0][0] == 1:
#             return firstWins
#         elif game[0][0] == 2:
#             return secondWins
#     if game[0][2]==game[1][1]==game[2][0]:
#         if game[0][2] == 1:
#             return firstWins
#         elif game[0][2] == 2:
#             return secondWins
#     else:
#         return noneWins

# def main():
#     if horizontalWin(game)== firstWins or verticalWin(game)== firstWins or diagonalWin(game) == firstWins:
#         print ("The first player won")
#     elif horizontalWin(game)== secondWins or verticalWin(game)== secondWins or diagonalWin(game) == secondWins:
#         print ("The second player won")
#     else:
#         print("No one won")
#
# if __name__=="__main__":
#     main()


####TRY

game = [[2, 1, 1],
	    [1, 2, 2],
	    [1, 2, 2]]

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
    if horizontalWin(game)== firstWins or verticalWin(game)== firstWins or diagonalWin(game) == firstWins:
        print ("The first player won")
    elif horizontalWin(game)== secondWins or verticalWin(game)== secondWins or diagonalWin(game) == secondWins:
        print ("The second player won")
    else:
        print("No one won")

if __name__=="__main__":
    main()




# if verticalWin(game)==firstWins:
#     print ("a")
# elif verticalWin(game)==secondWins:
#     print ("b")
# if horizontalWin(game)==firstWins:
#     print ("c")
# elif horizontalWin(game)==secondWins:
#     print ("d")
#
# if diagonalWin(game)==firstWins:
#     print ("e")
# elif diagonalWin(game)==secondWins:
#     print ("f")



