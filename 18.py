import random


MAXGENERATED=3

def getUserInput():
    while True:
        try:
            guessList = list(input('Guess a 4 digit number please:'))

            guessListOfInts = []
            for x in guessList:
                guessListOfInts.append(int(x))
        except Exception as e:
            print("Exception when parsing input: %s" %e)
            continue

        #validate input
        if len(guessListOfInts)!=4:
            print ("4 digits please")
        elif guessListOfInts[0] == 0:
            print ("Cannot start with 0")
        else:
            break

    return guessListOfInts

def getComputerList():
    randlist=[]
    randlist.append(random.randrange(1, MAXGENERATED))
    for i in range(3):
        randlist.append(random.randrange(0, MAXGENERATED))
    return randlist

def bull(numbersGuessed, numbersSolution):
    bullCount=0

    for i in range (len(numbersGuessed)):
        if numbersGuessed[i]==numbersSolution[i]:
            bullCount+=1

    return bullCount

def cow(numbersGuessed, numbersSolution, numberBull):
    cowCount=0
    copyNumbersSolution=[]
    for i in numbersSolution:
        copyNumbersSolution.append(i)
    for item in numbersGuessed:
        if item in copyNumbersSolution:
            cowCount+=1
            copyNumbersSolution.remove(item)

    return cowCount-numberBull


def main():
    randlist = getComputerList()
    resultOfBull=0

    while resultOfBull!=4:
        guesslist = getUserInput()
        print ("User guessed: %s" %guesslist)
        # print("The computer's list: %s" %randlist)

        #bull=right place,  cow=wrong place
        resultOfBull=bull(guesslist,randlist)
        print ("You have %s bulls" %str(resultOfBull))

        resultOfCow=cow(guesslist,randlist, resultOfBull)
        print ("You have %s cows" %str(resultOfCow))
    print ("You won")
if __name__=="__main__":
    main()

