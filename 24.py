
def gameBoard(x):
    for lines in range (1,x+1):
        print ("---  " *x)
        print ("|   " *x + "|")
    print ("---  " *x)



def main():
    x = int(input("What size would you like?"))
    gameBoard(x)


if __name__=="__main__":
    main()

    