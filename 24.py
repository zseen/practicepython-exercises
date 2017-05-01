
def gameBoard(lines):
    for _ in range(1, lines+1):
        print(" ---" * lines)
        print("|   " * lines + "|")
    print(" ---" * lines)



def main():
    size = int(input("What size would you like?"))
    gameBoard(size)


if __name__=="__main__":
    main()
